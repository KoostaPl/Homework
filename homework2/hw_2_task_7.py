# Пользователь вводит строку. Напишите программу, которая сжимает строку
# следующим образом: если символ X повторяется N раз, то итоговая строка
# должна содержать XN.

s = input("Введите строку: ")
result = ""
counter = 0
current_char = s[0]

for char in s:
    if char == current_char:
        counter += 1
    else:
        result += current_char + str(counter)
        counter = 1
        current_char = char

result += current_char + str(counter)

print(result)
