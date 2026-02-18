import sys


def print_arg() -> None:
    print("=== Command Quest ===")
    nb_arg: int = len(sys.argv)
    if nb_arg < 2:
        print("No argument provided!")
        print(f"Programme name: {sys.argv[0]}")
    else:
        print(f"Programme name: {sys.argv[0]}")
        print(f"Argument received: {nb_arg - 1}")
        i: int = 1
        while i < nb_arg:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    print(f"Total arguments: {nb_arg}")


if __name__ == "__main__":
    print_arg()
