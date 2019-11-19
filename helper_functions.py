def stringer(arg):
    '''returns a string made from the argument'''
    return str(arg)

def duplicates(list1, list2):
    '''checks whether the two lists have overlapping elements'''
    duplicates = []
    for item in list1:
        if item in list2:
            duplicates.append(item)
    if len(duplicates) == 0:
        return "There's no overlapping items!"
    else:
        return duplicates
    return

def pancaker(arg):
    '''replaces the first element of a list with the word "pancakes"'''    
    if type(arg) is tuple:
        return ('pancake',) + arg[1:]
    elif type(arg) is list:
        arg[0] = 'pancakes'
        return arg
    else:
        return 'pancake' + arg[1:]





