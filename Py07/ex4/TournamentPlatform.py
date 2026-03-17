from ex4.TournamentCard import TournamentCard
from random import randint

class ErrTourPlat(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class TournamentPlatform:
    def __init__(self):
        self.info = {
            'cards': {},
            'match_played': 0,
            'platform_status': 'active'}

    def register_card(self, card: TournamentCard) -> str:
        card_id = self.set_id(card.info['name'])
        self.info['cards'].update({card_id: card})
        return f"Card resistred with id: {card_id}"

    def set_id(self, card_name: str) -> str:
        prefix = card_name.split(' ')[-1].lower()
        last_id = max([int(number) for key in list(self.info['cards'].keys())
                       for name, number in [key.split('_')]
                       if name == prefix], default=None)
        sufix = 0
        if last_id is not None:
            sufix = last_id + 1
        return f"{prefix + '_' + str(sufix)}"

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        result = {'winner': '', 'loser': '', 'winner_rating': 0,
                  'loser_rating': 0}
        card1 = self.get_card(card1_id)
        card2 = self.get_card(card2_id)
        self.simulate_match(card1, card2)
        health_1 = card1.info['health']
        health_2 = card2.info['health']
        winner = card2
        loser = card1
        if health_1 > health_2:
            winner = card1
            loser = card2
        winner.info['stats']['win'] += 1
        loser.info['stats']['loose'] += 1
        result['winner'] = winner.info['name']
        result['loser'] = loser.info['name']
        winner.info['stats']['rank'] += 16
        result['winnner_rating'] = winner.info['stats']['rank']
        loser.info['stats']['rank'] -= 16
        result['loser_rating'] = loser.info['stats']['rank']
        return result

    def simulate_match(self, card1: TournamentCard, card2: TournamentCard):
        round = randint(0, 1)
        while card1.info['health'] > 0 and card2.info['health'] > 0:
            attacker = card2
            defender = card1
            if round % 2:
                attacker = card1
                defender = card2
            result_attack = attacker.attack(defender)
            incomming_damage = result_attack['damage']
            defender.defend(incomming_damage)

    def get_card(self, id: str) -> TournamentCard:
        result = None
        try:
            result = self.info['cards'][id]
        except KeyError:
            raise ErrTourPlat(f"ErrTourPlat: id not found: {id}")
        return result

    def get_leaderboard(self) -> list:
        lst_sorted = sorted([card for card in self.info['cards'].values()], key=lambda x: x.info['stats']['rank'], reverse=True)
        return lst_sorted

    def generate_tournament_report(self) -> dict:
        pass
