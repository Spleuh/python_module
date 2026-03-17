from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self.info['cards': {}, 'match_played': 0, 'platform_status': 'active']

    def register_card(self, card: TournamentCard) -> str:
        pass

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        pass

    def get_leaderboard(self) -> list:
        pass

    def generate_tournament_report(self) -> dict:
        pass
