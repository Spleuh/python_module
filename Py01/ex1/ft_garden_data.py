class Plant:
    """class plant"""
    def __init__(self, name: str, height: int, age: int):
        """init plant"""
        self.name: str = name
        self.height: int = height
        self.age: int = age


if __name__ == '__main__':
    print("=== Garden Plant Registry ===")
    p1: Plant = Plant("Rose", 25, 30)
    p2: Plant = Plant("Sunflower", 80, 45)
    p3: Plant = Plant("Cactus", 15, 120)
    garden: list[Plant] = [p1, p2, p3]
    for n in garden:
        print(f"{n.name}: {n.height}cm, {n.age} days old")
