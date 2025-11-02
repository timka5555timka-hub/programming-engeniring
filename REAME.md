# Тема 8. Работа с файлами (ввод, вывод)
Отчёт по Теме 8 выполнил:
- Новицкий Тимофей Дмитриевич
- Группа: АИС-23-1
  
| Задание     | Лаб_Раб     | Сам_Раб     | 
| ----------- | ----------- | ----------- |
|  Задание 1  |     +       |    +       |
|  Задание 2  |     +       |    +       |
|  Задание 3  |     +       |    +       |
|  Задание 4  |     +       |    +       |
|  Задание 5  |     +       |    +       |

# Лабораторные работа 1
## Создание класса "Car" с атрибутами производитель и модель

```
# Определяем класс Car (автомобиль)
class Car:
    # Конструктор класса - метод, который вызывается при создании объекта
    # self - ссылка на текущий объект
    # make - производитель автомобиля
    # model - модель автомобиля
    def __init__(self, make, model):
        # Сохраняем производителя в атрибут объекта
        self.make = make
        # Сохраняем модель в атрибут объекта
        self.model = model

# Создаем объект класса Car с конкретными значениями
# my_car - это экземпляр класса Car
my_car = Car("Toyota", "Corolla")
```

# Лабораторные работа 2
## Добавление атрибутов и методов класса, машина "едет"

```python
# Определяем класс Car (автомобиль)
class Car:
    # Конструктор класса - инициализирует объект при создании
    def __init__(self, make, model):
        # Атрибут производителя автомобиля
        self.make = make
        # Атрибут модели автомобиля
        self.model = model

    # Метод для имитации движения автомобиля
    # Выводит информацию о том, что машина едет
    def drive(self):
        print(f"Driving the {self.make} {self.model}")

# Создаем объект класса Car
my_car = Car("Toyota", "Corolla")

# Вызываем метод drive() для объекта my_car
# Машина "поедет" - выведется сообщение в консоль
my_car.drive()
```




# Лабораторные работа 3
## Создание класса ElectricCar с наследованием от класса Car

```python

# Базовый класс Car (автомобиль)
class Car:
    # Конструктор базового класса
    def __init__(self, make, model):
        self.make = make
        self.model = model

    # Метод для движения автомобиля
    def drive(self):
        print(f"Driving the {self.make} {self.model}")


# Класс ElectricCar наследуется от класса Car
# Использует все методы и атрибуты родительского класса
class ElectricCar(Car):
    # Конструктор класса ElectricCar
    # Принимает дополнительный параметр battery_capacity (емкость батареи)
    def __init__(self, make, model, battery_capacity):
        # Вызываем конструктор родительского класса Car
        # super() - обращение к родительскому классу
        super().__init__(make, model)
        # Добавляем новый атрибут - емкость батареи
        self.battery_capacity = battery_capacity

    # Новый метод для зарядки электромобиля
    def charge(self):
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")


# Создаем объект класса ElectricCar
my_electric_car = ElectricCar("Tesla", "Model S", 75)

# Машина едет (используется унаследованный метод drive)
my_electric_car.drive()

# Машина заряжается (используется новый метод charge)
my_electric_car.charge()
```




# Лабораторные работа 4
## Реализация инкапсуляции с защищенными и приватными атрибутами

```python
# Класс Car с инкапсуляцией
class Car:
    # Конструктор класса
    def __init__(self, make, model):
        # Защищенный атрибут (одно подчеркивание)
        # Условно приватный - доступен, но не рекомендуется использовать извне
        self._make = make

        # Приватный атрибут (два подчеркивания)
        # Строго приватный - Python изменяет имя (name mangling)
        self.__model = model

    # Метод для движения автомобиля
    # Использует защищенный и приватный атрибуты внутри класса
    def drive(self):
        print(f"Driving the {self._make} {self.__model}")


# Создаем объект класса Car
my_car = Car("Toyota", "Corolla")

# Доступ к защищенному атрибуту (работает, но не рекомендуется)
print(my_car._make)

# Попытка доступа к приватному атрибуту напрямую вызовет ошибку
# print(my_car.__model)  # Ошибка! Приватный атрибут не доступен

# Вызываем метод drive() - внутри класса доступны все атрибуты
my_car.drive()
```



