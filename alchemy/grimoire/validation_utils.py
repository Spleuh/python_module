def is_valid(ingredients: str) -> bool:
    elements = ['fire', 'water', 'earth', 'air']
    for i in elements:
        if i in ingredients:
            return True
    return False
