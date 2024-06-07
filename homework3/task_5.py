# Пользователь вводит положительное целое число N. Напишите программу, которая генерирует случайный пароль длины N, который содержит символы в
# верхнем и нижнем регистрах, числа, и специальные символы: , . * ^ _ ( ) [ ] { } ? ! @.
# В пароле должны присутствовать как минимум одна заглавная буква, одна маленькая буква, одна цифра, и один специальный символ.

import random
import string

length = int(input('Введите длину пароля: '))

lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits
special_characters = string.punctuation

all_characters = lowercase_letters + uppercase_letters + digits + special_characters

password = random.choice(lowercase_letters) + random.choice(uppercase_letters) + random.choice(digits) + random.choice(special_characters)
password += ''.join(random.choice(all_characters) for _ in range(length - 4))

password_list = list(password)
random.shuffle(password_list)
password = ''.join(password_list)

print(f"Сгенерированный пароль: {password}")   