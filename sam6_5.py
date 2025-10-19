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
