from typing import Any, List
from abc import ABC, abstractmethod


def ft_len(data: Any) -> int:
    count: int = 0
    for item in data:
        count += 1
    return (count)


def ft_sum(numbers: List[int | float]) -> int | float:
    ret: int | float = 0
    for number in numbers:
        ret = ret + number
    return (ret)


def ft_avg(numbers: List[int | float]) -> float:
    return (ft_sum(numbers) / ft_len(numbers))


def count_words(string: str) -> int:
    i: int = 0
    w: int = 0
    str_size: int = ft_len(string)
    while (i < str_size):
        while (i < str_size and string[i] == ' '):
            i += 1
        if (i < str_size):
            w += 1
        while (i < str_size and string[i] != ' '):
            i += 1
    return (w)


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return (f"Output: {result}")


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        return (f"Processed {ft_len(data)} numeric valuers, "
                f"sum={ft_sum(data)}, avg={ft_avg(data)}")

    def validate(self, data: Any) -> bool:
        if (None in data):
            raise ValueError("Invalid Data")
        print("Validation: Numeric data verified")
        return (True)


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        return (f"Processed text: {ft_len(data)} characters, "
                f"{count_words(data)} words")

    def validate(self, data: Any) -> bool:
        if (data is None):
            raise ValueError("Invalid Data")
        print("Validation: Text data verified")
        return (True)


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        return ("[INFO] INFO level detected: System ready")

    def validate(self, data: Any) -> bool:
        if (data is None):
            raise ValueError("Invalid Data")
        print("Validation: Log entry verified")
        return (True)


def print_message(data: Any, cls: DataProcessor) -> None:
    if (cls is NumericProcessor):
        print("\nInitializing Numeric Processor...")
    elif (cls is TextProcessor):
        print("\nInitializing Text Processor...")
    else:
        print("\nInitializing Log Processor...")
    try:
        print(f"Processing data: {data}")
        processed: str = cls.process(data)
        cls.validate(data)
    except Exception as error:
        print(f"Validation: [ERROR] {error}")
        processed: str = ("[ALERT] ERROR level detected: Connection timed out")
    finally:
        output: str = cls.format_output(processed)
        print(output)


def main() -> None:
    num_proc: DataProcessor = NumericProcessor()
    text_proc: DataProcessor = TextProcessor()
    log_proc: DataProcessor = LogProcessor()

    print_message([1, 2, 3, 4, 5], num_proc)
    print_message("Hello Nexus World", text_proc)
    print_message(None, log_proc)

    print("\n=== Polymorphic Processing Demo ===")
    print("\nProcessing multiple data types through same interface...")
    data_stream: list[tuple[DataProcessor | int | str]] =\
        [(num_proc, [1, 2, 3]),
         (text_proc, "Hello, World"),
         (log_proc, "Test")]
    i: int = 1
    for proc, data in data_stream:
        print(f"Result {i}: "
              f"{proc.process(data)}")
        i += 1
    print("\nFoundation systems online. Nexus ready for advanced streams.")


if (__name__ == "__main__"):
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    main()