# Лабораторные работа 5
## Реализация полиморфизма с классами Shape, Rectangle и Circle
```python
# Базовый (общий) класс Shape (фигура)
class Shape:
    # Базовый метод для вычисления площади
    # В базовом классе этот метод возвращает 0 (заглушка)
    def area(self):
        return 0.0


# Класс Rectangle (прямоугольник) наследуется от Shape
class Rectangle(Shape):
    # Конструктор принимает ширину и высоту
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Переопределяем метод area для прямоугольника
    # Площадь прямоугольника = ширина * высота

   def area(self):
        return self.width * self.height


# Класс Circle (круг) наследуется от Shape
class Circle(Shape):
    # Конструктор принимает радиус
    def __init__(self, radius):
        self.radius = radius

    # Переопределяем метод area для круга
    # Площадь круга = π * радиус²
    def area(self):
        pi = 3.14
        return pi * self.radius * self.radius


# Создаем массив с фигурами
shapes = [
    Rectangle(5, 10),    # Прямоугольник 5x10
    Circle(3)            # Круг с радиусом 3
]

# Проходим по массиву и выводим площади фигур
# Полиморфизм: метод area() вызывается для разных типов объектов
for shape in shapes:
    print(shape.area())
```



# Самостоятельная работа 1
## Создание собственного класса и объекта

```python
# Создаем класс Book (Книга)
class Book:
    # Конструктор класса - инициализирует объект при создании
    # title - название книги
    # author - автор книги
    def __init__(self, title, author):
        self.title = title
        self.author = author


# Создаем объект класса Book
my_book = Book("Мастер и Маргарита", "Михаил Булгаков")

# Выводим информацию о книге
print(f"Название: {my_book.title}")
print(f"Автор: {my_book.author}")

```



# Самостоятельная работа 2
## Добавление атрибутов и методов для класса Book
```python
# Класс Book (Книга)
# Класс Book (Книга)
class Book:
    # Конструктор класса
    # Добавляем новый атрибут - год издания
    def __init__(self, title, author, year):
        self.title = title      # Название книги
        self.author = author    # Автор книги
        self.year = year        # Год издания

    # Метод для отображения информации о книге
    def display_info(self):
        print(f"Книга: '{self.title}' ({self.year})")
        print(f"Автор: {self.author}")

    # Метод для проверки, является ли книга классической (старше 50 лет)
    def is_classic(self):
        current_year = 2024
        if current_year - self.year > 50:
            print(f"'{self.title}' - классическое произведение")
        else:
            print(f"'{self.title}' - современное произведение")


# Создаем объект класса Book
my_book = Book("Война и мир", "Лев Толстой", 1869)

# Вызываем методы объекта
my_book.display_info()
my_book.is_classic()
```





# Самостоятельная работа 3
## Реализация наследования для класса Book

```python
#Базовый класс Book (Книга)
class Book:
    # Конструктор базового класса
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    # Метод для отображения информации о книге
    def display_info(self):
        print(f"Книга: '{self.title}' ({self.year})")
        print(f"Автор: {self.author}")


# Класс EBook наследуется от класса Book
# Представляет электронную книгу с дополнительными свойствами
class EBook(Book):
    # Конструктор класса EBook
    # Добавляем параметр file_size (размер файла в МБ)
    def __init__(self, title, author, year, file_size):
        # Вызываем конструктор родительского класса
        super().__init__(title, author, year)
        # Добавляем новый атрибут - размер файла
        self.file_size = file_size

    # Новый метод для скачивания электронной книги
    def download(self):
        print(f"Скачивание '{self.title}' ({self.file_size} МБ)...")
        print("Загрузка завершена!")


# Создаем объект класса EBook
my_ebook = EBook("Python для начинающих", "Марк Лутц", 2020, 5.2)

# Используем унаследованный метод display_info
my_ebook.display_info()

# Используем новый метод download
my_ebook.download()
```




# Самостоятельная работа 4
## Реализация инкапсуляции для класса Book
```python
# Класс Book с инкапсуляцией
class Book:
    # Конструктор класса
    def __init__(self, title, author, year):
        # Защищенный атрибут (одно подчеркивание)
        # Название книги - доступно, но не рекомендуется обращаться извне
        self._title = title

        # Приватный атрибут (два подчеркивания)
        # Автор книги - строго приватный, доступен только внутри класса
        self.__author = author

        # Публичный атрибут - год издания
        self.year = year

    # Публичный метод для отображения информации
    # Внутри метода доступны все атрибуты класса
    def display_info(self):
        print(f"Книга: '{self._title}' ({self.year})")
        print(f"Автор: {self.__author}")

    # Геттер для получения приватного атрибута __author
    def get_author(self):
        return self.__author


# Создаем объект класса Book
my_book = Book("Преступление и наказание", "Федор Достоевский", 1866)

# Доступ к защищенному атрибуту (работает, но не рекомендуется)
print(f"Защищенный атрибут _title: {my_book._title}")

# Доступ к публичному атрибуту
print(f"Публичный атрибут year: {my_book.year}")

# Попытка доступа к приватному атрибуту напрямую вызовет ошибку
# print(my_book.__author)  # Ошибка!

# Правильный способ - через геттер
print(f"Приватный атрибут через геттер: {my_book.get_author()}")

# Вызываем метод display_info
my_book.display_info()

```



# Самостоятельная работа 5
## Реализация полиморфизма с классами Animal, Dog и Cat

```python
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
```

