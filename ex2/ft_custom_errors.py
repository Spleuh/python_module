class Plant():
    """class plant"""
    def __init__(self, name: str, wilting: int) -> None:
        """init class Plant"""
        self.name: str = name
        self.wilting: int = wilting


class Garden():
    """class garden owner, list plant and level of water in tank"""
    def __init__(self, owner: str, plants: list[Plant], tank: int) -> None:
        """init garden"""
        self.owner: str = owner
        self.plants: list[Plant] = plants
        self.tank: int = tank


class GardenError(Exception):
    """GardenError : basic error for garden problems"""
    pass


class PlantError(GardenError):
    """class error custom for wilting plant"""
    pass


class WaterError(GardenError):
    """class error water error"""
    pass


def PlantErrorTest(garden: Garden) -> None:
    """Plant error test"""
    for plant in garden.plants:
        if plant.wilting == 1:
            raise PlantError(f"The {plant.name} plant is wilting!")


def WaterErrorTest(garden: Garden) -> None:
    """water error test"""
    if garden.tank == 0:
        raise WaterError("Not enough water in the tank!")


def GardenErrorTest(garden: Garden) -> None:
    """garden error test all custom error"""
    print("=== Custom Garden Errors Demo ===\n")
    try:
        print("Testing PlantError...")
        PlantErrorTest(garden)
    except PlantError as e:
        print(f"Caught PlantError: {e}", end="\n\n")
    try:
        print("Testing WaterError...")
        WaterErrorTest(garden)
    except WaterError as e:
        print(f"Caught WaterError: {e}", end="\n\n")
    try:
        print("Testing catching all garden errors...")
        PlantErrorTest(garden)
    except GardenError as e:
        print(f"Caught garden error: {e}", end="\n")
    try:
        WaterErrorTest(garden)
    except GardenError as e:
        print(f"Caught garden error: {e}", end="\n\n")
    print("All custom error types work correctly!")


if __name__ == "__main__":
    plants: list[Plant] = []
    plants.append(Plant("rose", 0))
    plants.append(Plant("tomato", 1))
    garden: Garden = Garden("Bob", plants, 0)
    GardenErrorTest(garden)
