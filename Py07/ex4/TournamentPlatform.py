from ex4.TournamentCard import TournamentCard


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
                       for name, number in [tuple(key.split('_'))]
                       if name == prefix], default=None)
        sufix = 0
        if last_id is not None:
            sufix = last_id + 1
        return f"{prefix + '_' + str(sufix)}"

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        pass

    def get_leaderboard(self) -> list:
        pass

    def generate_tournament_report(self) -> dict:
        pass
