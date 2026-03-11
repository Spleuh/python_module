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
        if not Rarity[rarity]:
            raise ErrorCard(f"Error Card: Rarity unknown")