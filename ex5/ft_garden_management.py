class GardenError(Exception):
    """Custom error"""
    pass


class PlantError(GardenError):
    """custom error"""
    pass


class PlantHealthError(PlantError):
    """custom error"""
    pass


class WaterTrunkError(GardenError):
    """custom error"""
    pass


class WaterPlantError(PlantError):
    """custom error"""
    pass


class Plant:
    """class plant"""
    def __init__(
            self,
            name: str = None,
            sunlight: int = 0,
            water_level: int = 0) -> None:
        """init class plant name sunlighthours water level"""
        self.name: str = name
        self.sunlight: int = sunlight
        self.water_level: int = water_level


class Garden:
    """garden class"""
    def __init__(
            self,
            owner: str,
            plants: list[Plant],
            water_trunk: int) -> None:
        """init garden owner list plant water trunk level"""
        self.owner: str = owner
        self.plants: list[Plant] = plants
        self.water_trunk: int = water_trunk


class GardenManager:
    """class garden manager"""
    def __init__(self, garden: Garden) -> None:
        """init garden manager"""
        self.garden: Garden = garden

    def test_name(self, plant: Plant) -> None:
        """check if name is None and raise error"""
        if plant.name is None:
            raise PlantError("Plant name cannot be empty!")

    def add_plants(self, plants: list[Plant]) -> None:
        """add plant to garden"""
        for plant in plants:
            self.test_name(plant)
            self.garden.plants.append(plant)
            print(f"Added {plant.name} successfully")

    def water_plant(self) -> None:
        """water all plant from garden"""
        print("Opening watering system")
        try:
            for plant in self.garden.plants:
                self.check_trunk_level()
                print(f"Watering {plant.name} - success")
                plant.water_level += 1
                self.garden.water_trunk -= 1
        except GardenError as e:
            print(f"Caught GardenError: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant: Plant) -> str:
        """check plant health"""
        if plant.water_level > 10:
            raise PlantHealthError(
                f"{plant.name}: "
                f"Water level {plant.water_level} is too high (max 10)")
        if plant.water_level < 1:
            raise PlantHealthError(
                f"{plant.name}: Water level"
                f"{plant.water_level} is too low (min 1)")
        if plant.sunlight > 12:
            raise PlantHealthError(
                f"{plant.name}: Sunlight hours"
                f"{plant.sunlight} is too high (min 12)")
        if plant.sunlight < 2:
            raise PlantHealthError(
                f"{plant.name}: "
                f"Sunlight hours {plant.sunlight} is too low (min 2)")

    def check_plants_health(self) -> None:
        """check plants health"""
        try:
            for plant in self.garden.plants:
                self.check_plant_health(plant)
                print(
                    f"{plant.name}: healthy (water: {plant.water_level},"
                    f" sun: {plant.sunlight})")
        except PlantError as e:
            print(f"Error checking {e}")

    def check_trunk_level(self) -> None:
        """check water level of garden and raise error"""
        if self.garden.water_trunk < 1:
            raise WaterTrunkError("Not enough water in tank")


def test_garden_management() -> None:
    """test custom error garden management"""
    print("=== Garden Management System ===", end="\n\n")
    plants: list[Plant] = []
    garden: Garden = Garden("Bob", [], 2)
    garden_manager: GardenManager = GardenManager(garden)
    plants.append(Plant("tomato", 8, 4))
    plants.append(Plant("lettuce", 7, 14))
    plants.append(Plant())
    try:
        print("Adding plants to garden...")
        garden_manager.add_plants(plants)
    except PlantError as e:
        print(f"Error adding plant: {e}", end="\n\n")
    try:
        print("Watering plants...")
        garden_manager.water_plant()
    except WaterTrunkError as e:
        print(f"Error garden: {e}")
    finally:
        print()
    try:
        print("Checking plant health...")
        garden_manager.check_plants_health()
    except PlantHealthError as e:
        print(f"Error checking {e}")
    finally:
        print()
    try:
        print("Testing error recovery...")
        garden_manager.check_trunk_level()
    except GardenError as e:
        print(f"Caught GardenError: {e}", )
    finally:
        print("System recovered and continuing...", end="\n\n")
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
