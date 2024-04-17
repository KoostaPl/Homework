# Пользователь вводит список чисел. Числа вводятся через пробел, могут быть
# как целые, так и с плавающей точкой. Выведите на экран:
# 1. Уникальные числа.
# 2. Повторяющиеся числа.
# 3. Четные и нечетные чисел.
# 4. Отрицательные чисел.
# 5. Числа с плавающей точкой.
# 6. Сумму всех чисел, кратных 5.
# 7. Самое большое число.
# 8. Самое маленькое число.

numbers = input("Введите список чисел через пробел: ")
numbers_list = numbers.split()

unique_numbers = set()
repeated_numbers = []
even_numbers = []
odd_numbers = []
negative_numbers = []
float_numbers = []
multiples_of_5 = []

for number in numbers_list:
    if number not in unique_numbers:
        unique_numbers.add(number)
    else:
        repeated_numbers.append(number)

    if float(number) % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

    if float(number) < 0:
        negative_numbers.append(number)

    if '.' in number:
        float_numbers.append(number)

    if float(number) % 5 == 0:
        multiples_of_5.append(number)

print("Уникальные числа:", ' '.join(unique_numbers))
print("Повторяющиеся числа:", ' '.join(repeated_numbers))
print("Четные числа:", ' '.join(even_numbers))
print("Нечетные числа:", ' '.join(odd_numbers))
print("Отрицательные числа:", ' '.join(negative_numbers))
print("Числа с плавающей точкой:", ' '.join(float_numbers))
print("Сумма всех чисел, кратных 5:", sum(map(float, multiples_of_5)))
print("Максимальное число из списка:", max(numbers_list))
print("Минимальное число из списка:", min(numbers_list))