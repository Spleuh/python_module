from ex0.Card import Card


class Player(Card):
    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 20
