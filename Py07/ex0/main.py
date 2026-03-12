from ex0.CreatureCard import CreatureCard, ErrCreatureC
from ex0.Card import ErrCard


def main():
    print('=== DataDeck Card Foundation ===\n')
    print('Testing Abstract Base Class Design:\n')
    print('CreatureCard Info:')
    try:
        dragon = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
        print(f'{dragon.get_card_info()}\n')

        game_state = {'available_mana': 6}
        print('Playing Fire Dragon with 6 mana available:')
        print(f'Playable: {dragon.is_playable(game_state["available_mana"])}')
        print(f'Play result: {dragon.play(game_state)}\n')

        target = CreatureCard('Goblin Warrior', 2, 'Common', 3, 7)
        print('Fire Dragon attacks Goblin Warrior:')
        print(f'Attack result: {dragon.attack_target(target)}\n')

        game_state['available_mana'] = 3
        print('Testing insufficient mana (3 available):')
        print(f'Playable: {dragon.is_playable(game_state["available_mana"])}')
    except (ErrCard, ErrCreatureC) as e:
        print(f"{e}")
    else:
        print('\nAbstract pattern successfully demonstrated!')


if __name__ == '__main__':
    main()
