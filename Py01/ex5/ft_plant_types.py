class Plant:
    """Represent a generic plant.

    Attributes:
        name (str): Plant name.
        height (int): Height in centimeters.
        age (int): Age in days.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """init plant"""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self, line: str = "\n") -> None:
        """Print the plant information on a single line.

        Args:
            line (str): line terminator (default '\\n').
        """
        print(f"{self.name.capitalize()}", end="")
        print(f"({self.__class__.__name__}): ", end="")
        print(f"{self.height}cm, {self.age} days", end=line)


class Flower(Plant):
    """Represent a flower, specialization of Plant.

    Attributes:
        color (str): Flower color.
        bloom (int): Bloom state counter (internal use).
    """

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize a Flower instance.

        Args:
            name (str): flower name.
            height (int): height in centimeters.
            age (int): age in days.
            color (str): flower color.
        """
        super().__init__(name, height, age)
        self.color: str = color
        self.bloom: int = 0

    def bloo(self) -> None:
        """Simulate blooming by printing a message."""
        print(f"{self.name.capitalize()} is blooming beautifully!")

    def get_info(self, line: str = "\n") -> None:
        """get info about flower"""
        super().get_info("")
        print(f", {self.color.lower()} color", end=line)


class Tree(Plant):
    """Represent a tree, specialization of Plant.

    Attributes:
        trunk_diam (int): Trunk diameter in centimeters.
    """

    def __init__(self, name: str, height: int, age: int, diam: int) -> None:
        """Initialize a Tree instance.

        Args:
            name (str): tree name.
            height (int): height in centimeters.
            age (int): age in days.
            diam (int): trunk diameter in centimeters.
        """
        super().__init__(name, height, age)
        self.trunk_diam: int = diam

    def get_info(self, line: str = "\n") -> None:
        """Print tree information (includes trunk diameter).

        Args:
            line (str): line terminator (default '\\n').
        """
        super().get_info("")
        print(f", {self.trunk_diam}cm diameter", end=line)

    def produce_shade(self) -> None:
        """Print a placeholder message about shade area provided by the tree"""
        print(f"{self.name.capitalize()} provides 78 square meters of shade")


class Vegetable(Plant):
    """Represent a vegetable, specialization of Plant.

    Attributes:
        harvest_season (str): Harvest season.
        nutritional_value (int): Nutritional value (e.g. vitamin content).
    """

    def __init__(
            self, name: str, height: int, age: int, harvest: str, nutri: int
    ) -> None:
        """Initialize a Vegetable instance.

        Args:
            name (str): vegetable name.
            height (int): height in centimeters.
            age (int): age in days.
            harvest (str): harvest season.
            nutri (int): nutritional value (integer).
        """
        super().__init__(name, height, age)
        self.harvest_season: str = harvest
        self.nutritional_value: int = nutri

    def get_info(self, line: str = "\n") -> None:
        """Print vegetable info and indicate if it's rich in vitamin C."""
        super().get_info("")
        print(f", {self.harvest_season} harvest", end=line)
        if self.nutritional_value > 0:
            print(f"{self.name.capitalize()} is rich in vitamin C")


if __name__ == '__main__':

    print("=== Garden Plant Types ===")
    print()
    rose: Flower = Flower("rose", 2, 3, "Red")
    lily: Flower = Flower("lily", 3, 3, "white")
    rose.get_info()
    rose.bloo()
    print()
    tree: Tree = Tree("Oak", 500, 1825, 50)
    fir: Tree = Tree("fir", 500, 1825, 50)
    tree.get_info()
    tree.produce_shade()
    print()
    tomato: Vegetable = Vegetable("tomato", 80, 90, "summer", 15)
    carrot: Vegetable = Vegetable("carrot", 80, 90, "summer", 15)
    tomato.get_info()
