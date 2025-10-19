def remove_from_tuple(te, element):
    if element not in te:
        return te
    
    lst = list(te)
    lst.remove(element)
    return tuple(lst)

print(remove_from_tuple((1, 2, 3), 1))
print(remove_from_tuple((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
print(remove_from_tuple((2, 4, 6, 6, 4, 2), 9))
