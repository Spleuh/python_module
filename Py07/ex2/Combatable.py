from ex0 import Card
from abc import abstractmethod


class Combatable(Card):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        super().__init__(name, cost, rarity)

    @abstractmethod
    def attack(self, target: Card) -> dict:
        result = {'attacker': self.info['name'], 'target': target.info['name']}
        return result

    @abstractmethod
    def defend(self, incomming_damage: int) -> dict:
        result = {'defender': self.info['name'],
                  'damage_taken': incomming_damage}
        return result
