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
                 rank: int):
        super().__init__(name, cost, rarity)
        info = {'health': health, 'combat':
                {'attack': attack, 'defense': defense, 'combat_type': 'melee'}}
        info.update({'stats': {'win': 0, 'loose': 0, 'rank': rank}})
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
        return result

    def defend(self, incomming_damage: int) -> dict:
        result = super().defend(incomming_damage)
        combat_dict = self.info['combat']
        dmg_taken = combat_dict['defense'] - incomming_damage
        if dmg_taken >= 0:
            dmg_blocked = incomming_damage
            dmg_taken = 0
        else:
            dmg_blocked = combat_dict['defense']
            dmg_taken *= -1
        self.info['health'] -= dmg_taken
        alive = True
        if self.info['health'] <= 0:
            alive = False
        result.update({'damage_taken': dmg_taken,
                       'damage_blocked': dmg_blocked,
                       'still_alive': alive})
        return result

    def get_combat_stats(self) -> dict:
        return self.info['combat']

    def calculate_rating(self) -> int:
        self.info['stats']['rank'] += (
            16 * self.info['stats']['win']
            - 16 * self.info['stats']['loose'])
        return self.info['stats']['rank']

    def update_wins(self, wins: int) -> None:
        if wins > -1:
            self.info['stats']['win'] = wins

    def get_wins(self) -> int:
        return self.info['stats']['win']

    def update_losses(self, losses: int) -> None:
        if losses > -1:
            self.info['stats']['loose'] = losses

    def get_losses(self) -> int:
        return self.info['stats']['loose']

    def get_rank_info(self) -> dict:
        return self.info['stats']
