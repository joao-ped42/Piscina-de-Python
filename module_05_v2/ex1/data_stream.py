from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.datas_processed: list[str] = []
        self.index: int = 0
        self.validated_data: set = set()

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        if (len(self.datas_processed) > 0):
            ret: tuple[int, str] = (self.index,
                                    self.datas_processed.pop(0))
            self.index += 1
            return (ret)
        print(" No more data to ingest")
        return (-1, "")


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if (isinstance(data, (int, float))):
            self.validated_data.add(data)
            return (True)
        elif (isinstance(data, list)):
            ret: bool = all(isinstance(num, (int, float))
                            for num in data)
            if (ret):
                self.validated_data.add(tuple(data))
            return (ret)
        return (False)

    def ingest(self, data: Any) -> None:
        if (isinstance(data, list)):
            if ((tuple(data) in self.validated_data) or (self.validate(data))):
                print(f" Processing {data}")
                for num in data:
                    if (str(num) not in self.datas_processed):
                        self.datas_processed.append(str(num))
            else:
                raise ValueError("Improper numeric data")
        elif (isinstance(data, (int, float))):
            if (data in self.validated_data or self.validate(data)):
                print(f" Processing {data}")
                ret: str = str(data)
                if (ret not in self.datas_processed):
                    self.datas_processed.append(ret)
        else:
            raise ValueError("Improper numeric data")


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if (isinstance(data, str)):
            self.validated_data.add(data)
            return (True)
        elif (isinstance(data, list)):
            ret: bool = all(isinstance(word, str)
                            for word in data)
            if (ret):
                self.validated_data.add(tuple(data))
            return (ret)
        return (False)

    def ingest(self, data: Any) -> None:
        if (isinstance(data, list)):
            if ((tuple(data) in self.validated_data) or (self.validate(data))):
                print(f" Processing {data}")
                for word in data:
                    if (word not in self.datas_processed):
                        self.datas_processed.append(word)
            else:
                raise ValueError("Improper text data")
        elif (isinstance(data, str)):
            if (data in self.validated_data or self.validate(data)):
                print(f" Processing {data}")
                if (data not in self.datas_processed):
                    self.datas_processed.append(data)
        else:
            raise ValueError("Improper text data")


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.validated_dicts: list = []

    @staticmethod
    def validate_dict(dic: dict) -> bool:
        keys: bool = all(isinstance(key, str)
                         for key in dic.keys())
        values: bool = all(isinstance(value, str)
                           for value in dic.values())
        ret: bool = keys and values
        return (ret)

    def validate(self, data: Any) -> bool:
        if (not isinstance(data, (dict, list))):
            return (False)
        elif (isinstance(data, dict)):
            ret: bool = self.validate_dict(data)
            if (ret):
                self.validated_dicts.append(data)
            return (ret)
        elif (isinstance(data, list)):
            for dic in data:
                if (not isinstance(dic, dict)):
                    return (False)
            ret = True
            for dic in data:
                ret = ret and self.validate_dict(dic)
            if (ret):
                self.validated_dicts.append(data)
            return (ret)
        return (False)

    def ingest(self, data: Any) -> None:
        if (isinstance(data, list)):
            if (data in self.validated_dicts or self.validate(data)):
                print(f" Processing {data}")
                for dic in data:
                    try:
                        self.datas_processed.append(
                            {dic["log_level"]: dic["log_message"]})
                    except KeyError:
                        print("Invalid kind of log level or message")
            else:
                raise ValueError("Improper log data")
        elif (isinstance(data, dict)):
            if (data in self.validated_dicts or self.validate(data)):
                print(f" Processing {data}")
                try:
                    self.datas_processed.append(
                        {data["log_level"]: data["log_message"]})
                except KeyError:
                    print(" Invalid kind of log level or message")
            else:
                raise ValueError("Improper log data")
        else:
            raise ValueError("Improper log data")


class DataStream:
    def __init__(self) -> None:
        self.processors: dict = {}
        print("\nInitialize Data Stream...")

    def register_processor(self, proc: DataProcessor) -> None:
        if (not isinstance(proc, DataProcessor)):
            print("\nRegister Fail")
            return
        key: str = ""
        if (isinstance(proc, NumericProcessor)):
            print("\nRegistering Numeric Processor")
            key = "num_proc"
        elif (isinstance(proc, TextProcessor)):
            print("\nRegistering Text Processor")
            key = "text_proc"
        else:
            print("\nRegistering Log Processor")
            key = "log_proc"
        self.processors.update({key: proc})

    def process_stream(self, stream: list[Any]) -> None:
        for data in stream:
            try:
                if (self.processors["num_proc"].validate(data)):
                    self.processors["num_proc"].ingest(data)
                elif (self.processors["text_proc"].validate(data)):
                    self.processors["text_proc"].ingest(data)
                elif (self.processors["log_proc"].validate(data)):
                    self.processors["log_proc"].ingest(data)
                else:
                    raise ValueError
            except (KeyError, ValueError):
                print(" DataStream error -",
                      f"Can't process element in stream: {data}")

    def count_data(self, proc_name: str) -> tuple[int, int]:
        processor: DataProcessor = self.processors[proc_name]
        ingested: int = len(processor.datas_processed)
        validated: int = 0

        if (proc_name == "log_proc"):
            log_processor: LogProcessor = self.processors["log_proc"]
            for log in log_processor.validated_dicts:
                if (isinstance(log, list)):
                    validated += len(log)
                else:
                    validated += 1
        else:
            for data in processor.validated_data:
                if (isinstance(data, tuple)):
                    validated += len(data)
                else:
                    validated += 1

        return (validated, ingested)

    def print_processors_stats(self) -> None:
        print("\n== DataStream statistics ==")
        if (len(self.processors) == 0):
            print("No processor found, no data")
            return
        proc_name: str = ""
        for processor in self.processors:
            if (processor == "num_proc"):
                proc_name = "Numeric Processor"
            elif (processor == "text_proc"):
                proc_name = "Text Processor"
            else:
                proc_name = "Log Processor"
            count: tuple[int, int] = self.count_data(processor)
            print(f"{proc_name}: total {count[0]} items processed,",
                  f"remaining {count[1]} on processor")


def main() -> None:
    data_stream: DataStream = DataStream()
    data_stream.print_processors_stats()

    num_proc: NumericProcessor = NumericProcessor()
    text_proc: TextProcessor = TextProcessor()
    log_proc: LogProcessor = LogProcessor()

    data_stream.register_processor(num_proc)
    data: list = ['Hello world',
                  [3.14, -1, 2.71],
                  [{'log_level': 'WARNING',
                    'log_message': 'Telnet access! Use ssh instead'},
                   {'log_level': 'INFO',
                    'log_message': 'User wil isconnected'}],
                  42, ['Hi', 'five']]
    try:
        data_stream.process_stream(data)
    except Exception as e:
        print(e)
    data_stream.print_processors_stats()

    data_stream.register_processor(text_proc)
    data_stream.register_processor(log_proc)
    try:
        data_stream.process_stream(data)
    except Exception as e:
        print(e)
    data_stream.print_processors_stats()

    data_stream.processors["num_proc"].output()
    data_stream.processors["num_proc"].output()
    data_stream.processors["num_proc"].output()
    data_stream.processors["text_proc"].output()
    data_stream.processors["text_proc"].output()
    data_stream.processors["log_proc"].output()
    data_stream.print_processors_stats()


if (__name__ == "__main__"):
    print("=== Code Nexus - Data Stream ===")
    main()
