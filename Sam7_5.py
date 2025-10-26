import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%"
    return ''.join(random.choice(chars) for _ in range(length))

with open("passwords.txt", "w", encoding="utf-8") as file:
    for i in range(5):
        file.write(f"Пароль {i+1}: {generate_password()}\n")

print("Пароли сохранены в файл 'passwords.txt'.")
