# Тема 6. Базовые коллекции: словари, кортежи
Отчет по Теме #6 выполнил: 
- Новицкий Тимофей Дмитриевич 
- АИС-23-1 

| Задание | Лаб_раб | Сам_раб | 
| ------ | ------ | ------ | 
| Задание 1 | + | + | 
| Задание 2 | + | + | 
| Задание 3 | + | + | 
| Задание 4 | + | + | 
| Задание 5 | + | + | 

Работу проверили: 
- Ротенштрайх Т.В. 

## Лабораторная работа №1 

```python
def classroom_access():
    request = int(input('Введите номер кабинета: '))
    dictionary = {
        101: {'key': 1234, 'access': True},
        102: {'key': 1337, 'access': True},
        103: {'key': 8943, 'access': True},
        104: {'key': 5555, 'access': False},
        None: {'key': None, 'access': False},
    }
    
    response = dictionary.get(request)
    if not response:
        response = dictionary[None]
    
    key = response.get('key')
    access = response.get('access')
    print(key, access)

classroom_access()
```
### Результат.

![Меню](https://github.com/timka5555timka-hub/programming-engeniring/blob/tema_6/pic/lab6_1.png?raw=true
)
вывод:
Программа демонстрирует работу словаря dict, заменяя длинные конструкции условий.
Если введённого кабинета нет, выводятся значения по умолчанию (None, False).

## Лабораторная работа №2 

```python
from pprint import pprint

def dict_maker(**kwargs):
    my_dict = {'first': 'so easy'}
    my_dict.update(kwargs)
    return my_dict

result = dict_maker(second=2, third='three', fourth=[1, 2, 3])
pprint(result)
```
### Результат.

![Меню](https://github.com/timka5555timka-hub/programming-engeniring/blob/tema_6/pic/lab6_2.png?raw=true
)
вывод:
Функция принимает любое количество именованных аргументов и добавляет их в словарь.
Используется **kwargs и метод .update(), что упрощает расширение словаря.

## Лабораторная работа №3 

```python
def string_to_tuple(text):
    char_tuple = tuple(text)
    char_list = list(char_tuple)
    return char_tuple, char_list

text = "Hello World!"
tuple_result, list_result = string_to_tuple(text)
print("Кортеж:", tuple_result)
print("Список:", list_result)
```
### Результат.

![Меню](https://github.com/timka5555timka-hub/programming-engeniring/blob/tema_6/pic/lab6_3.png?raw=true
)
вывод:
Программа показывает, как с помощью tuple() разбить строку посимвольно.
Каждый символ становится отдельным элементом кортежа (включая пробелы и знаки).

## Лабораторная работа №4 

```python
def person_info(data_tuple):
    name, age, job = data_tuple
    print(f"Имя: {name}")
    print(f"Возраст: {age}")
    print(f"Место работы: {job}")

person_data = ("Вовочка", 25, "Школа")
person_info(person_data)
```
### Результат.

![Меню](https://github.com/timka5555timka-hub/programming-engeniring/blob/tema_6/pic/lab6_4.png?raw=true
)
вывод:
Функция принимает кортеж с тремя элементами и красиво выводит информацию о человеке.
Пример использования распаковки кортежей в параметры.



## Лабораторная работа №5 

```python
def tuple_sort(tpl):
    for elm in tpl:
        if not isinstance(elm, int):
            return tpl
    return tuple(sorted(tpl))

print(tuple_sort((5, 5, 3, 1, 9)))
print(tuple_sort((5, 5, 2.1, '1', 9)))
```
### Результат.

![Меню](https://github.com/timka5555timka-hub/programming-engeniring/blob/tema_6/pic/lab6_5.png?raw=true
)
вывод:
Функция сортирует кортеж, если все элементы — числа.
В противном случае возвращает исходный.
Используется проверка isinstance() и функция sorted().




## Самостоятельная работа №1 

```python
def convert_sequence():
    data = input("Введите числа через пробел: ")
    numbers_list = [int(x) for x in data.split()]
    numbers_tuple = tuple(numbers_list)
    print("Список:", numbers_list)
    print("Кортеж:", numbers_tuple)

convert_sequence()
```
### Результат.

![Меню](https://github.com/timka5555timka-hub/programming-engeniring/blob/tema_6/pic/sam6_1.png?raw=true
)
вывод:
Программа принимает строку чисел, разделяет её на элементы и формирует из них список и кортеж.

## Самостоятельная работа №2 

```python
def remove_from_tuple(te, element):
    if element not in te:
        return te
    
    lst = list(te)
    lst.remove(element)
    return tuple(lst)

print(remove_from_tuple((1, 2, 3), 1))
print(remove_from_tuple((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
print(remove_from_tuple((2, 4, 6, 6, 4, 2), 9))
```
### Результат.

![Меню](https://github.com/timka5555timka-hub/programming-engeniring/blob/tema_6/pic/sam6_2.png?raw=true
)
вывод:
Программа создаёт изменённую копию кортежа без указанного значения.
Если элемент не найден — возвращается исходный кортеж.

## Самостоятельная работа №3 

```python
def count_digits(digit_string):
    if len(digit_string) < 15:
        return "Строка должна содержать минимум 15 символов"
    
    digit_count = {}
    for char in digit_string:
        digit = int(char)
        digit_count[digit] = digit_count.get(digit, 0) + 1
    
    frequent_three = sorted(digit_count.items(), key=lambda x: (-x[1], x[0]))[:3]
    
    result_dict = dict(sorted(frequent_three, key=lambda x: x[0]))
    
    print("Три самых частых числа:", result_dict)
    return result_dict

digits = "123456789012345678901234567890"
count_digits(digits)
```
### Результат.

