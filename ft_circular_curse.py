from alchemy.grimoire import validate_ingredients, record_spell


def demo():
    print('\n=== Circular Curse Breaking ===\n')
    print('Testing ingredinet validation:')
    print("validate_ingredients(\"fire_air\"): "
          f"{validate_ingredients('fire_air')}")
    print("validate_ingredients(\"dragon_scales\"): "
          f"{validate_ingredients('dragon_scales')}")

    print('\nTesting spell recording with valitdation:')
    print("record_spell(\"Fireball\", \"fire_air\"): "
          f"{record_spell('Fireball', 'fire_air')}")
    print("record_spell(\"Dark Magic\", \"shadow\"): "
          f"{record_spell('Dark Magic', 'shadow')}\n")

    print('Testing Shared Module technique:')
    print("record_spell(\"Lightning\", \"air\"): "
          f"{record_spell('Lightning', 'air')}\n")

    print('Circular dependency curse avoided using shared module!')
    print('All spells processed safely!')


if __name__ == '__main__':
    demo()
