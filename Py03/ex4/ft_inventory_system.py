import sys


class PlayerError(Exception):
    """custom error player"""

    def __init__(self, message: str,
                 prefix: str = "PlayerError: "):
        super().__init__(f"{prefix}{message}")


class InventoryError(PlayerError):
    """custom error inventory"""

    def __init__(self, message: str,
                 prefix: str = "InventoryError: "):
        super().__init__(message, prefix)


class ItemError(InventoryError):
    """custom error item"""

    def __init__(
            self,
            message: str,
            prefix: str = "ItemError: "):
        super().__init__(message, prefix)


def str_unit(quantity: int) -> str:
    """return str unit or units"""
    if quantity == 1:
        return "unit"
    elif quantity > 1:
        return "units"
    else:
        raise ItemError("Quantity is negative")


class InventoryManager:
    """manage inventory"""

    def __init__(self, data: dict[str, dict[str, int]] = {}) -> None:
        """init InventoryManager with default data {}"""
        self.data = data

    def add_inventory(self,
                      player: str,
                      inventory: dict[str,
                                      int] = {}) -> None:
        """add dict inventory for player (str)"""
        self.data[player] = inventory

    def system_analysis(self) -> None:
        """display demo inventory system analysis"""
        print("=== Inventory System Analysis ===")
        print(f"Total items in inventory: {len(manager.data['alice'])}")

    def inv_sys_analysis(self) -> None:
        """display demo sys analysis"""
        print("=== Inventory System Analysis ===")
        for player in self.data:
            print(
                f"Total items in {player.capitalize()}'s inventory: "
                f"{self.calc_total_items(player)}")
            print(
                f"Unique item types: {len(set(self.data[player].keys()))}\n")

    def current_inventory(self, name: str) -> None:
        """display inventory of all player"""
        print(f"=== Current {name.capitalize()}'s inventory ===")
        try:
            total: int = self.calc_total_items(name)
            sort_inv: dict[str, int] = dict(
                sorted(self.data[name].items(),
                       key=lambda x: x[1], reverse=True))
            for item in sort_inv:
                quantity: int = sort_inv[item]
                print(
                    f"{item}: {quantity} {str_unit(quantity)} "
                    f"({quantity / total * 100:.1f}%)")
            print()
        except ItemError as e:
            print(f"{e}")

    def get_min_max(self, name: str, flag: int = -1) -> tuple[str, int]:
        """return most or least abundant item"""
        if name in self.data.keys():
            sort_inv: list[tuple[str, int]] = sorted(
                self.data[name].items(), key=lambda x: x[1])
            if flag < 0:
                return sort_inv[0]
            else:
                return sort_inv[len(sort_inv) - 1]
        else:
            raise PlayerError("Player name unknown")

    def inv_stats(self, name: str) -> None:
        """demo inventory statistics"""
        print(f"=== {name.capitalize()}'s Inventory Statistics ===")
        if self.data[name] is not None:
            try:
                min: tuple[str, int] = self.get_min_max(name, -1)
                max: tuple[str, int] = self.get_min_max(name, 1)
            except PlayerError as e:
                print(f"{e}")
            else:
                print(f"Most abundant: {max[0]} ({max[1]} {str_unit(max[1])})")
                print(f"Least abundant: {min[0]} "
                      f"({min[1]} {str_unit(min[1])})")
                print()
        else:
            raise InventoryError("Inventory is empty")

    def get_items_cat(self, name: str, flag: int) -> dict[str, int]:
        items: dict[str, int] = {}
        min: int = 1
        if flag < 0:
            min = -1
            flag *= -1
        if min < 0:
            for item in self.data[name].items():
                if item[1] < flag:
                    items.update({item[0]: item[1]})
        else:
            for item in self.data[name].items():
                if item[1] >= flag:
                    items.update({item[0]: item[1]})
        return items

    def item_categories(self, name: str) -> None:
        print(f"{name.capitalize()}'s inventory: ")
        moderate: dict[str, int] = self.get_items_cat(name, 5)
        scarce: dict[str, int] = self.get_items_cat(name, -5)
        print(f"Moderate: {moderate}")
        print(f"Scarce: {scarce}\n")

    def item_cat_all(self) -> None:
        for name in self.data:
            self.item_categories(name)

    def inv_stats_all(self) -> None:
        try:
            for name in self.data:
                self.inv_stats(name)
        except ItemError as e:
            print(f"{e}")

    def current_inv_all(self) -> None:
        for name in self.data:
            self.current_inventory(name)

    def calc_total_items(self, name: str) -> int:
        if name in self.data.keys():
            total: int = 0
            for item in self.data[name]:
                total += self.data[name][item]
            return total
        else:
            raise PlayerError("Player's name unknown")

    def demo(self) -> None:
        print("=== Dictionary Properties Demo ===")
        for name in self.data.items():
            print(f"Player {name[0].capitalize()}")
            print(f"Dictionary keys: {list(name[1].keys())}")
            print(f"Dictionary values: {list(name[1].values())}")
            print("Sample lookup - 'sword' in inventory: ", end="")
            if "sword" in name[1].keys():
                print("True\n")
            else:
                print("False\n")


def parse_item(item: str) -> list[str]:
    lst_item: list[str] = item.split(":")
    if len(lst_item) != 2:
        raise ItemError("Invalid arg (item:nb)")
    try:
        test: int = int(lst_item[1])
    except ValueError as e:
        print(f"{e}")
    else:
        if test < 1:
            raise ItemError("quantity is nul or negative")
    return lst_item


def parse_all() -> InventoryManager:
    manager: InventoryManager = InventoryManager()
    if len(sys.argv) == 1:
        raise ItemError("No arg provided")
    else:
        inventory: dict[str, int] = {}
        for item in sys.argv[1:]:
            lst_item: list[str] = parse_item(item)
            if len(lst_item[0]) == 0:
                raise ItemError("Item's name cant be null")
            inventory.update({lst_item[0]: int(lst_item[1])})
        manager.data.update({"alice": inventory})
    return manager


if __name__ == "__main__":
    try:
        manager: InventoryManager = parse_all()
    except (ValueError, ItemError) as e:
        print(f"Caught {e}")
    else:
        manager.inv_sys_analysis()
        manager.current_inv_all()
        manager.inv_stats_all()
        manager.item_cat_all()
        manager.demo()
