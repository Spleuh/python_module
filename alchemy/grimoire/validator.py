from .validation_utils import is_valid


def validate_ingredients(ingredients: str) -> str:
    if is_valid(ingredients):
        return (f'{ingredients} - VALID')
    else:
        return (f'{ingredients} - INVALID')
