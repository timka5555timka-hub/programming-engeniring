def person_info(data_tuple):
    name, age, job = data_tuple
    print(f"Имя: {name}")
    print(f"Возраст: {age}")
    print(f"Место работы: {job}")

person_data = ("Вовочка", 25, "Школа")
person_info(person_data)
