class Plant():
    """class Plant"""
    def __init__(self, name: str, height: int) -> None:
        """init plant"""
        self.height: int = height
        self.name: str = name

    def get_info(self, line: str = "\n") -> None:
        """display info plant"""
        print(f"- {self.name}: {self.height}cm", end=line)

    def get_type(self) -> str:
        """"return class name"""
        return "Plant"


class FloweringPlant(Plant):
    """sub class plant with color var"""
    def __init__(self, name: str, height: int, color: str) -> None:
        """init FloweringPlant"""
        super().__init__(name, height)
        self.color: str = color

    def get_info(self, line: str = "\n") -> None:
        """display info flowring plant"""
        super().get_info("")
        print(f", {self.color} flowers (blooming)", end=line)

    def get_type(self) -> str:
        """return class name"""
        return "FloweringPlant"


class PrizeFlower(FloweringPlant):
    """subclass FloweringPlant"""
    def __init__(self, name: str, height: int, color: str, prize: int) -> None:
        """init PrizeFlower"""
        super().__init__(name, height, color)
        self.prize: int = prize

    def get_info(self, line: str = "\n") -> None:
        """display info"""
        super().get_info("")
        print(f", Prize points = {self.prize}", end=line)

    def get_type(self) -> str:
        """return class name"""
        return "PrizeFlower"


class Garden:
    """garden class (owner, list[Plant])"""
    def __init__(self, owner: str, plants: list[Plant] = []) -> None:
        """init garden"""
        self.owner: str = owner
        self.plants: list[Plant] = plants
        self.grow: int = 0
        self.added: int = 0


class GardenManager:
    """Class GardenManager"""
    network = {}

    @staticmethod
    def __init__() -> None:
        """print msg intro"""
        print("== Garden Management System Demo ===\n")

    @classmethod
    def create_garden_network(
            cls,
            owner: str,
            plants: list[Plant] = []) -> None:
        """create key owner in dict network and init value garden"""
        cls.network[owner] = Garden(owner, plants)

    @classmethod
    def check_owner(cls, owner: str) -> int:
        """check if owner exist in network"""
        if owner in cls.network.keys():
            return 1
        else:
            return 0

    @staticmethod
    def create_plant(name: str, height: int, color: str, prize: int) -> Plant:
        """create plant ( or subclass)"""
        if color is None and prize is None:
            return Plant(name, height)
        elif prize is None:
            return FloweringPlant(name, height, color)
        else:
            return PrizeFlower(name, height, color, prize)

    @classmethod
    def get_garden(cls, owner: str) -> Garden:
        """return Garden of owner"""
        if cls.check_owner(owner) == 1:
            return cls.network[owner]

    @classmethod
    def add_plant(
            cls,
            owner: str,
            name: str,
            height: int,
            color: str = None,
            prize: int = None) -> None:
        """add plant in garden's owner"""
        garden: Garden = cls.get_garden(owner)
        plant: Plant = cls.create_plant(name, height, color, prize)
        garden.plants.append(plant)
        garden.added += 1
        print(f"Added {plant.name} to {garden.owner}'s garden")

    @classmethod
    def grow(cls, owner: str) -> None:
        """+1 cm height for all plant in garden's owner"""
        if cls.check_owner(owner) is not None:
            print(f"{owner} is helping all plants grow...")
            garden: Garden = cls.get_garden(owner)
            for plant in garden.plants:
                garden.grow += 1
                print(f"{plant.name} grew 1cm")
                plant.height += 1

    class GardenStats:
        """manage statistics"""
        @staticmethod
        def __init__(owner: str) -> None:
            """print msg intro"""
            print(f"=== {owner.capitalize()}'s Garden Report ===")

        @staticmethod
        def display_added_growth(owner: str) -> None:
            """display number plant added and cm grow"""
            garden: Garden = GardenManager.get_garden(owner)
            print("Plants added: ", end="")
            print(f"{garden.added},  Total growth: {garden.grow}cm")

        @staticmethod
        def get_info(owner: str) -> None:
            """display info all plant in garden"""
            garden: Garden = GardenManager.get_garden(owner)
            for plant in garden.plants:
                plant.get_info("\n")

        @staticmethod
        def display_type(owner: str) -> None:
            """display nb of plant type(Plant, FloweringPlant, PrizeFlower)"""
            regular: int = 0
            flowering: int = 0
            prize: int = 0
            garden: Garden = GardenManager.get_garden(owner)
            for plant in garden.plants:
                if plant.get_type() == "Plant":
                    regular += 1
                elif plant.get_type() == "FloweringPlant":
                    flowering += 1
                elif plant.get_type() == "PrizeFlower":
                    prize += 1
            print("Plant types: ", end="")
            print(f"{regular} regular, {flowering} ", end="")
            print(f"flowering, {prize} prize flowers")

        @staticmethod
        def height_validation(owner: str) -> None:
            """display msg true if all height from garden >= 0"""
            i: int = 1
            garden: Garden = GardenManager.get_garden(owner)
            for plant in garden.plants:
                if plant.height < 0:
                    i = 0
            if i == 1:
                print("Height validation test: True")
            else:
                print("Height validation test: False")

        @staticmethod
        def total_garden() -> None:
            """display total nb of garden managed"""
            i: int = 0
            for garden in GardenManager.network:
                i += 1
            print(f"Total garden managed: {i}")

        @staticmethod
        def score() -> None:
            """calc and display score of all owner"""
            print("Garden scores -", end="")
            i: int = 0
            comma: str = ","
            for garden in GardenManager.network.values():
                i += 1
            for garden in GardenManager.network.values():
                score = 0
                i -= 1
                if i == 0:
                    comma = ""
                for plant in garden.plants:
                    score += plant.height + 10
                    if plant.get_type() == "PrizeFlower":
                        score += plant.prize
                print(f" {garden.owner}: {score}", end=comma)
            print("\n", end="")


if __name__ == "__main__":
    manager: GardenManager = GardenManager()
    manager.create_garden_network("Alice")
    plants: list[Plant] = []
    plants.append(Plant("Test", 82))
    manager.create_garden_network("Bob", plants)
    manager.add_plant("Alice", "Oak Tree", 100)
    manager.add_plant("Alice", "Rose", 25, "red")
    manager.add_plant("Alice", "Sunflower", 50, "yellow", 10)
    print()
    manager.grow("Alice")
    print()
    gardenstats: GardenManager.GardenStats = GardenManager.GardenStats("Alice")
    gardenstats.display_added_growth("Alice")
    gardenstats.display_type("Alice")
    print()
    gardenstats.height_validation("Alice")
    gardenstats.score()
    gardenstats.total_garden()
