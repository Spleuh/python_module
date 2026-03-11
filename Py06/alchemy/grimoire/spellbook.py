from .validator import validate_ingredients


def record_spell(spell_name: str, ingredients: str) -> str:
    result = validate_ingredients(ingredients)
    if 'INVALID' in result:
        tmp = 'rejected'
    else:
        tmp = 'recorded'
    return ("Spell " + tmp + f": {spell_name} ({result})")