![Меню](https://github.com/timka5555timka-hub/programming-engeniring/blob/tema_6/pic/sam6_3.png?raw=true
)
вывод:
Программа анализирует строку цифр, подсчитывает их количество
и выводит три самые часто встречающиеся цифры в виде словаря.



## Самстоятельная работа №4 

```python
def office_access(tpl, employee_id):
    if employee_id not in tpl:
        return ()
    
    indices = [i for i, x in enumerate(tpl) if x == employee_id]
    
    if len(indices) == 1:
        return tpl[indices[0]:]
    else:
        return tpl[indices[0]:indices[1] + 1]

print(office_access((1, 2, 3), 8))
print(office_access((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(office_access((1, 2, 8, 5, 1, 2, 9), 8))
```
### Результат.

![Меню](https://github.com/timka5555timka-hub/programming-engeniring/blob/tema_6/pic/sam6_4.png?raw=true
)
вывод:
Программа ищет указанное значение и возвращает часть кортежа от первого до второго появления,
либо до конца, если элемент встретился один раз.

## Самостоятельная работа №5 

```python
def employee_performance_system():
    """
    Система для расчета эффективности сотрудников и определения лучших
    """
    employees = [
        ("Иван Петров", (4.2, 4.5, 4.8, 4.1)),  # оценки по кварталам
        ("Мария Сидорова", (4.7, 4.9, 4.6, 4.8)),
        ("Алексей Козлов", (3.9, 4.2, 4.0, 4.3)),
        ("Елена Новикова", (4.8, 4.9, 4.7, 4.9)),
        ("Сергей Иванов", (4.0, 4.1, 3.8, 4.2))
    ]

    employee_performance = []
    for name, ratings in employees:
        average_rating = sum(ratings) / len(ratings)
        employee_performance.append((name, average_rating))

    employee_performance.sort(key=lambda x: x[1], reverse=True)

    print("Рейтинг сотрудников по эффективности:")
    for i, (name, rating) in enumerate(employee_performance, 1):
        print(f"{i}. {name}: {rating:.2f}")

    top_performers = [name for name, rating in employee_performance if rating > 4.5]
    print(f"\nЛучшие сотрудники (рейтинг > 4.5): {', '.join(top_performers)}")
    
    need_improvement = [name for name, rating in employee_performance if rating < 4.0]
    if need_improvement:
        print(f"Сотрудники, нуждающиеся в улучшении: {', '.join(need_improvement)}")
    
    return employee_performance


print("=== Тест 1 ===")
employee_performance_system()

print("\n=== Тест 2 ===")
test_employees = [("Тест1", (5.0, 5.0, 5.0)), ("Тест2", (3.0, 3.0, 3.0))]
result = [(name, sum(ratings)/len(ratings)) for name, ratings in test_employees]
print("Тестовые данные:", result)

print("\n=== Тест 3 ===")
empty_employees = []
print("Пустой список сотрудников:", empty_employees)

print("\n=== Тест 4 ===")
# Дополнительный тест с разным количеством оценок
mixed_employees = [
    ("Разработчик", (4.5, 4.7, 4.8)),
    ("Менеджер", (4.2, 4.3, 4.6, 4.4, 4.5)),
    ("Аналитик", (4.8,))
]
for name, ratings in mixed_employees:
    avg = sum(ratings) / len(ratings)
    print(f"{name}: {avg:.2f}")
```
### Результат.

![Меню](https://github.com/timka5555timka-hub/programming-engeniring/blob/tema_6/pic/sam6_5.png?raw=true
)


Общие выводы по теме:

Словари (dict):

Представляют собой коллекцию пар «ключ: значение».
Позволяют быстро находить данные по уникальному ключу.
Могут заменять громоздкие конструкции if/elif/else при обработке условий.
Поддерживают методы .get(), .update(), .keys(), .values(), .items() для удобной работы с данными.
Являются изменяемыми структурами, то есть можно добавлять, удалять и изменять элементы.


Кортежи (tuple):

Неизменяемые коллекции, упрощающие хранение данных, которые не должны меняться.
Обеспечивают более высокую производительность по сравнению со списками.
Поддерживают индексирование, срезы, объединение и распаковку значений.
Могут использоваться как ключи в словарях (так как они хешируемы).
Часто применяются для возврата нескольких значений из функций.


Работа с данными:

Преобразование строк в списки и кортежи позволяет гибко управлять вводом пользователя.
Использование кортежей и словарей делает код более читаемым и структурированным.
Словари идеально подходят для подсчёта и анализа данных (например, частоты символов или чисел).
Кортежи помогают безопасно хранить неизменяемые наборы значений (например, координаты, даты, записи сотрудников).


Архитектура и подход:
Создание функций с возвратом значений делает код повторно используемым.
Применение циклов и проверок типов (isinstance(), in, count()) обеспечивает корректность данных.
Работа с коллекциями развивает умение оптимально хранить и обрабатывать информацию.


Итог:

Освоение словарей и кортежей — это важный шаг в понимании структур данных в Python.
Они позволяют не только хранить информацию эффективно, но и организовывать логику программ более гибко и безопасно.
Знание этих коллекций формирует основу для работы с более сложными структурами — списками списков, множествами, базами данных и JSON-объектами.
