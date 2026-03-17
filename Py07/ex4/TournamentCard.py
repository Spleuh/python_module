from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
from ex0.Card import Card


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 attack: int,
                 health: int,
                 defense: int):
        super().__init__(name, cost, rarity)
        self.info.update({'health': health, 'combat':
                          {'attack': attack, 'defense': defense}})
        self.info.update({'stats': {'win': 0, 'loose': 0, 'rank': None}})

    def play(self, game_state: dict) -> dict:
        return super().play(game_state)

    def attack(self, target: Card) -> dict:
        return super().attack(target)

    def defend(self, incomming_damage: int) -> dict:
        return super().defend(incomming_damage)

    def get_combat_stats(self) -> dict:
        return self.info['combat']

    def calculate_rating(self) -> int:
        pass

    def update_wins(self, wins: int) -> None:
        pass

    def update_losses(self, losses: int) -> None:
        pass

    def get_rank_info(self) -> dict:
        pass
