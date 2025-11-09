class Mammal:
    """Базовый класс - Млекопитающие"""

    className = 'Mammal'

    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"{self.name} является млекопитающим")


class Dog(Mammal):
    """Класс Собака"""

    species = 'canine'
    sounds = 'wow'

    def bark(self):
        print(f"{self.name} лает: {self.sounds}")


class Cat(Mammal):
    """Класс Кошка"""

    species = 'feline'
    sounds = 'meow'

    def meow(self):
        print(f"{self.name} мяукает: {self.sounds}")

# Тесты
dog = Dog("Бобик")
cat = Cat("Мурка")

dog.info()
cat.info()

dog.bark()
cat.meow()
