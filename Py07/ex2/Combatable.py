from ex0 import Card
from abc import ABC, abstractmethod


class Combatable(ABC):
    @abstractmethod
    def attack(self, target: Card) -> dict:
        result = {'attacker': self.info['name'], 'target': target.info['name']}
        return result

    @abstractmethod
    def defend(self, incomming_damage: int) -> dict:
        result = {'defender': self.info['name'],
                  'damage_taken': incomming_damage}
        return result

    @abstractmethod
    def get_combat_stats(self) -> dict:
        pass
