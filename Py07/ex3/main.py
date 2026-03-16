from ex3.GameEngine import GameEngine, Player
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggresiveStrategy


def main() -> None:
    engine1 = GameEngine()
    engine2 = GameEngine()
    engine1.configure_engine(FantasyCardFactory(), AggresiveStrategy())
    engine2.configure_engine(FantasyCardFactory(), AggresiveStrategy())
    player1 = Player('jsam', engine1)
    player2 = Player('ennemy', engine2)
    battle_field = [{player1.name: player1.health}, {player2.name: player2.health}]
    player1.setup_deck()
    player1.draw(7)
    for c in player1.hand:
        print(c.info['name'])


if __name__ == '__main__':
    main()
