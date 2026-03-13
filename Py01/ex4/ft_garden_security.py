class SecurePlant:
    """class SecurePlant"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """validates data before storing it, ensuring data integrity"""
        self.set_height(height, 0)
        self.set_age(age, 0)
        self.name: str = name
        print(f"Plant created: {name.capitalize()}")

    def set_height(self, height: int, p: int = 1) -> None:
        """Modify height of a Plant with restriction. Height cant be < 0"""
        if height > -1:
            self.__height: int = height
            if p == 1:
                print(f"Height updated: {height}cm [OK]")
        else:
            if p == 1:
                print("Invalid operation attempted:", end="")
                print(f" height {height}cm [REJECTED]")
                print("Security: Negative height rejected")

    def set_age(self, age: int, p: int = 1) -> None:
        """Modify age of a Plant. Raise error if age < 0"""
        if age < 0:
            if p == 1:
                print(f"Invalid operation attempted: age {age}days [REJECTED]")
                print("Security: Negative age rejected")
        else:
            if p == 1:
                print(f"Age updated: {age} days [OK]")
            self.__age: int = age

    def get_info(self) -> None:
        print(f"Current plant: {self.name.capitalize()} ", end="")
        print(f"({self.__height}cm, {self.__age} days)")

    def get_height(self) -> int:
        """return height"""
        return self.__height

    def get_age(self) -> int:
        """return age"""
        return self.__age


if __name__ == "__main__":
    print("=== Garden Security ===")
    rose: SecurePlant = SecurePlant("rose", 2,  3)
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    print()
    rose.get_info()
