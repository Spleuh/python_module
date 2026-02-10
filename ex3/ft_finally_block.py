class PlantError(Exception):
    """Plant error (custom error)"""
    pass


class Plant():
    """class plant"""
    def __init__(self, name: str = None) -> None:
        """init class plant with name str"""
        self.name: str = name


def water_plant(plant: Plant) -> None:
    """watering plant"""
    if plant.name is None:
        raise PlantError(f"Cannot water {plant.name} - invalid plant!")
    print(f"Watering {plant.name}")


def water_plants(plant_list: list[Plant]) -> None:
    """watering all plants"""
    print("Opening watering system")
    for plant in plant_list:
        water_plant(plant)


def test_watering_system() -> None:
    """test watering system"""
    plant_list: list[Plant] = [
        Plant("tomato"),
        Plant("lettuce"),
        Plant("carrots")]
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    try:
        water_plants(plant_list)
    except PlantError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")
    print("Watering completed successfully!")
    print()
    print("Testing with error...")
    error_list: list[Plant] = [
        Plant("tomato"),
        Plant()]
    try:
        water_plants(error_list)
    except PlantError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
