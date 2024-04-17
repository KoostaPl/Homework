#Пользователь вводит 2 набора чисел. Выведите на экран:
#1. Числа, которые присутствуют в обоих наборах одновременно.
#2. Числа из первого набора, которые отсутствуют во втором, и наоборот.
#3. Числа из обоих наборов, за исключением чисел, найденных в пункте 1.


first_numbers = input("Введите список чисел через пробел: ")
second_numbers = input("Введите список чисел через пробел: ")
first_numbers_list = first_numbers.split()
second_numbers_list = second_numbers.split()
bothnumbers = []
firsnotinsecond = set()
secondnotinfirst = set()
notbothnumbers = set()

for num in first_numbers_list:
    for num1 in second_numbers_list:
        if num == num1:
            bothnumbers.append(num1)       
        if num not in second_numbers_list:
            firsnotinsecond.add(num)
            notbothnumbers.add(num)
        if num1 not in first_numbers_list:
            secondnotinfirst.add(num1) 
            notbothnumbers.add(num1)

print("Повторяющиеся цифры обоих списков:", ' '.join(bothnumbers))
print("Цифры из первого списка отсутствующие во втором списке:", ' '.join(firsnotinsecond))
print("Цифры из второго списка отсутствующие в первом списке:", ' '.join(secondnotinfirst))
print("Числа из обоих наборов, за исключением чисел, найденных в пункте 1:", ' '.join(notbothnumbers))
