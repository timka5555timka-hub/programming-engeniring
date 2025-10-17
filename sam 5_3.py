from math import sqrt



one = [12, 25, 3, 48, 71]

two = [5, 18, 40, 62, 98]

three = [4, 21, 37, 56, 84]



# Минимальные и максимальные стороны

a_min, b_min, c_min = min(one), min(two), min(three)

a_max, b_max, c_max = max(one), max(two), max(three)



def heron(a, b, c):

    p = (a + b + c) / 2

    return round(sqrt(p * (p - a) * (p - b) * (p - c)), 2)



print("Площадь треугольника из минимальных сторон:", heron(a_min, b_min, c_min))

print("Площадь треугольника из максимальных сторон:", heron(a_max, b_max, c_max))
