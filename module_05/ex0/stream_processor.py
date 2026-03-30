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
        try:
            return (f"Processed {ft_len(data)} numeric valuers, "
                    f"sum={ft_sum(data)}, avg={ft_avg(data)}")
        except Exception:
            return ("Invalid data")

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
        if (data.__class__.__name__ == "str"):
            print("Validation: Text data verified")
            return (True)
        print("Invalid data")
        return (False)


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if ((not (":" in data)) or (not (data.__class__.__name__ == "str"))):
            return ("Invalid log")
        log_split: list[str] = data.split(":")
        message_types: dict[str, str] = {"ERROR": "[ALERT]",
                                         "INFO": "[INFO]",
                                         "DEBUG": "[DEBUG]",
                                         "CRITICAL": "[ALERT]",
                                         "WARNING": "[ALERT]"}
        return (f"{message_types[log_split[0].upper()]} "
                f"{log_split[0].upper()} level detected:"
                f"{log_split[1]}")

    def validate(self, data: Any) -> bool:
        log_types: set[str] = {"DEBUG", "ERROR", "WARNING", "INFO", "CRITICAL"}
        if (data is None):
            raise ValueError("Invalid Data")
        log_type: str = (data.split(":")[0]).upper()
        if (log_type in log_types):
            print("Validation: Log entry verified")
            return (True)
        print("Validation: Invalid log entry")
        return (False)


def print_message(data: Any, cls: DataProcessor) -> None:
    if (cls.__class__ is NumericProcessor):
        print("\nInitializing Numeric Processor...")
    elif (cls.__class__ is TextProcessor):
        print("\nInitializing Text Processor...")
    else:
        print("\nInitializing Log Processor...")
    try:
        print(f"Processing data: {data}")
        processed: str = cls.process(data)
        cls.validate(data)
        output: str = cls.format_output(processed)
        print(output)
    except Exception as error:
        print(f"Validation: {error}")
        print("Output: Invalid Data")


def main() -> None:

    num_proc: DataProcessor = NumericProcessor()
    text_proc: DataProcessor = TextProcessor()
    log_proc: DataProcessor = LogProcessor()

    print_message([1, 2, 3, 4, 5], num_proc)
    print_message("Hello World!", text_proc)
    print_message("ERROR: Connection timeout", log_proc)

    print("\n=== Polymorphic Processing Demo ===")
    processors: List[tuple]
    processors = [(num_proc, [1, 2, 3]),
                  (text_proc, "sonic naruto"),
                  (log_proc, "INFO: System ready")]
    i: int = 1
    print("\nProcessing multiple data types through same interface...")
    for processor, data in processors:
        print(f"Result {i}: {processor.process(data)}")
        i += 1


if (__name__ == "__main__"):
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    main()
    print("\nFoundation systems online. Nexus ready for advanced streams.")
