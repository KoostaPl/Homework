# Пользователь вводит положительное целое число N. Напишите программу,
# которая считает факториал N.


num = int(input("Введите число: "))
fuct = 1 
for i in range(1, num + 1):
    fuct *= i
print(f"Факториал числа {num} равен {fuct}")