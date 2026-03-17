from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
from ex0.Card import Card


class ErrTourCard(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 attack: int,
                 health: int,
                 defense: int,
                 rating: int):
        super().__init__(name, cost, rarity)
        info = {'health': health, 'combat':
                {'attack': attack, 'defense': defense, 'combat_type': 'melee'}}
        info.update({'stats': {'win': 0, 'loose': 0, 'rank': rating}})
        self.info.update(info)

    def play(self, game_state: dict) -> dict:
        return super().play(game_state)

    def attack(self, target: Card) -> dict:
        if not isinstance(target, Card):
            raise ErrTourCard("ErrTourCard: target is not a card: "
                              f"{target.info}")
        result = super().attack(target)
        combat_dict = self.info['combat']
        result.update({'damage': combat_dict['attack'],
                       'combat_type': combat_dict['combat_type']})
        target.info['health'] -= result['damage']
        return result

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
