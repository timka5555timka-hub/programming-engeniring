from triangle import heron

a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))

print("Площадь треугольника:", heron(a, b, c))
