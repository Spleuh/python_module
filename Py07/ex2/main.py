from ex2.EliteCard import EliteCard, ErrCard
from ex0.CreatureCard import CreatureCard


def main() -> None:
    try:
        print('\n=== DataDeck Ability System ===\n')
        print('EliteCard capabilities:')
        print("- Card: ['play', 'get_card_info', 'is_playable']")
        print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
        print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

        print('\nPlaying Arcane Warrior (Elite Card):\n')
        arc_war = EliteCard('Arcane Warrior', 5, 'Rare', 5, 10,
                            {'Fire Ball': 4})
        arc_war.play({"available_mana": 10})
        dragon = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
        gob_war = CreatureCard('Goblin Warrior', 2, 'Common', 3, 7)

        print('Combat phase:')
        print(f'Attack result: {arc_war.attack(dragon)}')
        print(f'Deffense result: {arc_war.defend(5)}')

        print('\nMagic phase:')
        print("Spell cast: "
              f"{arc_war.cast_spell('Fire Ball', [dragon, gob_war])}")
        print(f"Mana channel: {arc_war.channel_mana(3)}")

        print('\nMultiple interface implementation successful!')
    except ErrCard as e:
        print(f"{e}")


if __name__ == '__main__':
    main()
