from ex3.CardFactory import CardFactory, ErrFacto
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from random import choice
from typing import Callable


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
        self.create = {
            'creatures': self.create_creature,
            'spells': self.create_spell,
            'artifacts': self.create_artifact
        }

    def get_available_type(self) -> None:
        result = {'creatures': [], 'spells': [], 'artifacts': []}
        result['creatures'] = [key.lower() for key in self.creatures.keys()]
        result['spells'] = [key for key in self.spells.keys()]
        result['artifacts'] = [key for key in self.artifacts.keys()]
        return result

    def create_creature(self, name_or_power: str | int = None) -> Card:
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

    def create_spell(self, name_or_power: str | int = None) -> Card:
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

    def create_artifact(self, name_or_power: str | int = None) -> Card:
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

    def create_themed_deck(self, size: int) -> dict:
        if size < 60:
            raise ErrFacto(
                f"ErrFacto: Deck must contain at least 60cards: {size}")
        result = {'creatures': [], 'spells': [], 'artifacts': []}
        for _ in range(size):
            rand_type = choice(list(result.keys()))
            f = self.create.get(rand_type)
            if f is None:
                raise ErrFacto("ErrFacto: create methods "
                               f"doesnt exist: {rand_type}")
            card = self.create_card(f)
            if card:
                result[rand_type].append(card)
        return result

    def create_card(self, func: Callable[[], Card]) -> None | Card:
        try:
            result = func()
        except Exception as e:
            print(f"Error during creation card: {e}")
            result = None
        return result

    def get_supported_types(self) -> dict:
        result = {
            'creatures': self.creatures.keys(),
            'spells': self.spells.keys(),
            'artifacts': self.artifacts.keys()}
        return result
