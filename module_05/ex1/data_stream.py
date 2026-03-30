from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


def int_to_str(num: int) -> str:
    if (num <= 0):
        return (str(num))
    else:
        return (f"+{str(num)}")


def ft_len(count: Any) -> int:
    n: int = 0
    for i in count:
        n += 1
    return (n)


class DataStream(ABC):
    def __init__(self,
                 stream_id: str) -> None:
        ids: List[str] = ["SENSOR", "TRANS", "EVENT"]
        if (stream_id.split("_")[0].upper() in ids):
            self.stream_id: str = stream_id.upper()
        else:
            raise ValueError("There's no such stream")
        self.type: str = "Generic"
        if (stream_id.split("_")[0].upper() == "SENSOR"):
            self.type = "Environmental Data"
        elif (stream_id.split("_")[0].upper() == "TRANS"):
            self.type = "Financial Data"
        elif (stream_id.split("_")[0].upper() == "EVENT"):
            self.type = "System Events"

    def list_to_dict(self, lst: List[str]) -> Dict[str, float]:
        ret: Dict[str, float] = {}
        for string in lst:
            try:
                key_value: List[str] = string.split(":")
                ret.update({key_value[0].lower(): float(key_value[1])})
            except Exception:
                print(f"Couldn't process {string}")
                return ({"error": 1})
        return (ret)

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        ret: List[Any] = []
        if (criteria == "high_priority"):
            for item in data_batch:
                if (item == "error"):
                    ret.append(item)
        return (ret)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        ret: Dict[str, Union[str, int, float]] = {}
        ret.update({"id": self.stream_id,
                    "type": self.type})
        return (ret)

    @abstractmethod
    def process_batch(self,
                      data_batch: List[Any]) -> str:
        pass


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.sensor_count: int = 0
        self.biggest_temp: float = -2147483648
        self.lowest_temp: float = 2147483647

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if (criteria == "high_priority"):
            try:
                stats: Dict[str, float] = self.list_to_dict(data_batch)
                if ("error" in stats):
                    raise ValueError("Something is wrong with data batch")
                ret: List[Any] = []
                for key in stats:
                    if ((key == "temp" and stats[key] > 36) or
                            (key == "humidity" and stats[key] > 70) or
                            (key == "pressure" and stats[key] > 1013.75)):
                        ret.append(key)
                return (ret)
            except Exception as e:
                print(e)
                return ([None])
        elif (criteria is None):
            return (data_batch)
        return ([None])

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        big_temp: Dict[str, Union[str, int, float]] = {}
        low_temp: Dict[str, Union[str, int, float]] = {}
        ret: Dict[str, Union[str, int, float]] =\
            {"batch_count": self.sensor_count}
        if (self.biggest_temp > -2147483648):
            big_temp.update({"highest_temp": self.biggest_temp})
        if (self.lowest_temp < 2147483647):
            low_temp.update({"lowest_temp": self.lowest_temp})
        ret.update(big_temp)
        ret.update(low_temp)
        return (ret)

    def process_batch(self,
                      data_batch: List[Any]) -> str:
        print("Processing sensor batch: [", end="")
        print(*data_batch, sep=', ', end="")
        print("]")
        sensor_dict: Dict[str, float] = self.list_to_dict(data_batch)
        if (not ("temp" in sensor_dict)):
            return ("No temperature found")
        self.sensor_count += 1
        if (sensor_dict["temp"] > self.biggest_temp):
            self.biggest_temp = sensor_dict["temp"]
        if (sensor_dict["temp"] < self.lowest_temp):
            self.lowest_temp = sensor_dict["temp"]
        return (f"Sensor Analysis: {len(data_batch)} readings processed, "
                f"avg temp: {sensor_dict['temp']}°C")


class TransactionStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        self.trans_count: int = 0
        self.buy_count: int = 0
        self.sell_count: int = 0
        self.biggest_buy: int = 0
        self.biggest_sell: int = 0

    def list_to_fake_dict(self, lst: List[str]) -> List[str | int]:
        ret: List[str | int] = []
        for string in lst:
            try:
                string_num: List[str] = string.split(":")
                ret += [string_num[0].lower(), int(string_num[1])]
            except Exception:
                print(f"Couldn't process {string}")
        return (ret)

    def count_units(self, transaction_list: Dict[str, float]) -> int:
        units: int = 0
        for key in transaction_list:
            if (key == "buy"):
                try:
                    units += int(transaction_list[key])
                    self.trans_count += 1
                    self.buy_count += 1
                    if (int(transaction_list[key]) > self.biggest_buy):
                        self.biggest_buy = int(transaction_list[key])
                except Exception as e:
                    print(e)
            elif (key == "sell"):
                try:
                    units -= int(transaction_list[key])
                    self.trans_count += 1
                    self.sell_count += 1
                    if (int(transaction_list[key]) > self.biggest_sell):
                        self.biggest_sell = int(transaction_list[key])
                except Exception as e:
                    print(e)
            else:
                print(f"There's no such kind of "
                      f"{key} transiction")
        return (units)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        ret: Dict[str, Union[str, int, float]] = {}
        ret.update({"total_transiction": self.trans_count,
                    "total_buy": self.buy_count,
                    "biggest_buy": self.biggest_buy,
                    "total_sell": self.sell_count,
                    "biggest_sell": self.biggest_sell})
        return (ret)

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if (criteria is None):
            return (data_batch)
        if (criteria == "high_priority"):
            ret: List[Any] = []
            transactions: Dict[str, float] = self.list_to_dict(data_batch)
            if ("error" in transactions):
                return ([None])
            for key in transactions:
                if (int(transactions[key]) > 100):
                    ret.append(int(transactions[key]))
        return (ret)

    def process_batch(self,
                      data_batch: List[Any]) -> str:
        print("Processing transaction batch: [", end="")
        print(*data_batch, sep=', ', end="")
        print("]")
        units: int = 0
        transactions: Dict[str, float] = self.list_to_dict(data_batch)
        units = self.count_units(transactions)
        return (f"Transiction analysis: "
                f"{ft_len(transactions)} operations, "
                f"{int_to_str(units)} units")


class EventStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        self.event_count: int = 0
        self.login_count: int = 0
        self.logout_count: int = 0
        self.error_count: int = 0

    def ft_event_len(self, lst: List[Any]) -> int:
        ret: int = 0
        for item in lst:
            if ((item in ["login", "error", "logout"])
                    and isinstance(item, str)):
                ret += 1
        return (ret)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        ret: Dict[str, Union[str, int, float]] = {}
        ret.update({"total_events": self.event_count,
                    "total_login": self.login_count,
                    "total_logout": self.logout_count,
                    "total_error": self.error_count})
        return (ret)

    def process_batch(self,
                      data_batch: List[Any]) -> str:
        print("Processing transaction batch: [", end="")
        print(*data_batch, sep=', ', end="")
        print("]")
        error_count: int = 0
        for event in data_batch:
            if (event.lower() == "error"):
                error_count += 1
        self.event_count = self.ft_event_len(data_batch)
        return (f"Event analysis: "
                f"{self.event_count} events, "
                f"{error_count} error detected")


class StreamProcessor:
    def __init__(self):
        try:
            self.sensor: SensorStream = SensorStream("SENSOr_001")
        except ValueError:
            print("Unable to create sensor stream")
        try:
            self.transaction: TransactionStream = TransactionStream(
                "TRANS_001")
        except ValueError:
            print("Unable to create transaction stream")
        try:
            self.event: EventStream = EventStream("EVENT_001")
        except ValueError:
            print("Unable to create event stream")

    def stream(self,
               data_batch: List[Any],
               data_type: str) -> None:
        streamer: DataStream
        if (data_type.lower() == "environmental"):
            print("\nInitializing Sensor Stream...")
            streamer = self.sensor
        elif (data_type.lower() == "financial"):
            print("\nInitializing Transaction Stream...")
            streamer = self.transaction
        elif (data_type.lower() == "event"):
            print("\nInitializing Event Stream...")
            streamer = self.event
        else:
            print(f"Can't process {data_type} type of data")
            return
        print(f"Stream ID: {streamer.stream_id}, "
              f"Type: {streamer.type}")
        print(streamer.process_batch(data_batch))


def filter_display(processor: StreamProcessor,
                   sensor_batch: List[Any],
                   trans_batch: List[Any],
                   event_batch: List[Any]) -> None:
    ret: str = ""
    sensor: int = len(processor.sensor.filter_data(sensor_batch,
                                                   "high_priority"))
    trans: int = len(processor.transaction.filter_data(trans_batch,
                                                       "high_priority"))
    event: int = len(processor.event.filter_data(event_batch, "high_priority"))
    if (sensor > 0):
        ret += f"{sensor} critical sensor alerts"
        if (trans > 0):
            ret += ", "
    if (trans > 0):
        ret += f"{trans} large transaction"
        if (event > 0):
            ret += ", "
    if (event > 0):
        ret += f"{event} error events"
    print(f"Filtered results: {ret}")


def main() -> None:
    processor: StreamProcessor = StreamProcessor()
    try:
        processor.stream(["temp:22.5", "humidity:65", "pressure:1013"],
                         "environmental")
    except Exception:
        print("Couldn't load sensor stream")
    try:
        processor.stream(["buy:100", "sell:150", "buy:75"],
                         "financial")
    except Exception:
        print("Couldn't load transaction stream")
    try:
        processor.stream(["login", "error", "logout"],
                         "event")
    except Exception:
        print("Couldn't load event stream")
    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    print("\nBatch 1 Results:")
    try:
        print("- Sensor data: "
              f"{processor.sensor.sensor_count} "
              "readings processed")
    except AttributeError:
        print("- There was no sensor stream")
    try:
        print("- Transaction data: "
              f"{processor.transaction.trans_count} "
              "operations processed")
    except AttributeError:
        print("- There was no transaction stream")
    try:
        print("- Event data: "
              f"{processor.event.event_count} "
              "events processed")
    except AttributeError:
        print("- There was no transaction stream")
    print("\nStream filtering active: High-priority data only")
    filter_display(processor,
                   ["temp:22.5", "humidity:65", "pressure:1013"],
                   ["buy:100", "sell:150", "buy:75"],
                   ["login", "error", "logout"])
    print("\nAll streams processed successfully. Nexus throughput optimal.")


if (__name__ == "__main__"):
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    main()
