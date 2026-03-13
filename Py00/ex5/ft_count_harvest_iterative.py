def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    if days < 1:
        return None
    i = 1
    while i <= days:
        print("Day ", i)
        i += 1
    print("Harvest time!")
