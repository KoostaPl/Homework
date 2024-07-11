# Пользователь вводит 2 набора чисел. Выведите на экран:
# 1. Числа, которые присутствуют в обоих наборах одновременно.
# 2. Числа из первого набора, которые отсутствуют во втором, и наоборот.
# 3. Числа из обоих наборов, за исключением чисел, найденных в пункте 1.


first_numbers = set(input("Введите числа первого набора через пробел: ").split())
second_numbers = set(input("Введите числа второго набора через пробел: ").split())

both_numbers = first_numbers.intersection(second_numbers)
print(
    "Числа, которые присутствуют в обоих наборах одновременно:", ", ".join(both_numbers)
)

first_not_in_second = first_numbers.difference(second_numbers)
second_not_in_first = second_numbers.difference(first_numbers)
print(
    "Числа из первого набора, которые отсутствуют во втором:",
    ", ".join(first_not_in_second),
)
print(
    "Числа из второго набора, которые отсутствуют в первом:",
    ", ".join(second_not_in_first),
)

not_both_numbers = first_numbers.symmetric_difference(second_numbers) - both_numbers
print(
    "Числа из обоих наборов, за исключением чисел, найденных в пункте 1:",
    ", ".join(not_both_numbers),
)
