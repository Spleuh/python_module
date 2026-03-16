from abc import ABC, abstractmethod
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from random import randint, choice


class ErrFacto(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)


class CardFactory(ABC):
    def __init__(self) -> None:
        self.creatures: dict[str, dict[str, str | int]] = {}
        self.spells = dict[str, dict[str, str | int]] = {}
        self.artifacts = dict[str, dict[str, str | int]] = {}
        # self.create = None

    def random_key(
            self,
            filtred_data: dict[str: dict[str, str | int]]) -> str:
        if len(filtred_data) == 0:
            raise ErrFacto(
                f"ErrFacto: filtred data is null: {filtred_data}")
        lst_key = [key for key in filtred_data.keys()]
        rand_key = lst_key[randint(0, len(lst_key) - 1)]
        return rand_key

    def get_sub_dict(self, key: str, data: dict) -> dict:
        try:
            value = data[key]
        except KeyError:
            raise ErrFacto(f"ErrFacto: name unknown: {key}")
        else:
            return {key: value}

    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        filtred = self.creatures
        if isinstance(name_or_power, str):
            filtred = self.get_sub_dict(name_or_power, filtred)
        elif isinstance(name_or_power, int):
            filtred = {
                key: value for key,
                value in self.creatures if value['attack'] == name_or_power}
        rand_key = self.random_key(filtred)
        rand_value = filtred[rand_key]
        result = CreatureCard(
            rand_key,
            rand_value['cost'],
            rand_value['rarity'],
            rand_value['attack'],
            rand_value['health'])
        return result

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        filtred = self.spells
        if isinstance(name_or_power, int):
            raise ErrFacto(
                f"ErrFacto: spell dont have attribute power: {name_or_power}")
        elif isinstance(name_or_power, str):
            filtred = self.get_sub_dict(name_or_power, filtred)
        rand_key = self.random_key(filtred)
        rand_value = filtred[rand_key]
        result = SpellCard(
            rand_key,
            rand_value['cost'],
            rand_value['rarity'],
            rand_value['effect_type'])
        return result

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        filtred = self.artifacts
        if isinstance(name_or_power, int):
            raise ErrFacto(
                "ErrFacto: artifact dont have attribute power: "
                f"{name_or_power}")
        elif isinstance(name_or_power, str):
            filtred = self.get_sub_dict(name_or_power, filtred)
        rand_key = self.random_key(filtred)
        rand_value = filtred[rand_key]
        result = ArtifactCard(
            rand_key,
            rand_value['cost'],
            rand_value['rarity'],
            rand_value['durability'],
            rand_value['effect'])
        return result

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
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

    @abstractmethod
    def get_supported_types(self) -> dict:
        result = {
            'creatures': self.creatures.keys(),
            'spells': self.spells.keys(),
            'artifacts': self.artifacts.keys()}
        return result
