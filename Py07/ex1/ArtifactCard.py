from ex0.Card import Card, ErrCard


class ErrArtifactC(ErrCard):
    def __init__(self, *args):
        super().__init__(*args)


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        if durability < 1:
            raise ErrArtifactC(f"ErrArtifactC: Durability < 1: {durability}")
        self.info['durability'] = durability
        self.info['effect'] = effect

    def play(self, game_state: dict):
        return super().play(game_state)

    def activate_ability(self) -> dict:
        tmp = self.info['effect'].split(":")
        if len(tmp) == 2:
            key, value = tmp
            return {key: value}
        raise ErrArtifactC(f"ErrArtifactC: error format effect: {self.info['effect']}")
