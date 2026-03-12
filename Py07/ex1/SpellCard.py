from ex0.Card import Card, ErrCard
from ex0.CreatureCard import CreatureCard
from random import randint


class ErrSpellC(ErrCard):
    def __init__(self, *args) -> None:
        super().__init__(*args)


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.info.update({'type': 'spell', 'effect_type': effect_type})

    def play(self, game_state: dict) -> dict:
        result = super().play(game_state)
        result.update({'effect': 'Deal 3 damage to target'})
        return result

    def resolve_effect(self, targets: list[CreatureCard]) -> dict:
        if len(targets) == 0:
            raise ErrSpellC(f'ErrSpellC: lst targets is empty: {targets}')
        i_targ = randint(0, len(targets) - 1)
        target = targets[i_targ]
        result = {'Spell played': self.info['name'],
                  'Target': target.info['name']}
        if "Deal" in str(self.info['effect']):
            dmg = "".join([a for a in str(self.info['effect']) if a.isdigit()])
            int(dmg)
            target.info['health'] = max(0, target.info['health'] - dmg)
            result.update({"Target's health": target.info['health']})
        return result
