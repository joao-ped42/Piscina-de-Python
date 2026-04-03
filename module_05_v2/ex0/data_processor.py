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
        elif (not isinstance(data, (str, dict, tuple, bool))):
            if (data in self.validated_data or self.validate(data)):
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
        pass


class LogProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    @staticmethod
    def validate_dict(dic: dict) -> bool:
        keys: bool = all(isinstance(key, str)
                         for key in dic.keys())
        values: bool = all(isinstance(value, str)
                           for value in dic.values())
        ret: bool = keys and values
        return (ret)

    def validate(self, data: Any) -> bool:
        return (False)

    def ingest(self, data: Any) -> None:
        pass


def main() -> None:
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
    num_proc.ingest([1, 2, 3, 4, 5])
    limit: int = 3
    print(f" Extracting {limit} values...")
    for _ in range(limit):
        output: tuple[int, str] = num_proc.output()
        if (-1 not in output):
            print(f" Numeric value {output[0]}: {output[1]}")

    print("\nTesting Text Processor...")
    text_proc: TextProcessor = TextProcessor()
    print(" Trying to validate input '42':",
          text_proc.validate(42))
    text_proc.validate(["Hello", "Nexus", "World"])
    text_proc.ingest(["Hello", "Nexus", "World"])
    limit = 1
    print(f" Extracting {limit} value...")
    for _ in range(limit):
        output = text_proc.output()
        if (-1 not in output):
            print(f" Text value {output[0]}: {output[1]}")


if (__name__ == "__main__"):
    print("=== Code Nexus - Data Processor ===")
    main()
