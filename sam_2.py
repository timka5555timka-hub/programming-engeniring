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
