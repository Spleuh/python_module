from ex0.Card import Card, ErrCard


class ErrArtifactC(ErrCard):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        if durability < 1:
            raise ErrArtifactC(f"ErrArtifactC: Durability < 1: {durability}")
        self.info.update({'type': 'artifact', 'durability': durability,
                          'effect': effect})

    def play(self, game_state: dict) -> None:
        result = super().play(game_state)
        result.update({'effect': self.info['effect']})
        return result

    def activate_ability(self) -> dict:
        tmp = self.info['effect'].split(":")
        if len(tmp) == 2:
            key, value = tmp
            return {key: value}
        raise ErrArtifactC("ErrArtifactC: error format effect: "
                           f"{self.info['effect']}")
