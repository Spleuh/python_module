from ex3.CardFactory import CardFactory, ErrFacto
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from random import randint, choice


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
        filtred = self.creatures
        if isinstance(name_or_power, str):
            filtred = self.get_sub_dict(name_or_power, filtred)
        elif isinstance(name_or_power, int):
            filtred = {
                key: value for key,
                value in self.creatures.items()
                if value['attack'] == name_or_power}
        rand_item = choice(list(filtred.items()))
        rand_key, rand_value = rand_item
        result = CreatureCard(
            rand_key,
            rand_value['cost'],
            rand_value['rarity'],
            rand_value['attack'],
            rand_value['health'])
        return result

    def create_spell(self, name_or_power=None) -> Card:
        filtred = self.spells
        if isinstance(name_or_power, int):
            raise ErrFacto(
                f"ErrFacto: spell dont have attribute power: {name_or_power}")
        elif isinstance(name_or_power, str):
            filtred = self.get_sub_dict(name_or_power, filtred)
        rand_item = choice(list(filtred.items()))
        rand_key, rand_value = rand_item
        result = SpellCard(
            rand_key,
            rand_value['cost'],
            rand_value['rarity'],
            rand_value['effect'])
        return result

    def create_artifact(self, name_or_power=None) -> Card:
        filtred = self.artifacts
        if isinstance(name_or_power, int):
            raise ErrFacto(
                "ErrFacto: artifact dont have attribute power: "
                f"{name_or_power}")
        elif isinstance(name_or_power, str):
            filtred = self.get_sub_dict(name_or_power, filtred)
        rand_item = choice(list(filtred.items()))
        rand_key, rand_value = rand_item
        result = ArtifactCard(
            rand_key,
            rand_value['cost'],
            rand_value['rarity'],
            rand_value['durability'],
            rand_value['effect'])
        return result

    def create_themed_deck(self, size):
        if size < 60:
            raise ErrFacto(
                f"ErrFacto: Deck must contain at least 60cards: {size}")
        result = {'creatures': [], 'spells': [], 'artifacts': []}
        for _ in range(size):
            type = randint(0, 2)
            if type == 0:
                card = self.create_creature()
                result['creatures'].append(card)
            elif type == 1:
                card = self.create_spell()
                result['spells'].append(card)
            else:
                card = self.create_artifact()
                result['artifacts'].append(card)
        return result

    def get_supported_types(self) -> dict:
        result = {
            'creatures': self.creatures.keys(),
            'spells': self.spells.keys(),
            'artifacts': self.artifacts.keys()}
        return result
