n = int(input())
integer_list = [str(i) for i in range(1, n + 1)]
result = "".join(integer_list)
print(result)


def is_leap(year):
    leap = False

    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        leap = True

    return leap


year = int(input())


fig = str(input())
if fig == "треугольник":
    a, b, c = float(input()), float(input()), float(input())
    p = (a + b + c) / 2
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
elif fig == "прямоугольник":
    a, b = float(input()), float(input())
    print(a * b)
elif fig == "круг":
    r = int(input())
    print(3.14 * r**2)


a = int(input())
b = int(input())
c = int(input())
if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if b > c:
    b, c = c, b
print(a, b, c, sep="\n")


a = int(input())
if -15 < a <= 12 or 17 > a > 14 or a >= 19:
    print("True")
else:
    print("False")


a = int(input())
i = 0
while a != 0:
    i += a
    a = int(input())
print(i)

string = input("Введите строку: ")
string = string.replace(" ", "")
if string == string[::-1]:
    print("Введенная строка является палиндромом")
else:
    print("Введенная строка не является палиндромом")


# Является ли слово анаграммой
str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")
str1 = str1.lower().replace(" ", "")
str2 = str2.lower().replace(" ", "")
if sorted(str1) == sorted(str2):
    print("Введенные строки являются анаграммами")
else:
    print("Введенные строки не являются анаграммами")


# Сумма чисел от 1 до N
num = int(input("Введите число: "))
sum_numbers = 0
for i in range(1, num + 1):
    sum_numbers += i
print(f"Сумма всех чисел от 1 до {num} равна {sum_numbers}")
