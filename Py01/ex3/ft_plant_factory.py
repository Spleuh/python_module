class Plant:
    """class plant"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """init plant"""
        self.name: str = name
        self.height: int = height
        self.age: int = age


class Factory:
    """class factory"""
    def __init__(self) -> None:
        """init factory"""
        pass

    def PlantFactory(self, specs: list[tuple[str, int, int]]) -> list[Plant]:
        """return a list of plant initialized with data from specs"""
        plants: list[Plant] = []
        i: int = 0
        for data in specs:
            plant = Plant(data[0], data[1], data[2])
            plants.append(plant)
            i += 1
            print(f"Created: {plant.name.capitalize()} ", end="")
            print(f"({plant.height}cm, {plant.age} days)")
        print(f"\nTotal plants created: {i}")
        return plants


if __name__ == "__main__":
    plant_specs = [("rose", 25, 30), ("oak", 200, 365), ("Cactus", 5, 90),
                   ("Sunflower", 80, 45), ("Fern", 15, 120)]
    fac: Factory = Factory
    print("=== Plant Factory Output ===")
    plants: list[Plant] = fac.PlantFactory(fac, plant_specs)
