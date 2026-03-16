from ex3.CardFactory import CardFactory, ErrFacto
from ex0.Card import Card
# from ex0.CreatureCard import CreatureCard


class ErrFantFact(ErrFacto):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self.creatures = {
            'Dragon': {
                'cost': 4,
                'rarity': 'Rare',
                'attack': 5,
                'health': 3},
            'Goblin': {
                'cost': 1,
                'rarity': 'Common',
                'attack': 2,
                'health': 1}}
        self.spells = {
            'fireball': {
                'cost': 4,
                'rarity': 'Rare',
                'effect': 'Deal 4 dammage to target'}}
        self.artifacts = {
            'mana_ring': {
                'cost': 1,
                'rarity': 'Legendary',
                'durability': 6,
                'effect': 'Permanent: +1 mana per turn'}}

    def create_creature(self, name_or_power=None) -> Card:
        result = super().create_creature(name_or_power)
        return result

    def create_spell(self, name_or_power=None) -> Card:
        result = super().create_spell(name_or_power)
        return result

    def create_artifact(self, name_or_power=None) -> Card:
        result = super().create_artifact(name_or_power)
        return result

    def create_themed_deck(self, size):
        result = super().create_themed_deck(size)
        return result

    def get_supported_types(self) -> dict:
        result = super().get_supported_types()
        return result
