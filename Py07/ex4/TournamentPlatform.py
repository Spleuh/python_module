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
        return f"{card_id}"

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
        if not self.simulate_match(card1, card2):
            return result
        health_1 = card1.info['health']
        health_2 = card2.info['health']
        winner = card2
        loser = card1
        if health_1 > health_2:
            winner = card1
            loser = card2
        winner.update_wins(winner.get_wins() + 1)
        loser.update_losses(loser.get_losses() + 1)
        winner.calculate_rating()
        loser.calculate_rating()
        result['winner'] = winner.info['name']
        result['loser'] = loser.info['name']
        result['winner_rating'] = winner.get_rank_info()['rank']
        result['loser_rating'] = loser.get_rank_info()['rank']
        self.info['match_played'] += 1
        return result

    def simulate_match(self,
                       card1: TournamentCard,
                       card2: TournamentCard) -> bool:
        round = randint(0, 1)
        while (card1.info['health'] > 0 and
               card2.info['health'] > 0 and
               round < 50):
            attacker = card1
            defender = card2
            if round % 2:
                attacker = card2
                defender = card1
            result_attack = attacker.attack(defender)
            incomming_damage = result_attack['damage']
            defender.defend(incomming_damage)
            round += 1
        if round == 50:
            return False
        return True

    def get_card(self, id: str) -> TournamentCard:
        result = None
        try:
            result = self.info['cards'][id]
        except KeyError:
            raise ErrTourPlat(f"ErrTourPlat: id not found: {id}")
        return result

    def get_leaderboard(self) -> list:
        lst_sorted = sorted([card for card in self.info['cards'].values()],
                            key=lambda x: x.info['stats']['rank'],
                            reverse=True)
        return lst_sorted

    def print_leaderboard(self) -> None:
        lst_sorted = self.get_leaderboard()
        for i, card in enumerate(lst_sorted):
            name = card.info['name']
            rating = card.info['stats']['rank']
            win = card.info['stats']['win']
            loose = card.info['stats']['loose']
            print(f"{i + 1}. {name} - Rating: {rating} ({win}-{loose})")

    def generate_tournament_report(self) -> dict:
        info = self.info
        lst_rating = [card.info['stats']['rank']
                      for card in info['cards'].values()]
        avg_rating = sum(lst_rating) // len(lst_rating)
        result = {'total_cards': len(info['cards']),
                  'match_played': info['match_played'],
                  'avg_rating': avg_rating,
                  'platform_status': info['platform_status']}
        return result
