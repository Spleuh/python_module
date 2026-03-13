def ft_seed_inventory(seed_typ: str, quantity: int, unit: str) -> None:
    list_units = ['packets', 'grams', 'area']
    list_msg = [' packets available', ' grams total', ' square meters']
    if unit not in list_units:
        print("Unknown unit type")
        return None
    i = list_units.index(unit)
    if unit == "area":
        print(seed_typ.capitalize() + " seeds: cover " +
              str(quantity) + list_msg[i])
    else:
        print(seed_typ.capitalize() + " seeds: " +
              str(quantity) + list_msg[i])
