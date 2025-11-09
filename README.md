# Тема 9. Концепции и принципы ООП
Отчёт по Теме 9 выполнил:
- Новицкий Тимофей Дмитриевич
- Группа: АИС-23-1

| Задание     | Лаб_Раб     | Сам_Раб     |
| ----------- | ----------- | ----------- |
|  Задание 1  |     +       |      +      |
|  Задание 2  |     +       |             |
|  Задание 3  |     +       |             |
|  Задание 4  |     +       |             |
|  Задание 5  |     +       |             |

# Лабораторная работа 1
## Класс с проверкой имени

```python
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
```

### Результат
Демонстрирует использование `__slots__` для ограничения атрибутов класса.
![Sreen](https://github.com/timka5555timka-hub/programming-engeniring/blob/tema_9/pic/lab1.png?raw=true)
# Лабораторная работа 2
## Класс мороженого с проверкой топпинга

```python
class Icecream:
    """Класс мороженого с возможностью добавления топпинга"""

    def __init__(self, ingredient=None):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None

    def composition(self):
        if self.ingredient:
            print(f"Мороженое с {self.ingredient}")
        else:
            print('Обычное мороженое')

# Тесты
icecream1 = Icecream()
icecream1.composition()

icecream2 = Icecream('шоколадом')
icecream2.composition()

icecream3 = Icecream(5)
icecream3.composition()
```

### Результат
Программа проверяет тип параметра и принимает только строковые значения как топпинг.

![](https://github.com/timka5555timka-hub/programming-engeniring/blob/tema_9/pic/lab2.png?raw=true)

# Лабораторная работа 3
## Инкапсуляция с геттером, сеттером и деструктором

```python
class MyClass:
    """Класс с инкапсуляцией"""

    def __init__(self, value):
        self._value = value
        print(f"Объект создан со значением: {self._value}")

    def set_value(self, value):
        self._value = value
        print(f"Значение установлено: {self._value}")

    def get_value(self):
        return self._value

    def del_value(self):
        del self._value
        print("Атрибут _value удален")

    value = property(get_value, set_value, del_value, "Свойство value")

    def __del__(self):
        print("Объект удаляется (деструктор)")

# Тесты
obj = MyClass(42)
print(obj.get_value())
obj.set_value(45)
obj.value = 100
obj.del_value()
```

### Результат
Демонстрирует использование геттера, сеттера, деструктора и property.

![](https://github.com/timka5555timka-hub/programming-engeniring/blob/tema_9/pic/lab3.png?raw=true)

# Лабораторная работа 4
## Наследование - Млекопитающие, Кошки, Собаки

```python
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
```

### Результат
Демонстрирует наследование классов и доступ к методам родительского класса.

![](https://github.com/timka5555timka-hub/programming-engeniring/blob/tema_9/pic/lab4.png?raw=true)

# Лабораторная работа 5
## Полиморфизм - Приветствия на разных языках

```python
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
```

### Результат
Полиморфизм позволяет использовать одну функцию `greet()` для разных классов.

![](https://github.com/timka5555timka-hub/programming-engeniring/blob/tema_9/pic/lab5.png?raw=true)

# Самостоятельная работа 1
## Садовник и помидоры - Полная ООП система

```python
class Tomato:
    """Класс, описывающий один помидор"""

    STAGES = ['отсутствует', 'цветение', 'зеленый', 'красный']

    def __init__(self, number):
        # приватные динамические свойства
        self._number = number
        self._stage = 0
        print(
            f"Создан помидор №{self._number}: стадия '{self.STAGES[self._stage]}'")

    def grow(self):
        """Переход на следующую стадию созревания"""
        if self._stage < len(self.STAGES) - 1:
            self._stage += 1
            print(
                f"Помидор {self._number} → стадия '{self.STAGES[self._stage]}'")

    def is_ready(self):
        """Проверка зрелости"""
        return self._stage == len(self.STAGES) - 1


class TomatoBush:
    """Класс, моделирующий куст с несколькими помидорами"""

    def __init__(self, count):
        self.tomatoes = [Tomato(i + 1) for i in range(count)]
        print(f"\nПосажен куст с {count} помидорами!\n")

    def grow_all(self):
        """Все помидоры растут"""
        print("Куст растет...")
        for tomato in self.tomatoes:
            tomato.grow()

    def are_all_ripe(self):
        """Все ли плоды созрели"""
        return all(tomato.is_ready() for tomato in self.tomatoes)

    def collect_all(self):
        """Сбор урожая (очистка списка)"""
        self.tomatoes.clear()
        print("Куст пуст — урожай собран!")


class Gardener:
    """Класс садовника"""

    def __init__(self, name, plant):
        self.name = name           # публичное свойство
        self._plant = plant        # приватное свойство
        print(f"Садовник {self.name} начал ухаживать за кустом.\n")

    def care(self):
        """Садовник ухаживает за растением"""
        print(f"{self.name} поливает и рыхлит землю...")
        self._plant.grow_all()

    def gather(self):
        """Проверка и сбор урожая"""
        print(f"\n{self.name} проверяет зрелость урожая...")
        if self._plant.are_all_ripe():
            print("Все помидоры красные! Можно собирать!")
            self._plant.collect_all()
        else:
            print("Еще не все помидоры спелые. Нужно подождать.")

    @staticmethod
    def help():
        """Справка по садоводству"""
        print("=" * 55)
        print(" С П Р А В К А   П О   С А Д О В О Д С Т В У ")
        print("=" * 55)
        print("1. Посадите куст с помидорами.")
        print("2. Ухаживайте за ним, пока все плоды не покраснеют.")
        print("3. Соберите урожай и радуйтесь результату!")
        print("=" * 55)


# ===== Тестирование программы =====
if __name__ == '__main__':
    Gardener.help()
    bush = TomatoBush(4)
    gardener = Gardener("Алексей", bush)

    gardener.care()
    gardener.gather()

    gardener.care()
    gardener.gather()

    gardener.care()
    gardener.gather()

```

### Результат
Комплексная программа, демонстрирующая все принципы ООП: инкапсуляцию, наследование и полиморфизм.

![Скриншот](https://github.com/timka5555timka-hub/programming-engeniring/blob/tema_9/pic/sam1.png?raw=true)
