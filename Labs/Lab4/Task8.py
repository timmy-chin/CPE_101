def less_than_5(list_stuff):
    i = 0
    for x in list_stuff:
        if len(x) < 5:
            i += 1
    return i
