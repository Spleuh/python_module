import sys
import math


class ParsingCoordError(Exception):
    """custom error for parsing coord"""

    def __init__(
            self,
            message: str = "Invalid argument number",
            prefix: str = "Error parsing coordinate: ") -> None:
        super().__init__(f"{prefix} {message}")


def calc_distance(coord: tuple[int, int, int]) -> float:
    """return distance between two points"""
    distance: float = math.sqrt(
        (coord[0] - 0)**2 + (coord[1] - 0)**2 + (coord[2] - 0)**2)
    return distance


def create_position(tpl_coord: tuple[int, int, int] = (10, 20, 5)) -> None:
    """create position and display distance
    between point (0, 0, 0) and point created"""
    print(f"Position created: {tpl_coord}")
    distance: float = calc_distance(tpl_coord)
    print(f"Distance between (0, 0, 0) and {tpl_coord}: {distance:.2f}")


def print_parsing_coord(tpl_coord: tuple[int, int, int] = (3, 4, 0)) -> None:
    """parsing coordinates"""
    print(
        f"Parsing coordinates: {tpl_coord[0]},"
        f"{tpl_coord[1]},{tpl_coord[2]}")
    print(f"Parsed position: {tpl_coord}")
    dist_between: float = calc_distance(tpl_coord)
    print(f"Distance between (0, 0, 0) and {tpl_coord}: {dist_between:.2f}")


def parsing(lst_coord: list[str] = [
        "abc", "def", "ghi"]) -> tuple[int, int, int]:
    """parsing arg and display default setup if no arg provided"""
    if len(sys.argv) == 1:
        tpl_coord: tuple[int, int, int] = (
            int(lst_coord[0]), int(lst_coord[1]), int(lst_coord[2]))
        return tpl_coord
    elif len(sys.argv) == 2:
        if len(sys.argv[1].split(",")) != 3:
            raise ParsingCoordError()
        x, y, z = sys.argv[1].split(",")
        tpl_coord: tuple[int, int, int] = (int(x), int(y), int(z))
        return tpl_coord
    elif len(sys.argv) == 4:
        tpl_coord: tuple[int, int, int] = (
            int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
        return tpl_coord
    raise ParsingCoordError()


def unpacking(tpl_coord: tuple[int, int, int] = (3, 4, 0)) -> None:
    """demo unpacking"""
    print("Unpacking demonstration:")
    x, y, z = tpl_coord
    print(f"Player at x={tpl_coord[0]}, y={tpl_coord[1]}, z={tpl_coord[2]}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    if len(sys.argv) != 1:
        try:
            tpl_coord: tuple[int, int, int] = parsing()
            create_position()
            print()
            print_parsing_coord(tpl_coord)
            print()
            unpacking(tpl_coord)
            print()
            unpacking()
        except Exception as e:
            if type(e).__name__ == "ValueError":
                print(f"Error parsing coordinates: {e}")
                print(
                    f"Error details - Type: {type(e).__name__}, "
                    f"Args: (\"{e}\"),")
            elif type(e).__name__ == "ParsingCoordError":
                print(f"{e}")
                print("Error details - "
                      f"Type: {type(e).__name__}, "
                      "3 values needed (ft_coordinate_system.py \"x, y, z\" "
                      "or ft_coordinate_system.py x y z)")
            else:
                print("Error details - "
                      f"Type: {type(e).__name__}, {e} ")
    else:
        try:
            create_position()
            print()
            print_parsing_coord()
            print()
            unpacking()
        except (ParsingCoordError, ValueError, OverflowError) as e:
            print(f"{e}")
