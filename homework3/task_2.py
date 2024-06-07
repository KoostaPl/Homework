# Пользователь вводит положительное целое число N. Напишите программу,
# которая проверяет, является ли число N простым и выводит результат.

num = int(input("Введите число: "))

if num <= 1:
    print("Число должно быть больше 1")
else:
    is_not_prime = False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_not_prime = True
            break

    if is_not_prime:
        print("Составное число")
    else:
        print("Простое число")
