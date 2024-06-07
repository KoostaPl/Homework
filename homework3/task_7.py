# Решите предыдущую задачу не используя проход по списку в цикле.


def binary_search(numbers, num):
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == num:
            return mid
        elif numbers[mid] < num:
            low = mid + 1
        else:
            high = mid - 1

    return -1

user_input = input("Введите числа, разделенные пробелом: ").split()
numbers = [int(i) for i in user_input]

num = int(input("Введите число для нахождения индекса: "))
numbers.sort()
index = binary_search(numbers, num)
print(f"Индекс искомого числа из списка: {index}")