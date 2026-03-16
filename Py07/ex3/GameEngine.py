from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from ex1.Deck import Deck


class ErrPlayer(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)


class GameEngine():
    def __init__(self) -> None:
        pass

    def configure_engine(
            self,
            factory: CardFactory,
            strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        self.strategy.execute_turn()

    def get_engine_status(self) -> dict:
        pass


class Player():
    def __init__(self, name: str, game_engine: GameEngine) -> None:
        self.name = name
        self.health = 20
        self.game_engine = game_engine
        self.hand = []

    def setup_deck(self, size: int = 60):
        try:
            data_cards = self.game_engine.factory.create_themed_deck(size)
            lst_cards = []
            for i in data_cards.values():
                lst_cards += i
            self.deck = Deck(lst_cards)
            self.deck.shuffle()
        except Exception as e:
            print(f"{e}")

    def draw(self, quantity: int = 1):
        if quantity < 1:
            raise ErrPlayer("ErrPlayer: quantity cards draw "
                            f"cant be < 1: {quantity}")
        for i in range(quantity):
            self.hand.append(self.deck.draw_card())
