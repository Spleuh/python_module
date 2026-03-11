from abc import ABC
from enum import Enum


class Rarity(Enum):
    COMMON = "Common"
    RARE = "Rare"
    LEGENDARY = "Legendary"


class ErrorCard(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str):
        if name == '':
            raise ErrorCard(f"Error Card: name cant be '': {name}")
        if cost < 0:
            raise ErrorCard(f"Error Card: cost cant be < 0: {cost}")
        try:
            self.rarity = Rarity(rarity)
        except Exception:
            raise ErrorCard(f"Error Card: Rarity unknown: {rarity}")
        self.name = name
        self.cost = cost

    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        info = {}
        info.update({"name": self.name, "cost": self.cost,
                    "rarity": self.rarity.value})
        return info


if __name__ == '__main__':
    test = None
    try:
        test = Card('test', 8, 'Legendary')
    except ErrorCard as e:
        print(f"{e}")
    print(test.get_card_info())
