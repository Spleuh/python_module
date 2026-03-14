from ex3.CardFactory import CardFactory, ErrFacto
from ex0.Card import Card


class ErrFantFact(ErrFacto):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self.creatures = ['Dragon', 'Goblin']
        self.spells = ['Fire', 'Ice', 'Lightning']
        self.artifacts = ['Ring', 'Staff', 'Crystal']

    def create_creature(self, name_or_power=None) -> Card:
        pass

    def create_spell(self, name_or_power=None) -> Card:
        pass

    def create_artifact(self, name_or_power=None) -> Card:
        pass

    def get_supported_types(self) -> dict:
        pass
