from ex3.GameStrategy import GameStrategy


class AggresiveStrategy(GameStrategy):
    def __init__(self) -> None:
        pass

    def execute_turn(self, hand, battlefield) -> dict:
        pass

    def get_strategy_name(self) -> str:
        pass

    def prioritize_targets(self, available_targets) -> list:
        pass
