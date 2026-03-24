from typing import Callable, Any
from random import randint

class ErrorHigherMagic(Exception):
    def __init__(self, *args):
        super().__init__(*args)


def safe_exec(f: Callable, **kwargs: Any) -> Any:
    try:
        return f(**kwargs)
    except ErrorHigherMagic as e:
        print(f'{e}')
        return None
    except Exception as e:
        print(f'{e}')
        return None


def check_callable(lst_callable: list[Callable]) -> bool:
    if not all([callable(f) for f in lst_callable]):
        return False
    return True


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    if not check_callable([spell1, spell2]):
        raise ErrorHigherMagic(f"ErrorHigherMagic: spell combiner take 2 callables: {spell1} {spell2}")
    def combined_spell(*args: Any, **kwargs: Any) -> tuple[Any, Any]:
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    if not check_callable([base_spell]):
        raise ErrorHigherMagic(f"ErrorHigherMagic: spell amplifier take 1 callable: {base_spell}")
    def amplified_spell(*args: Any, **kwargs: Any) -> Any:
        return base_spell(*args, **kwargs) * multiplier
    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    if not check_callable([condition, spell]):
        raise ErrorHigherMagic("ErrorHigherMagic: conditional caster take 2 callable: "
                               f"{condition} {spell}")
    def conditioned(*args: Any, **kwargs: Any) -> Any:
        if not condition(*args, **kwargs):
            return 'Spell fizzled'
        return spell(*args, **kwargs)
    return conditioned


def spell_sequence(spells: list[Callable]) -> Callable:
    if not check_callable(spells):
        raise ErrorHigherMagic(f"ErrorHigherMagic: spell sequence take list of callable: {spells}")
    def sequenced(*args: Any, **kwargs: Any) -> list[Any]:
        result = []
        for s in spells:
            result.append(s(*args, **kwargs))
        return result
    return sequenced


def fireball(target: str) -> str:
    return f"Fireball hits {target}"


def heal(target: str) -> str:
    return f"Heals {target}"

def condition(target: str) -> bool:
    if len(target) % 2:
        return True
    return False


def base_spell() -> int:
    return 5

def main() -> None:
    test_values = [16, 5, 10]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']
    print('\nTesting spell combiner...')
    print(f"Combined spell result: {', '.join(spell_combiner(fireball, heal)('Dragon'))}")

    print('\nTesting power amplifier...')
    print(f"Original: {base_spell()} Amplified: {power_amplifier(base_spell, 5)()}")

    print('\nTesting conditional caster...')
    result = conditional_caster(condition, fireball)(target='Dragoon')
    print(f"Conditional caster result: {result}")

    print('\nTesting spell sequence...')
    result = spell_sequence([fireball, heal, condition])(target='Dragon')
    print(f"Spell sequence result: {result}")

if __name__ == '__main__':
    main()