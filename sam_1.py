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
