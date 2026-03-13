class Plant():
    """class plant"""
    def __init__(
            self,
            name: str = None,
            water_level: int = 0,
            sunlight_hours: int = 0):
        self.name: str = name
        self.water_level: int = water_level
        self.sunlight_hours: int = sunlight_hours


class PlantHealthError(Exception):
    """custom error plant health"""
    pass


def check_plant_health(
        plant_name: str,
        water_level: int,
        sunlight_hours: int) -> None:
    """check plant health and raise custom error"""
    if plant_name is None:
        raise PlantHealthError("Plant name cannot be empty!")
    if water_level > 10:
        raise PlantHealthError(
            f"Water level {water_level} is too high (max 10)")
    if water_level < 1:
        raise PlantHealthError(f"Water level {water_level} is too low (min 1)")
    if sunlight_hours > 12:
        raise PlantHealthError(
            f"Sunlight hours {sunlight_hours} is too high (min 12)")
    if sunlight_hours < 2:
        raise PlantHealthError(
            f"Sunlight hours {sunlight_hours} is too low (min 2)")


def test_plant_checks() -> None:
    """test plant health"""
    print("=== Garden Plant Health Checker ===\n")
    try:
        print("Testing good values...")
        check_plant_health("tomato", 5, 5)
    except PlantHealthError as e:
        print(f"Error: {e}")
    else:
        print("Plant 'tomato' is healthy!")
    print()
    try:
        print("Testing empty plant name...")
        check_plant_health(None, 5, 5)
    except PlantHealthError as e:
        print(f"Error: {e}")
        print()
    try:
        print("Testing bad water level...")
        check_plant_health("tomato", 0, 5)
    except PlantHealthError as e:
        print(f"Error: {e}")
    print()
    try:
        print("Testing bad sunlight hours...")
        check_plant_health("tomato", 5, 0)
    except PlantHealthError as e:
        print(f"Error: {e}")
    print()
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
