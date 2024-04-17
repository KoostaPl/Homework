# Пользователь вводит положительное целое число N. Напишите программу, которая генерирует случайный пароль длины N, который содержит символы в
# верхнем и нижнем регистрах, числа, и специальные символы: , . * ^ _ ( ) [ ] { } ? ! @.
# В пароле должны присутствовать как минимум одна заглавная буква, одна маленькая буква, одна цифра, и один специальный символ.

import random
lenght = int(input('Enter the length of your password: '))
random_stirng = ''.join(chr(random.randint(33,126)) for i in range(lenght))
print(f"Your generated pawword is: {random_stirng}")
