from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def __init__(self):
        print("Initializing Numeric Processor...")

    def process(self, data: Any) -> str:
        print(f"Processing data: {data}")
        try:
            sum_data: int = sum(data)
            avg_data: float = sum_data / len(data)
        except Exception as e:
            print({e})
        else:
            str_data: str = (f"Processed {len(data)} numeric "
                             f"values, {sum_data}, avg={avg_data:.2f}")
            return str_data

    def validate(self, data: Any) -> bool:

        try:
            iter_data = iter(data)
            for data in iter_data:
                int(data)
        except ValueError as e:
            print(f"{e}")
            return False
        else:
            print("Validation: Numeric data verified")
            return True


class TextProcessor(DataProcessor):
    def __init__(self):
        print("Initializing Text Processor...")

    def process(self, data: Any) -> str:
        try:
            str_data: str = (f"Processed text: {len(data)} characters"
                             f", {len(data.split(' '))} words")
        except Exception as e:
            print({e})
        else:
            return str_data

    def validate(self, data: Any) -> bool:
        try:
            str(data)
        except Exception as e:
            print(f"{e}")
            return False
        else:
            print("Validation: Text data verified")
            return True


class LogProcessor(DataProcessor):
    def __init__(self):
        print("Initializing Log Processor...")

    def process(self, data: Any) -> str:
        try:
            alert_level = data.split(':')[0]
            str_data: str = (
                f"[ALERT] {alert_level} level detected: "
                "Connection timeout"
            )
        except Exception as e:
            print({e})
        else:
            return str_data

    def validate(self, data: Any) -> bool:
        try:
            data = str(data).split(":")
            if len(data) != 2:
                return False
        except Exception as e:
            print(f"{e}")
        else:
            print("Validation: Log entry verified")
            return True


def data_processor() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    try:
        numeric: NumericProcessor = NumericProcessor()
        test: list[int] = [1, 2, 3, 4, 5]
        numeric.validate(test)
        print(f"{numeric.format_output(numeric.process(test))}")
        print()
        text: TextProcessor = TextProcessor()
        text_test: str = "Hello Nexus World"
        text.validate(text_test)
        print(f"{text.format_output(text.process(text_test))}")
        print()
        log: LogProcessor = LogProcessor()
        log_test: str = "ERROR: Connection timeout"
        log.validate(log_test)
        print(f"{log.format_output(log.process(log_test))}")
    except Exception as e:
        print(f"{e}")


if __name__ == "__main__":
    data_processor()
