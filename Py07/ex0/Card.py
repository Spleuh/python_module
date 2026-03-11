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
            self.rarity = Rarity[rarity]
        except KeyError:
            raise ErrorCard(f"Error Card: Rarity unknown: {rarity}")
        self.name = name
        self.cost = cost


if __name__ == '__main__':
    try:
        Card('test', 8, 'test')
    except ErrorCard as e:
        print(f"{e}")
