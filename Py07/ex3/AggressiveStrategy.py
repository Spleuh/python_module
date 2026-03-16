from ex3.GameStrategy import GameStrategy, ErrStrategy
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from random import randint, choice


class ErrAggrStrategy(ErrStrategy):
    def __init__(self, msg):
        super().__init__(msg)


class AggressiveStrategy(GameStrategy):
    def __init__(self) -> None:
        pass

    def execute_turn(self, hand: list[Card],
                     battlefield: list[dict[str, Card | int]]) -> dict:
        if len(battlefield) != 3:
            raise ErrAggrStrategy(
                "ErrAggreStrategy: battlefield can "
                "contain only 2 sides self/opponent: "
                f"{battlefield}")
        if len(hand) == 0:
            raise ErrAggrStrategy(
                "ErrAggreStrategy: hand cant be null at "
                f"start of turn: {hand}")
        target = choice(battlefield[1])
        cards = []
        if len(hand) == 1:
            card1 = hand.pop()
            cards.append(card1)
        else:
            card1 = hand.pop(randint(0, len(hand) - 1))
            card2 = hand.pop(randint(0, len(hand) - 1))
            cards.append(card1)
            cards.append(card2)
        result = self.resolve_effect(cards, battlefield, target)
        return result

    def resolve_effect(self,
                       cards: list[Card],
                       battlefield: list[dict], target: Card) -> dict:
        result = {'cards_played': [],
                  'mana_used': 0, 'targets_attacked': [], 'total_damage': 0}
        for card in cards:
            if isinstance(card, CreatureCard):
                battlefield[0].append(card)
                card.attack_target(target)
                if target.info['name'] not in result['targets_attacked']:
                    result['targets_attacked'].append(target.info['name'])
                result['total_damage'] += card.info['attack']
            elif isinstance(card, SpellCard):
                card.resolve_effect([target])
                damage = card.info['effect']
                damage = int(''.join([c for c in damage if c.isdigit()]))
                if target.info['name'] not in result['targets_attacked']:
                    result['targets_attacked'].append(target.info['name'])
                result['total_damage'] += damage
            result['cards_played'].append(card.info['name'])
            result['mana_used'] += card.info['cost']
        return result

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self,
                           available_targets: list[CreatureCard |
                                                   ArtifactCard |
                                                   Card]) -> list:
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
