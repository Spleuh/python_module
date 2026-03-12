from random import randint
from ex0.Card import Card


class ErrDeck(Exception):
    def __init__(self, *args) -> None:
        super().__init__(*args)


class Deck:
    def __init__(self, lst_card: list[Card] = []) -> None:
        self.lst_card = lst_card

    def add_card(self, card: Card) -> None:
        self.lst_card.append(card)

    def remove_card(self, card: str) -> bool:
        try:
            self.lst_card.remove(self.get_card(card))
            return True
        except Exception:
            return False

    def get_card(self, name: str) -> Card:
        for c in self.lst_card:
            if c.info['name'] == name:
                result = c
                return result
        raise ErrDeck(f"ErrDeck: Card not found: {name}")

    def shuffle(self) -> None:
        shuffled = []
        while len(self.lst_card):
            i = randint(0, len(self.lst_card) - 1)
            shuffled.append(self.lst_card[i])
            self.lst_card.pop(i)
        self.lst_card = shuffled

    def draw_card(self) -> Card:
        if len(self.lst_card) == 0:
            raise ErrDeck(f"ErrDeck: Deck is empty: {self.lst_card}")
        card = self.lst_card[len(self.lst_card) - 1]
        self.lst_card.pop()
        return card

    def count_by_type(self, type: str) -> int:
        i = 0
        for c in self.lst_card:
            if c.info['type'] == type:
                i += 1
        return i

    def avg_cost(self) -> float:
        total = 0
        if len(self.lst_card) == 0:
            return 0
        for c in self.lst_card:
            total += c.info['cost']
        result = total / len(self.lst_card)
        return result

    def get_deck_stats(self) -> dict:
        total_card = len(self.lst_card)
        creatures = self.count_by_type('creature')
        spells = self.count_by_type('spell')
        artifacts = self.count_by_type('artifact')
        avg = f"{self.avg_cost():.2f}"
        result = {'total_card': total_card, 'spells': spells,
                  'creatures': creatures, 'artifacts': artifacts,
                  'avg_cost': avg}
        return result
