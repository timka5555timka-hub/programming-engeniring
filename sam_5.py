# Базовый (общий) класс Animal (животное)
class Animal:
    # Конструктор базового класса
    def __init__(self, name):
        self.name = name

    # Базовый метод для издавания звука
    # Будет переопределен в дочерних классах
    def make_sound(self):
        pass


# Класс Dog (собака) наследуется от Animal
class Dog(Animal):
    # Конструктор класса Dog
    def __init__(self, name, breed):
        # Вызываем конструктор родительского класса
        super().__init__(name)
        # Добавляем атрибут породы
        self.breed = breed

    # Переопределяем метод make_sound для собаки
    def make_sound(self):
        return f"{self.name} ({self.breed}) говорит: Гав-гав!"


# Класс Cat (кошка) наследуется от Animal
class Cat(Animal):
    # Конструктор класса Cat
    def __init__(self, name, color):
        # Вызываем конструктор родительского класса
        super().__init__(name)
        # Добавляем атрибут цвета
        self.color = color

    # Переопределяем метод make_sound для кошки
    def make_sound(self):
        return f"{self.name} ({self.color}) говорит: Мяу-мяу!"


# Создаем массив с животными
animals = [
    Dog("Рекс", "Овчарка"),
    Cat("Мурка", "Рыжая"),
    Dog("Шарик", "Лабрадор"),
    Cat("Барсик", "Черный")
]

# Полиморфизм: вызываем метод make_sound() для разных типов животных
# Каждый класс реализует свою версию метода
print("=== Звуки животных ===")
for animal in animals:
    print(animal.make_sound())
