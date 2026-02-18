import sys


class NoScoreError(Exception):
    """Error custom score"""
    pass


def display_leaderboard(scores: list[int]) -> None:
    """display leaderboard"""
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    test: float = sum(scores) / len(scores)
    if test > sys.maxsize:
        print(f"Average score: {test}")
    else:
        print(f"Average score: {test:.2f}")
    print(f"Hight score: {max(scores)}")
    print(f"Low scores: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


def list_score() -> list[int]:
    """return list[int] from sys.argv"""
    print("=== Player Score Analytics ===")
    len_scores: int = len(sys.argv)
    if len_scores < 2:
        raise NoScoreError(
            "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        scores: list[int] = []
        i: int = 1
        while i < len_scores:
            score_int: int = int(sys.argv[i])
            scores.append(score_int)
            i += 1
        return scores


def print_scores() -> None:
    """display leaderboard"""
    scores: list[int] = []
    try:
        scores = list_score()
    except (NoScoreError, ValueError) as e:
        if type(e) is ValueError:
            print(f"Caught {type(e).__name__}: {e} is not a valide number")
        elif type(e) is NoScoreError:
            print(f"No score provided. {e}")
    else:
        display_leaderboard(scores)
    finally:
        print()


if __name__ == "__main__":
    print_scores()
