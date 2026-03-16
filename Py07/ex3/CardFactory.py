from abc import ABC, abstractmethod
from ex0.Card import Card


class ErrFacto(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)


class CardFactory(ABC):
    def __init__(self) -> None:
        self.creatures: dict[str, dict[str, str | int]] = {}
        self.spells = dict[str, dict[str, str | int]] = {}
        self.artifacts = dict[str, dict[str, str | int]] = {}

    def get_sub_dict(self, key: str, data: dict) -> dict:
        try:
            value = data[key]
        except KeyError:
            raise ErrFacto(f"ErrFacto: name unknown: {key}")
        else:
            return {key: value}

    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        pass

    @abstractmethod
    def get_supported_types(self) -> dict:
        pass
