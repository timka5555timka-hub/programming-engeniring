class Russian:
    """Класс для приветствия на русском"""

    @staticmethod
    def greeting():
        print("Привет")


class English:
    """Класс для приветствия на английском"""

    @staticmethod
    def greeting():
        print("Hello")


def greet(language):
    language.greeting()

# Тесты
ivan = Russian()
john = English()

greet(ivan)
greet(john)

Russian.greeting()
English.greeting()
