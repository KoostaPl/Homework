# Решите предыдущую задачу не используя проход по списку в цикле.


user_input_nums = sorted(list(map(int, input("Введите числа, разделенные пробелом: ").split())))
num = int(input("Введите число для нахождения индекса: "))
if num in user_input_nums:
    print(f"Индексом искомого числа {num} является {user_input_nums.index(num)}")
else:
    print(-1)
