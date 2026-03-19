from abc import ABC, abstractmethod


class ErrStrategy(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)


class GameStrategy(ABC):
    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        pass
