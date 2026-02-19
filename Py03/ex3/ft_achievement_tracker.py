class Player:
    """class player"""
    def __init__(self, name: str, achievements: set[str] = set()) -> None:
        """init player"""
        self.name: str = name
        self.achievements: set[str] = achievements


class AchieveManager:
    """Achievement manager"""
    lst_players: dict[str, Player] = {}

    @classmethod
    def add_player(cls, name: str) -> None:
        """add player to lst_player"""
        cls.lst_players[name] = Player(name)

    @classmethod
    def add_achievement(cls, name: str, add_achiev: set[str]) -> None:
        """add achievements to lst_players"""
        cls.lst_players[name].achievements = add_achiev.union(
            cls.lst_players[name].achievements)

    @classmethod
    def achievement_tracker(cls) -> None:
        """display achievement tracker system"""
        print("=== Achievement Tracker System ===\n")
        for player in cls.lst_players.values():
            print(f"Player {player.name} achievements: {player.achievements}")

    @classmethod
    def union_all(cls) -> set[str]:
        """return all achievements common to all players"""
        union_all: set[str] = set()
        for player in cls.lst_players.values():
            union_all = player.achievements.union(union_all)
        return union_all

    @classmethod
    def get_player(cls, name: str) -> Player:
        """return Player from lst_player"""
        return cls.lst_players[name]

    @classmethod
    def diff_all(cls, name: str) -> set[str]:
        """return unique achievements of a player"""
        diff_all: set[str] = cls.get_player(name).achievements
        for player in cls.lst_players.values():
            if player.name != name:
                diff_all = diff_all.difference(player.achievements)
        return diff_all

    @classmethod
    def rare_achievement(cls) -> set[str]:
        """return unique achievement of all player"""
        rare_achiev: set[str] = set()
        for player in cls.lst_players.keys():
            rare_achiev = rare_achiev.union(cls.diff_all(player))
        return rare_achiev

    @classmethod
    def inter_all(cls) -> set[str]:
        """return common achievement of all players"""
        inter_all: set[str] = cls.union_all()
        for player in cls.lst_players.values():
            inter_all = player.achievements.intersection(inter_all)
        return inter_all

    @classmethod
    def achievement_analytics(cls, player_1: str, player_2: str) -> None:
        """display achievement analytics"""
        print("=== Achievement Analytics ===")
        unique_achiev: set[str] = cls.union_all()
        common_achiev: set[str] = cls.inter_all()
        rare_achiev: set[str] = cls.rare_achievement()
        print(f"All unique achievements: {unique_achiev}")
        print(f"Total unique achievements: {len(unique_achiev)}")
        print()
        print(f"Common to all players: {common_achiev}")
        print(f"Rare achievement (1 player): {rare_achiev}")
        print()
        cls.display_common(
            cls.get_player(player_1),
            cls.get_player(player_2))
        cls.display_unique(cls.get_player(player_1), cls.get_player(player_2))
        cls.display_unique(cls.get_player(player_2), cls.get_player(player_1))

    @staticmethod
    def inter(player_1: Player, player_2: Player) -> set[str]:
        """return common lst of achievement"""
        common: set[str] = player_1.achievements.intersection(
            player_2.achievements)
        return common

    @staticmethod
    def diff(player_1: Player, player_2: Player) -> set[str]:
        """return lst of player_1's achievements - player_2's achievements"""
        unique: set[str] = player_1.achievements.difference(
            player_2.achievements)
        return unique

    @classmethod
    def display_common(cls, player_1: Player, player_2: Player) -> None:
        """display common achievements between player_1 and player_2"""
        print(
            f"{player_1.name.capitalize()} vs "
            f"{player_2.name.capitalize()} common: "
            f"{cls.inter(player_1, player_2)}")

    @classmethod
    def display_unique(cls, player_1: Player, player_2: Player) -> None:
        """display lst of player_1's achievements - player_2's achievements"""
        print(f"{player_1.name.capitalize()} unique:"
              f" {cls.diff(player_1, player_2)}")


def setup_default() -> None:
    """setup data for demo"""
    manager: AchieveManager = AchieveManager()
    manager.add_player("alice")
    manager.add_player("bob")
    manager.add_player("charlie")
    manager.add_achievement(
        "alice", set([
            "first_kill", "level_10", "treasure_hunter", "speed_demon"]))
    manager.add_achievement(
        "bob", set([
            "first_kill", "level_10", "boss_slayer", "collector"]))
    manager.add_achievement("charlie",
                            set(["level_10",
                                 "treasure_hunter",
                                 "boss_slayer",
                                 "speed_demon",
                                 "perfectionist"]))


if __name__ == "__main__":
    setup_default()
    manager: AchieveManager = AchieveManager()
    # test: dict[str,
    #            list[str]] = {'alice': ['first_blood',
    #                                    'pixel_perfect',
    #                                    'speed_runner',
    #                                    'first_blood',
    #                                    'first_blood'],
    #                          'bob': ['level_master',
    #                                  'boss_hunter',
    #                                  'treasure_seeker',
    #                                  'level_master',
    #                                  'level_master'],
    #                          'charlie': ['treasure_seeker',
    #                                      'boss_hunter',
    #                                      'combo_king',
    #                                      'first_blood',
    #                                      'boss_hunter',
    #                                      'first_blood',
    #                                      'boss_hunter',
    #                                      'first_blood'],
    #                          'diana': ['first_blood',
    #                                    'combo_king',
    #                                    'level_master',
    #                                    'treasure_seeker',
    #                                    'speed_runner',
    #                                    'combo_king',
    #                                    'combo_king',
    #                                    'level_master'],
    #                          'eve': ['level_master',
    #                                  'treasure_seeker',
    #                                  'first_blood',
    #                                  'treasure_seeker',
    #                                  'first_blood',
    #                                  'treasure_seeker'],
    #                          'frank': ['explorer',
    #                                    'boss_hunter',
    #                                    'first_blood',
    #                                    'explorer',
    #                                    'first_blood',
    #                                    'boss_hunter']}
    # for player in test.items():
    #     manager.add_player(player[0])
    #     manager.add_achievement(player[0], set(player[1]))
    manager.achievement_tracker()
    print()
    player_1: str = "alice"
    player_2: str = "bob"
    manager.achievement_analytics(player_1, player_2)
