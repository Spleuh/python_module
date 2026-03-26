from functools import wraps
from typing import Callable, Any
from time import time
from random import randint


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"Spell completed in {(end - start):.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def spell_validator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            tmp = kwargs.get('power')
            if tmp is None and len(args) > 2:
                tmp = args[2]
            if tmp is None or tmp < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return spell_validator


def retry_spell(max_attempts: int) -> Callable:
    def retry(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            count = 1
            while count <= max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if count < max_attempts:
                        print(f'Spell failed, retrying...(attempt {count}/{max_attempts})')
                    count += 1
            return f'Spell casting failed after {max_attempts} attempts'
        return wrapper
    return retry


class MageGuild:
    def __init__(self, name: str) -> None:
        self.name = name
        self.spells = {}
                
    @staticmethod
    def valid_mage_name(name: str) -> bool:
        result = False
        if name:
            result = all((c.isalpha() or c == ' ') for c in name)
        return result
    
    def add_spell(self, spell_name: str, spell: Callable) -> None:
        self.spells[spell_name] = spell
    
    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int):
        return 'Successfully cast ' + spell_name + f' with {power} power'


@spell_timer
def fire_ball() -> str:
    return 'Fireball cast!'


@retry_spell(2)
def retry_test() -> str:
    rand = randint(1, 10)
    if rand % 2:
        return "Retry test success"
    raise ValueError(f"rand is not odd: {rand}")



def main():
    print("\nTesting spell timer...")
    print("Casting fireball...")
    result = fire_ball()
    print(f"Result: {result}")

    print('\nTesting MageGuild...')
    mage = None
    try:
        print(MageGuild.valid_mage_name('jsam'))
        print(MageGuild.valid_mage_name('324'))
        mage = MageGuild('jsam')
    except Exception as e:
        print(f"{e}")

    if mage:
        print(mage.cast_spell('Lightning', 15))
        print(mage.cast_spell('Lightning', 2))

    print('\nTesting retry spell...')
    print(retry_test())


if __name__ == '__main__':
    main()