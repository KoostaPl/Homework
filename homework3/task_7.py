# Решите предыдущую задачу не используя проход по списку в цикле.


def find_index(user_input_nums, num, index=0):
    if not user_input_nums:  
        return -1
    if user_input_nums[0] == num: 
        return index
    return find_index(user_input_nums[1:], num, index + 1) 

user_input_nums = sorted(list(map(int, input("Введите числа, разделенные пробелом: ").split())))
num = int(input("Введите число для нахождения индекса: "))

print(find_index(user_input_nums, num))