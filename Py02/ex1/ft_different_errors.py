from typing import TextIO


def ValueErrorTest() -> None:
    print("Testing ValueError...")
    int("abc")


def ZeroDivisionErrorTest() -> None:
    print("Testing ZeroDivisionError...")
    print(10 / 0)


def FileNotFoundErrorTest() -> None:
    print("Testing FileNotFoundError...")
    f: TextIO = open("missing.txt", "r")
    f.close("missing.txt", "r")


def KeyErrorTest() -> None:
    missing = {}
    print("Testing KeyError...")
    print(missing["missing_plant"])


def test_error_types() -> None:
    try:
        ValueErrorTest()
    except ValueError as e:
        print(f"Caught {type(e).__name__}: {e}")
    print()
    try:
        ZeroDivisionErrorTest()
    except ZeroDivisionError as e:
        print(f"Caught {type(e).__name__}: {e}")
    print()
    try:
        FileNotFoundErrorTest()
    except FileNotFoundError as e:
        print(f"Caught {type(e).__name__}: {e}")
    print()
    try:
        KeyErrorTest()
    except KeyError as e:
        print(f"Caught {type(e).__name__}: {e}")
    print()
    print("All error types tested successfully!")


if __name__ == '__main__':
    print("=== Garden Error Types Demo ===\n")
    test_error_types()
