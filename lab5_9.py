def superset(a, b):

    if a == b:

        print("Множества равны")

    elif a > b:

        print("Объект A является чистым супермножеством")

    elif b > a:

        print("Объект B является чистым супермножеством")

    else:

        print("Супермножество не обнаружено")



set1 = {1, 2, 3}

set2 = {2, 3}

superset(set1, set2)
