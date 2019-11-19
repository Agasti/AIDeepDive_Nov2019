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
    
    my_list = list(arg)
    my_list[0] = 'pancakes'
    return my_list





