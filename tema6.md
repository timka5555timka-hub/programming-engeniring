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

![Меню](<img width="424" height="205" alt="image" src="https://github.com/user-attachments/assets/74882bae-eace-4919-b351-13f344f5908d" />
)


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

![Меню](<img width="744" height="95" alt="image" src="https://github.com/user-attachments/assets/157d6286-6769-49dd-bf22-60e8e3d9f510" />
)


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

![Меню](<img width="710" height="123" alt="image" src="https://github.com/user-attachments/assets/34c6e702-54a2-4677-8f69-0109b0bf29d9" />
)


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

![Меню](<img width="292" height="160" alt="image" src="https://github.com/user-attachments/assets/0cccd3a3-4264-49f3-a424-b95cf134d525" />
)


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

![Меню](<img width="251" height="125" alt="image" src="https://github.com/user-attachments/assets/a3d62b42-a9b6-40ff-8610-3969a580efc5" />
)

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

![Меню](<img width="624" height="107" alt="image" src="https://github.com/user-attachments/assets/7ada0369-1f52-4473-ad0a-19fd6f6abef2" />
)


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

![Меню](<img width="414" height="149" alt="image" src="https://github.com/user-attachments/assets/878b8889-8037-453b-a998-2e79009c34de" />
)


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

![Меню](<img width="452" height="107" alt="image" src="https://github.com/user-attachments/assets/e88efbc5-16c8-4f4c-b268-fe72ca437b41" />
)


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

![Меню](<img width="252" height="179" alt="image" src="https://github.com/user-attachments/assets/8a3bec3a-507f-4b0e-991d-a02152310355" />
)


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

![Меню](<img width="689" height="303" alt="image" src="https://github.com/user-attachments/assets/7e02d671-ba01-4110-b5f2-e3ee70ce11c7" />
)
