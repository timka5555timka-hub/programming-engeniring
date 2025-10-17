import random



big_list = []

for _ in range(5):

    small_list = [random.randint(1, 100) for _ in range(random.randint(3, 10))]

    big_list.append(small_list)



print(big_list)
