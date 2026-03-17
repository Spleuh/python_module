from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from ex1.Deck import Deck
from ex0.Card import Card


class ErrGameEngine(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)


class GameEngine():
    def __init__(self, player_name: str, opponent: str) -> None:
        self.player_name = player_name
        self.opponent = opponent
        self.hand = []
        self.report = {'turns_simulated': 0,
                       'strategy_used': '',
                       'total_damage': 0, 'card_created': 0}
        self.battle_field = [[Player(player_name)], [Player(opponent)],
                             {'available_mana': 10}]

    def get_hand(self) -> list[str]:
        result = []
        for card in self.hand:
            item = f"{card.info['name']} ({card.info['cost']})"
            result.append(item)
        return result

    def configure_engine(
            self,
            factory: CardFactory,
            strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        self.report['strategy_used'] = self.strategy.get_strategy_name()

    def simulate_turn(self) -> dict:
        result = self.strategy.execute_turn(self.hand, self.battle_field)
        self.report['turns_simulated'] += 1
        self.report['total_damage'] += result['total_damage']
        return result

    def get_engine_status(self) -> dict:
        return self.report

    def setup_deck(self, size: int = 60) -> None:
        data_cards = self.factory.create_themed_deck(size)
        lst_cards = [card for cards in data_cards.values() for card in cards]
        deck = Deck(lst_cards)
        deck.shuffle()
        self.report['card_created'] += len(deck.lst_card)
        self.deck = deck

    def setup_ennemy_board(self, size: int = 3) -> None:
        if size < 0:
            raise ErrGameEngine("ErrGameEgine: size "
                                f"ennemy board cant be < 0: {size}")
        for i in range(size):
            self.battle_field[1].append(self.factory.create_creature())

    def draw(self, quantity: int = 1):
        if quantity < 1:
            raise ErrGameEngine("ErrGameEngine: quantity cards draw "
                                f"cant be < 1: {quantity}")
        for i in range(quantity):
            self.hand.append(self.deck.draw_card())


class Player(Card):
    def __init__(self, name: str) -> None:
        self.info = {'name': name, 'health': 20}

    def play(self):
        pass
