from ex3.GameStrategy import GameStrategy, ErrStrategy
from ex3.GameEngine import Player
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from random import randint, choice


class ErrAggrStrategy(ErrStrategy):
    def __init__(self, msg):
        super().__init__(msg)


class AggresiveStrategy(GameStrategy):
    def __init__(self) -> None:
        pass

    def execute_turn(self, hand: list[Card],
                     battlefield: list[dict[str, Card | int]]) -> dict:
        if len(battlefield) != 2:
            raise ErrAggrStrategy(
                "ErrAggreStrategy: battlefield can "
                "contain only 2 sides self/opponent: "
                f"{battlefield}")
        creatures = [crea for crea in hand if isinstance(crea, CreatureCard)]
        spells = [spell for spell in hand if isinstance(spell, SpellCard)]
        artifacts = [arti for arti in hand if isinstance(arti, ArtifactCard)]
        ally = ""
        ennemy = ""
        for side in battlefield:
            if side.keys() == ["ally"]:
                ally = side
            else:
                ennemy = side
        if ally == "" or ennemy == "":
            raise ErrAggrStrategy(
                "ErrAggrStrategy: battlefield must have 2 sides: "
                f"{battlefield}")
        result = {'cards_played': [], 'mana_used': 0, 'targets_attacked': []}
        if len(hand) == 0:
            raise ErrAggrStrategy(
                "ErrAggreStrategy: hand cant be null at "
                f"start of turn: {hand}")
        if len(hand) == 1:
            card = hand(0)
            card.play()
            if isinstance(card, CreatureCard):
                target = choice(ennemy)
                card.attack_target(target)
                result['targets_attacked'].append(target)
                # caca
        if len(creatures) and len(spells):
            creatures(randint(0, len(creatures) - 1)).play()
            spells(randint(0, len(spells) - 1)).play()
        elif len(creatures) > 1:
            creatures(randint(0, len(creatures) - 1)).play()
            creatures(randint(0, len(creatures) - 1)).play()
        elif len(spells) > 1:
            spells(randint(0, len(spells) - 1)).play()
            spells(randint(0, len(spells) - 1)).play()
        else:
            artifacts(randint(0, len(artifacts) - 1)).play()

    def get_strategy_name(self) -> str:
        return "AggresiveStrategy"

    def prioritize_targets(self,
                           available_targets: list[CreatureCard,
                                                   ArtifactCard,
                                                   Player]) -> list:
        if available_targets is None:
            raise ErrAggrStrategy(
                "ErrAggrStrategy: available_targets cant be empty: :"
                f"{available_targets}")
        data = {'creatures': [], 'artifacts': [], 'opponent': []}
        for target in available_targets:
            if target.__class__.__name__ == "CreatureCard":
                data['creatures'].append(target)
            else:
                data['opponent'].append(target)
        if len(data['opponent']) != 1:
            raise ErrAggrStrategy(
                "ErrAggrStrategy: Can only have 1 opponnent: "
                f"{data['opponent']}")
        result = []
        if data['opponent'].health > 6:
            result.append(data['creatures'])
            result.append(data['opponent'])
            return result
        else:
            result.append(data['opponent'])
            return result
