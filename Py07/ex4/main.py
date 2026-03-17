from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


if __name__ == '__main__':
    card = TournamentCard('Fire Dragon', 3, 'Legendary', 4, 4, 3)
    test = TournamentCard('Fire Wizard', 3, 'Legendary', 4, 4, 3)
    test1 = TournamentCard('Fire Dragon', 3, 'Legendary', 4, 4, 3)
    platform = TournamentPlatform()
    print(platform.register_card(card))
    print(platform.register_card(test))
    print(platform.register_card(test1))