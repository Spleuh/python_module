from typing import Callable


def mage_counter() -> Callable:
    count = 0
    def counter() -> int:
        nonlocal count
        count +=1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power
    def accumulator(up: int) -> int:
        nonlocal power
        power += up
        return power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant_item(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchant_item


def memory_vault() -> dict[str, Callable]:
    vault = {}
    def store(spell_name: str, spell: Callable) -> None:
        vault[spell_name] = spell
    
    def recall(spell_name: str) -> Callable | str:
        return vault.get(spell_name, 'Memory not found')

    def get_name_stored() -> list[str]:
        return list(vault.keys())

    return {'store': store, 'recall': recall, 'get_stored': get_name_stored}



def main():
    print('\nTesting mage counter...')
    counter = mage_counter()
    for i in range(1, 4):
        print(f"Call {i}: {counter()}")
    
    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(3)
    for i in range(1, 4):
        print(f"Call {i}: {accumulator(i)}")

    print('\nTesting enchantment factory...')
    enchant_flam = enchantment_factory('Flaming')
    print(f"{enchant_flam('Sword')}")
    enchant_froz = enchantment_factory('Frozen')
    print(f"{enchant_froz('Shield')}")

    print("\nTesting memory vault...")
    vault = memory_vault()
    print(f"Store counter: ")
    print(f"before: {vault.get('get_stored')()} ",end='')
    vault.get('store')('counter', counter)
    print(f"after: {vault.get('get_stored')()}")
    print('Recall counter:')
    recall_counter = vault.get('recall')('counter')
    if isinstance(recall_counter, Callable):
        for i in range(1, 4):
            print(f"Recall {i}: {recall_counter()}")
    if isinstance(recall_counter, str):
        print(recall_counter)

if __name__ == '__main__':
    main()