from functools import reduce, partial, lru_cache, singledispatch
from typing import Callable, Any
import operator


class ErrorFibo(ValueError):
    def __init__(self, *args):
        super().__init__(*args)


class ErrorSpellReducer(ValueError):
    def __init__(self, *args):
        super().__init__(*args)


def safe_exec(f: Callable,*arg, **kwargs: Any) -> Any:
    try:
        return f(*arg, **kwargs)
    except ErrorSpellReducer as e:
        print(f"ErrorSpellReducer: {e}")
        return None
    except (ErrorFibo, RecursionError) as e:
        print(f"ErrorFibo: {e}")
        return None
    except Exception as e:
        print(f"{e}")
        return None


def spell_reducer(spells: list[int], operation: str) -> int:
    supported = {'add': operator.add, 'multiply': operator.mul, 'max': max, 'min': min}
    if operation not in supported.keys():
        raise ErrorSpellReducer(f"Operation not supported: {operation}")
    return reduce(supported[operation], spells)


def base_enchant(power: int, element: str, target: str) -> str:
    return f"{element} spell hit {target} and deals {power} damage"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    result = {
        'ice_enchant': partial(base_enchantment, power=50, element='Ice'),
        'fire_enchant': partial(base_enchantment, power=50, element='Fire'),
        'lightning_enchant': partial(base_enchantment, power=50, element='Lightning')
        }
    return result


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ErrorFibo(f"Fibonacci sequence start at 0 and cant be < 0: {n}")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    @singledispatch
    def cast_spell(spell: Any):
        return f"Cast unknown spell {spell}"
    
    @cast_spell.register
    def damage_spell(damage: int):
        return f"Cast damage spell deal {damage} damage"
    
    @cast_spell.register
    def enchant_spell(enchant: str):
        return f"Cast enchantment spell {enchant}"
    
    @cast_spell.register
    def multi_cast(spells: list):
        result = [cast_spell(s) for s in spells]
        result = "Multi-cast: " + ", ".join(result)
        return result
    return cast_spell


def main() -> None:
    print('\nTesting spell reducer...') 
    print(f'Sum: {spell_reducer([10, 20, 30, 40], 'add')}')
    print(f'Product: {spell_reducer([24, 100, 100], 'multiply')}')
    print(f'Max: {spell_reducer([10, 20, 30, 40], 'max')}')

    print('\nTesting partial enchant...')
    part = partial_enchanter(base_enchant)
    print(f"fire: {part['fire_enchant'](target='Dragon')}")
    print(f"ice: {part['ice_enchant'](target='Dragon')}")
    print(f"lightning: {part['lightning_enchant'](target='Dragon')}")

    print('\n Testing memoized fibonacci...')
    print(f"fib(10): {safe_exec(memoized_fibonacci, 10)}")
    print(f"fib(15): {safe_exec(memoized_fibonacci, 15)}")

    print('\nTesting spell dispatcher...')
    cast = spell_dispatcher()
    print(f"{safe_exec(cast, 3)}")
    print(f"{safe_exec(cast, 'Fire')}")
    print(f"{safe_exec(cast, 2.1)}")
    print(f"{safe_exec(cast, [1, 2, 3, 3.3, 'Fire'])}")


if __name__ == '__main__':
    main()