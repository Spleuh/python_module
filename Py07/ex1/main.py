from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck, ErrDeck
from ex0.Card import ErrCard
from ex0.CreatureCard import CreatureCard


def main() -> None:
    print('\n=== DataDeck Deck Builder ===\n')
    print('Building deck with different card types...')
    try:
        game_state = {'available_mana': 5}
        spell = SpellCard('Lightning Bolt', 3, 'Common',
                          'Deal 3 damage to target')
        artifact = ArtifactCard("Mana Crystal", 2,
                                "Rare", 3, "Permanent: +1 mana per turn")
        creature = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
        deck = Deck()
        deck.add_card(spell)
        deck.add_card(artifact)
        deck.add_card(creature)
        print(f"Deck stats: {deck.get_deck_stats()}\n")

        deck.shuffle()
        print('Drawing and playing cards:\n')
        drew = deck.draw_card()
        print(f"Drew: {drew.info['name']} ({drew.info['type'].capitalize()})")
        print(drew.play(game_state))

        drew = deck.draw_card()
        print(f"\nDrew: {drew.info['name']} "
              f"({drew.info['type'].capitalize()})")
        print(drew.play(game_state))

        drew = deck.draw_card()
        print(f"\nDrew: {drew.info['name']} "
              f"({drew.info['type'].capitalize()})")
        print(drew.play(game_state))

    except (ErrCard, ErrDeck) as e:
        print(f'{e}')
    finally:
        print("\nPolymorphism in action: Same interface, "
              "different card behaviors!")


if __name__ == '__main__':
    main()
