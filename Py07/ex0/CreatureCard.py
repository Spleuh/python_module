from ex0.Card import Card, ErrCard


class ErrCreatureC(ErrCard):
    def __init__(self, *args):
        super().__init__(*args)


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int) -> None:
        super().__init__(name, cost, rarity)
        if health < 1:
            raise ErrCreatureC(f"ErrorCreature: health < 1: {health}")
        if attack < 0:
            raise ErrCreatureC(f"ErrorCreature: attack < 0: {attack}")
        self.info.update({'type': 'Creature', 'attack': attack,
                          'health': health})

    def play(self, game_state) -> dict:
        result = super().play(game_state)
        result.update({'effect': 'Creature summoned to battlefield'})
        return result

    def attack_target(self, target: Card) -> dict:
        result = {'attacker': self.info['name'], 'target': target.info['name']}
        if target.info['type'] == 'Creature' and target.info['health'] > 0:
            dmg_dealt = min(self.info['attack'], target.info['health'])
            result.update({'damage_dealt': dmg_dealt, 'combat_resolved': True})
        else:
            raise ErrCreatureC("ErrorCreature: Target is not a "
                               f"creature: {target.info['name']}")
        return result
