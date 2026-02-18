def lst_comp(players: dict[str, dict[str, int | str]],
             sessions: list[dict[str, str | int | bool]]) -> None:
    """demo using list comprehension"""
    print("=== List Comprehension Examples ===")
    names: list[str] = [name for name in players.keys()]
    players_data: list[dict[str, int | str]] = [
        data for data in players.values()]
    high_scorers: list[str] = [
        scorer for scorer in names if int(
            players[scorer]['total_score']) > 2000]
    print(f"High scorers (>2000): {high_scorers}")
    dbl_scores: list[int | str] = [
        data['total_score'] * 2 for data in players_data]
    print(f"Scores doubled: {dbl_scores}")
    active_player: list[str] = [
        str(data.get("player")) for data in sessions]
    print(f"Active players {sorted(set(active_player))}")


def dict_comp(players: dict[str, dict[str, int | str]]) -> None:
    """demo using dict comprehension"""
    print("=== Dict Comprehension Examples ===")
    player_score: dict[str, int] = {n[0]: n[1].get(
        "total_score") for n in players.items()}
    print(f"Player scores: {player_score}")
    all_scores: list[int] = [score[1].get(
        "total_score") for score in players.items()]
    high: int = len([score for score in all_scores if score >= 4000])
    medium: int = len([score for score in all_scores if 1450 <= score < 4000])
    low: int = len([score for score in all_scores if score < 1450])
    score_categories = {"high": high, "medium": medium, "low": low}
    print(f"Score categories: {score_categories}")
    count_achiev: dict[str, int] = {
        x[0]: x[1]["achievements_count"] for x in players.items()}
    print(f"Achievement counts: {count_achiev}")


def set_comp(sessions: list[dict[str, str | int | bool]],
             achievements: list[str]) -> None:
    """demo using set comprehension"""
    print("=== Set Comprehension Examples ===")
    unique_player: set[str] = {player["player"] for player in sessions}
    print(f"Unique players: {unique_player}")
    unique_achiev: set[str] = {achievement for achievement in achievements}
    print(f"Unique achievements: {unique_achiev}")
    region: dict[str: int] = {
        "north": 1,
        "east": 1,
        "central": 1,
        "south": 0}
    active_region: set[str] = {
        activ[0] for activ in region.items() if activ[1] == 1}
    print(f"Active regions: {active_region}")


def combined_comp(
        players: dict[str, dict[str, int | str]],
        achievements: list[str]) -> None:
    """mix all comprehension"""
    print("=== Combined Analysis ===")
    total_player: int = len([player for player in players.keys()])
    print(f"Total players: {total_player}")
    unique_achiev: int = len({achiev for achiev in achievements})
    print(f"Unique achievements: {unique_achiev}")
    sum_scores = sum([score[1].get(
        "total_score") for score in players.items()])
    print(f"Average score: {sum_scores / total_player:.2f}")
    top_performer: str = max(
        players, key=lambda name: players[name]["total_score"])
    print(
        f"Top performer: {top_performer} ("
        f"{players[top_performer]['total_score']} "
        f"points, {players[top_performer]['achievements_count']}"
        " achievements)")


def dashboard(data: dict[str, dict[str, dict[str, int | str]]
              | list[dict[str, str | int | bool]] | list[str]]) -> None:
    """demo display dashboard"""
    print("=== Game Analytics Dashboard ===\n")
    lst_comp(data["players"], data["sessions"])
    print()
    dict_comp(data["players"])
    print()
    set_comp(data["sessions"], data["achievements"])
    print()
    combined_comp(data["players"], data["achievements"])


