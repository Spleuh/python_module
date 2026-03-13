class Plant:
    """class plant"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """init plant"""
        self.name: str = name
        self.height: int = height
        self.age: int = age


def get_info(plant: Plant) -> None:
    """display information from plant"""
    print(f"{plant.name}: {plant.height}cm, {plant.age} days old")


def grow(plant: Plant) -> None:
    """increase height +1"""
    plant.height += 1


def age(plant: Plant) -> None:
    """increase age +1"""
    plant.age += 1


if __name__ == '__main__':
    plant: Plant = Plant("Rose", 25, 30)
    i: int = 1
    print(f"=== Day {i} ===")
    get_info(plant)
    for i in range(i, 7, 1):
        grow(plant)
        age(plant)
    print(f"=== Day {i+1} ===")
    get_info(plant)
    print(f"Growth this week: +{i}cm")
