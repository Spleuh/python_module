from ex1.SpellCard import SpellCard, ErrSpellC
from ex1.ArtifactCard import ArtifactCard, ErrArtifactC
from ex0.Card import ErrCard


def main():
    try:
        game_state = {'available_mana': 5}
        spell = SpellCard('Lightning Bolt', 3, 'Common', 'Deal 3 damage to target')
        print(spell.get_card_info())
        artifact = ArtifactCard("Mana Crystal", 2, "Rare", 3, "Permanent: +1 mana per turn")
        print(artifact.get_card_info())
        print(artifact.play(game_state))
        print(artifact.activate_ability())
    except ErrCard as e:
        print(f'{e}')


if __name__ == '__main__':
    main()
