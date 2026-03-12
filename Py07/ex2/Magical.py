from ex0.Card import Card
from abc import abstractmethod


class Magical(Card):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        super().__init__(name, cost, rarity)
    
    @abstractmethod
    def cast_spell()