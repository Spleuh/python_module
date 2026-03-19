from abc import ABC, abstractmethod
from enum import Enum


class Rarity(Enum):
    COMMON = "Common"
    RARE = "Rare"
    LEGENDARY = "Legendary"


class ErrCard(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        if name == '':
            raise ErrCard(f"ErrorCard: name cant be '': {name}")
        if isinstance(cost, int) and cost < 0:
            raise ErrCard(f"ErrorCard: cost cant be < 0: {cost}")
        try:
            Rarity(rarity)
        except Exception:
            raise ErrCard(f"ErrorCard: Rarity unknown: {rarity}")
        info = {'name': name, 'cost': cost, 'rarity': rarity}
        self.info = info

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        result: dict = {'card_played': self.info['name'],
                        'mana_used': self.info['cost']}
        if not self.is_playable(game_state['available_mana']):
            raise ErrCard("CardError: Not enough mana to play this card: "
                          f"available_mana:{game_state['available_mana']}, "
                          f"cost:{self.info['cost']}")
        return result

    def get_card_info(self) -> dict:
        return self.info

    def is_playable(self, available_mana: int) -> bool:
        if (isinstance(self.info['cost'], int) and
                available_mana >= self.info['cost']):
            return True
        return False