if __name__ == "__main__":
    data: dict[
        str,
        dict[str, dict[str, int | str]]
        | list[dict[str, str | int | bool]]
        | list[str]
    ] = {
        'players': {
            'alice': {
                'level': 41,
                'total_score': 2824,
                'sessions_played': 13,
                'favorite_mode': 'ranked',
                'achievements_count': 5,
            },
            'bob': {
                'level': 16,
                'total_score': 4657,
                'sessions_played': 27,
                'favorite_mode': 'ranked',
                'achievements_count': 2,
            },
            'charlie': {
                'level': 44,
                'total_score': 9935,
                'sessions_played': 21,
                'favorite_mode': 'ranked',
                'achievements_count': 7,
            },
            'diana': {
                'level': 3,
                'total_score': 1488,
                'sessions_played': 21,
                'favorite_mode': 'casual',
                'achievements_count': 4,
            },
            'eve': {
                'level': 33,
                'total_score': 1434,
                'sessions_played': 81,
                'favorite_mode': 'casual',
                'achievements_count': 7,
            },
            'frank': {
                'level': 15,
                'total_score': 8359,
                'sessions_played': 85,
                'favorite_mode': 'competitive',
                'achievements_count': 1,
            },
        },
        'sessions': [
            {
                'player': 'bob',
                'duration_minutes': 94,
                'score': 1831,
                'mode': 'competitive',
                'completed': False,
            },
            {
                'player': 'bob',
                'duration_minutes': 32,
                'score': 1478,
                'mode': 'casual',
                'completed': True,
            },
            {
                'player': 'diana',
                'duration_minutes': 17,
                'score': 1570,
                'mode': 'competitive',
                'completed': False,
            },
            {
                'player': 'alice',
                'duration_minutes': 98,
                'score': 1981,
                'mode': 'ranked',
                'completed': True,
            },
            {
                'player': 'diana',
                'duration_minutes': 15,
                'score': 2361,
                'mode': 'competitive',
                'completed': False,
            },
            {
                'player': 'eve',
                'duration_minutes': 29,
                'score': 2985,
                'mode': 'casual',
                'completed': True,
            },
            {
                'player': 'frank',
                'duration_minutes': 34,
                'score': 1285,
                'mode': 'casual',
                'completed': True,
            },
            {
                'player': 'alice',
                'duration_minutes': 53,
                'score': 1238,
                'mode': 'competitive',
                'completed': False,
            },
            {
                'player': 'bob',
                'duration_minutes': 52,
                'score': 1555,
                'mode': 'casual',
                'completed': False,
            },
            {
                'player': 'frank',
                'duration_minutes': 92,
                'score': 2754,
                'mode': 'casual',
                'completed': True,
            },
            {
                'player': 'eve',
                'duration_minutes': 98,
                'score': 1102,
                'mode': 'casual',
                'completed': False,
            },
            {
                'player': 'diana',
                'duration_minutes': 39,
                'score': 2721,
                'mode': 'ranked',
                'completed': True,
            },
            {
                'player': 'frank',
                'duration_minutes': 46,
                'score': 329,
                'mode': 'casual',
                'completed': True,
            },
            {
                'player': 'charlie',
                'duration_minutes': 56,
                'score': 1196,
                'mode': 'casual',
                'completed': True,
            },
            {
                'player': 'eve',
                'duration_minutes': 117,
                'score': 1388,
                'mode': 'casual',
                'completed': False,
            },
            {
                'player': 'diana',
                'duration_minutes': 118,
                'score': 2733,
                'mode': 'competitive',
                'completed': True,
            },
            {
                'player': 'charlie',
                'duration_minutes': 22,
                'score': 1110,
                'mode': 'ranked',
                'completed': False,
            },
            {
                'player': 'frank',
                'duration_minutes': 79,
                'score': 1854,
                'mode': 'ranked',
                'completed': False,
            },
            {
                'player': 'charlie',
                'duration_minutes': 33,
                'score': 666,
                'mode': 'ranked',
                'completed': False,
            },
            {
                'player': 'alice',
                'duration_minutes': 101,
                'score': 292,
                'mode': 'casual',
                'completed': True,
            },
            {
                'player': 'frank',
                'duration_minutes': 25,
                'score': 2887,
                'mode': 'competitive',
                'completed': True,
            },
            {
                'player': 'diana',
                'duration_minutes': 53,
                'score': 2540,
                'mode': 'competitive',
                'completed': False,
            },
            {
                'player': 'eve',
                'duration_minutes': 115,
                'score': 147,
                'mode': 'ranked',
                'completed': True,
            },
            {
                'player': 'frank',
                'duration_minutes': 118,
                'score': 2299,
                'mode': 'competitive',
                'completed': False,
            },
            {
                'player': 'alice',
                'duration_minutes': 42,
                'score': 1880,
                'mode': 'casual',
                'completed': False,
            },
            {
                'player': 'alice',
                'duration_minutes': 97,
                'score': 1178,
                'mode': 'ranked',
                'completed': True,
            },
            {
                'player': 'eve',
                'duration_minutes': 18,
                'score': 2661,
                'mode': 'competitive',
                'completed': True,
            },
            {
                'player': 'bob',
                'duration_minutes': 52,
                'score': 761,
                'mode': 'ranked',
                'completed': True,
            },
            {
                'player': 'eve',
                'duration_minutes': 46,
                'score': 2101,
                'mode': 'casual',
                'completed': True,
            },
            {
                'player': 'charlie',
                'duration_minutes': 117,
                'score': 1359,
                'mode': 'casual',
                'completed': True,
            },
        ],
        'game_modes': [
            'casual',
            'competitive',
            'ranked',
        ],
        'achievements': [
            'first_blood',
            'level_master',
            'speed_runner',
            'treasure_seeker',
            'boss_hunter',
            'pixel_perfect',
            'combo_king',
            'explorer',
        ],
    }
    dashboard(data)
