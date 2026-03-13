def check_temperature(temp_str: str) -> int:
    """convert and check temperature"""
    temp_int: int = int(temp_str)
    return temp_int


def test_temperature_input() -> None:
    """function test input"""
    i: int = 0
    while i < 4:
        try:
            temp_str: str = input("Testing temperature: ")
            tmp_int: int = check_temperature(temp_str)
        except ValueError:
            print(f"Error: '{temp_str}' is not a valid number\n")
        else:
            if tmp_int < 0:
                print(f"Error: {tmp_int}°C is too cold for plants (min 0°C)\n")
            elif tmp_int > 40:
                print(f"Error: {tmp_int}°C is too hot for plants (max 40°C)\n")
            else:
                print(f"Temperature {tmp_int}°C is perfect for plants!\n")
        finally:
            i += 1


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature_input()
