from SpellCard import SpellCard, ErrSpellC
from ex0.Card import ErrCard


def main():
    try:
        spell = SpellCard('Lightning Bolt', 3, 'Common', 'Deal 3 damage to target')
        print(spell.get_card_info())
    except ErrCard as e:
        print(f'{e}')


if __name__ == '__main__':
    main()
