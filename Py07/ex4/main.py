from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print('\n=== DataDeck Tournament Platform ===\n')
    print('Registering Tournament Cards...\n')
    platform = TournamentPlatform()
    card1 = TournamentCard('Fire Dragon', 3, 'Legendary', 3, 4, 3, 1200)
    card2 = TournamentCard('Ice Wizard', 3, 'Legendary', 3, 4, 2, 1150)
    id1 = platform.register_card(card1)
    id2 = platform.register_card(card2)
    print(f"{card1.info['name']} (ID: {id1})")
    print('- Interfaces: [Card, Combatable, Rankable]')
    print(f'- Rating: {card1.get_rank_info()}\n')

    print(f"{card1.info['name']} (ID: {id2})")
    print('- Interfaces: [Card, Combatable, Rankable]')
    print(f'- Rating: {card2.get_rank_info()}\n')

    print('Creating tournament match...')
    result_match = platform.create_match(id1, id2)
    print(f'Match result: {result_match}\n')

    print('Tournament Leaderboard:\n')
    platform.print_leaderboard()

    print('\nPlatform Report:')
    print(platform.generate_tournament_report())

    print('\n=== Tournament Platform Successfully Deployed! ===')
    print('All abstract patterns working together harmoniously!\n')


if __name__ == '__main__':
    main()
