def ft_count_harvest_recursive(days=-1):
    if days == -1:
        test = int(input("Days until harvest: "))
    else:
        test = days
    if test < 1:
        return 1
    else:
        ft_count_harvest_recursive(test - 1)
        print("Day ", test)
        if days == -1:
            print("Harvest time!")
