from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


if __name__ == '__main__':
    card = TournamentCard('Fire Dragon', 3, 'Legendary', 4, 4, 3)
    card1 = TournamentCard('Fire Dragon', 3, 'Legendary', 4, 4, 3)
    card2 = TournamentCard('Fire Dragon', 3, 'Legendary', 4, 4, 3)
    test = TournamentCard('Fire Wizard', 3, 'Legendary', 4, 4, 3)
    test2 = TournamentCard('Fire Wizard', 3, 'Legendary', 4, 4, 3)
    platform = TournamentPlatform()
    print(platform.register_card(card))
    print(platform.register_card(test))
    print(platform.register_card(test2))
    print(platform.register_card(card1))
    print(platform.register_card(card2))
    result_match = platform.create_match('dragon_0', 'wizard_0')
    print(result_match)
    lst_sorted = platform.get_leaderboard()
    for i, card in enumerate(lst_sorted):
        name = card.info['name']
        rating = card.info['stats']['rank']
        win = card.info['stats']['win']
        loose = card.info['stats']['loose']
        print(f"{i + 1}. {name} - Rating: {rating} ({win}-{loose})")
