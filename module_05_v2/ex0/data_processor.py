from typing import Any
from abc import ABC, abstractmethod


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
    def __init__(self):
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
                    self.datas_processed.append(str(num))
            else:
                raise ValueError("Improper numeric data")
        elif (isinstance(data, (int, float))):
            if (data in self.validated_data or self.validate(data)):
                print(f" Processing {data}")
                ret: str = str(data)
                self.datas_processed.append(ret)
        else:
            raise ValueError("Improper numeric data")


class TextProcessor(DataProcessor):
    def __init__(self):
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
                for num in data:
                    self.datas_processed.append(str(num))
            else:
                raise ValueError("Improper text data")
        elif (isinstance(data, str)):
            if (data in self.validated_data or self.validate(data)):
                print(f" Processing {data}")
                self.datas_processed.append(data)
        else:
            raise ValueError("Improper text data")


class LogProcessor(DataProcessor):
    def __init__(self):
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
                            f"{dic["log_level"]}: {dic["log_message"]}")
                    except KeyError:
                        print("Invalid kind of log level or message")
            else:
                raise ValueError("Improper log data")
        elif (isinstance(data, dict)):
            if (data in self.validated_dicts or self.validate(data)):
                print(f" Processing {data}")
                try:
                    self.datas_processed.append(
                        f"{data["log_level"]}: {data["log_message"]}")
                except KeyError:
                    print(" Invalid kind of log level or message")
            else:
                raise ValueError("Improper log data")
        else:
            raise ValueError("Improper log data")


def numeric_processor() -> None:
    print("\nTesting Numeric Processor...")
    num_proc: NumericProcessor = NumericProcessor()
    print(" Trying to validate input '42':",
          num_proc.validate(42))
    print(" Trying to validate input 'Hello':",
          num_proc.validate("Hello"))
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_proc.ingest("foo")
    except ValueError as e:
        print(f" Got exception: {e}")
    try:
        num_proc.ingest([1, 2, 3, 4, 5])
    except ValueError as e:
        print(f" Got exception: {e}")
    limit: int = 3
    print(f" Extracting {limit} values...")
    for _ in range(limit):
        output: tuple[int, str] = num_proc.output()
        if (-1 not in output):
            print(f" Numeric value {output[0]}: {output[1]}")


def text_processor() -> None:
    print("\nTesting Text Processor...")
    text_proc: TextProcessor = TextProcessor()
    print(" Trying to validate input '42':",
          text_proc.validate(42))
    text_proc.validate(["Hello", "Nexus", "World"])
    try:
        text_proc.ingest(["Hello", "Nexus", "World"])
    except ValueError as e:
        print(f" Got exception: {e}")
    limit: int = 1
    print(f" Extracting {limit} values...")
    for _ in range(limit):
        output = text_proc.output()
        if (-1 not in output):
            print(f" Text value {output[0]}: {output[1]}")


def log_processor() -> None:
    print("\nTesting Log Processor...")
    log_proc: LogProcessor = LogProcessor()
    print(" Trying to validate input 'Hello':", log_proc.validate("Hello"))
    try:
        log_proc.ingest([{'log_level': 'NOTICE',
                        'log_message': 'Connection to server'},
                         {'log_level': 'ERROR',
                         'log_message': 'Unauthorized access!!'}])
    except ValueError as e:
        print(f" Got exception: {e}")
    limit: int = 2
    print(f" Extracting {limit} values...")
    for _ in range(limit):
        output = log_proc.output()
        if (-1 not in output):
            print(f" Text value {output[0]}: {output[1]}")


def main() -> None:
    numeric_processor()
    text_processor()
    log_processor()


if (__name__ == "__main__"):
    print("=== Code Nexus - Data Processor ===")
    main()
