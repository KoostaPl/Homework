# Пользователь вводит слово. Напишите программу, которая проверяет, является ли оно палиндромом (читается одинаково слева-направо и справа-налево).

word = input("Введите слово: ").lower()
print(word == word[::-1])