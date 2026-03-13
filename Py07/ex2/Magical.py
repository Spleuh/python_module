from ex0.Card import Card
from abc import ABC, abstractmethod


class Magical(ABC):
    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        result = {'caster': self.info['name'],
                  'spell': spell_name, 'targets': targets}
        return result

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        result = {'channeled': amount}
        return result

    @abstractmethod
    def get_magic_stats(self) -> dict:
        pass
