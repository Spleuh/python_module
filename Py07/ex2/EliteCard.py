from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex0.Card import Card, ErrCard
from ex0.CreatureCard import CreatureCard


class ErrEliteC(ErrCard):
    def __init__(self, *args) -> None:
        super().__init__(*args)


class EliteCard(Card, Combatable, Magical):
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            attack: int,
            health: int,
            spell: dict) -> None:
        super().__init__(name, cost, rarity)
        self.info.update(
            {'health': health, 'magic':
             {'spells': spell, 'total_mana': 4},
             'combat': {'attack': attack, 'combat_type': 'melee',
                        'defense': 3}})

    def attack(self, target: Card) -> dict:
        if not isinstance(target, Card):
            raise ErrEliteC("ErreliteC: target is not a card: "
                            f"{target.info}")
        result = super().attack(target)
        combat_dict = self.info['combat']
        result.update({'damage': combat_dict['attack'],
                       'combat_type': combat_dict['combat_type']})
        target.info['health'] -= result['damage']
        return result

    def defend(self, incomming_damage: int) -> dict:
        result = super().defend(incomming_damage)
        combat_dict = self.info['combat']
        dmg_taken = combat_dict['defense'] - incomming_damage
        if dmg_taken >= 0:
            dmg_blocked = incomming_damage
            dmg_taken = 0
        else:
            dmg_blocked = combat_dict['defense']
            dmg_taken *= -1
        self.info['health'] -= dmg_taken
        alive = True
        if self.info['health'] <= 0:
            alive = False
        result.update({'damage_taken': dmg_taken,
                       'damage_blocked': dmg_blocked,
                       'still_alive': alive})
        return result

    def get_combat_stats(self) -> dict:
        return self.info['combat']

    def cast_spell(self, spell_name: str, targets: list[CreatureCard]) -> dict:
        magic = self.info['magic']
        cost = "None"
        try:
            cost = magic['spells'][spell_name]
        except KeyError:
            raise ErrEliteC(f"ErrEliteC: Spell not found: {spell_name}")
        name_targ = []
        for i in targets:
            name_targ.append(i.info['name'])
        result = {'caster': self.info['name'],
                  'spell': spell_name, 'targets': name_targ,
                  'mana_used': cost}
        return result

    def channel_mana(self, amount) -> dict:
        if amount < 1:
            raise ErrEliteC(f"ErrEliteC: amount mana <= 0: {amount}")
        self.info['magic']['total_mana'] += amount
        result = {'channeled': amount,
                  'total_mana': self.info['magic']['total_mana']}
        return result

    def get_magic_stats(self) -> dict:
        return self.info['magic']

    def play(self, game_state) -> dict:
        return super().play(game_state)
