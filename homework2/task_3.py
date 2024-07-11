first_numbers = set(input("Введите числа первого набора: ").split())
second_numbers = set(input("Введите числа второго набора: ").split())

both_numbers = first_numbers.intersection(second_numbers)
print("Числа, которые в наборах одновременно:", ", ".join(both_numbers))
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

not_both_numbers = (first_numbers ^ second_numbers) - both_numbers
print(
    "Числа наборов, за исключением чисел, найденных в пункте 1:",
    ", ".join(not_both_numbers),
)
