class Ivan:
    """Класс для проверки угадал ли человек имя"""

    __slots__ = ['name']

    def __init__(self, name):
        if name == 'Иван':
            self.name = f"Да, я {name}!"
        else:
            self.name = f"Я не {name}, а Иван"
        print(self.name)

# Тесты
person1 = Ivan('Алексей')
person2 = Ivan('Иван')

# Попытка обратиться к фамилии
try:
    person2.surname = 'Петров'
except AttributeError as e:
    print(f"Ошибка: {e}")
