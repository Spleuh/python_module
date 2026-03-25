from functools import wraps
from typing import Callable, Any
from time import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {getattr(func, '__name__')}")
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"Spell completed in {(end - start):.2f}secondes")
        return result
    return wrapper

@spell_timer
def test():
    print("this is a timer test")

def main():
    test()

if __name__ == '__main__':
    main()