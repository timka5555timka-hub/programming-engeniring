# Пример с set()

s = set([1, 2, 3])

for i in range(4, 7):

    s.add(i)

print("Изменяемое множество:", s)



# Пример с frozenset()

f = frozenset([1, 2, 3])

# f.add(4)  # Ошибка! frozenset неизменяемый

print("Неизменяемое множество:", f)
