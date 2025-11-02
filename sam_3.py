# Базовый класс Book (Книга)
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
