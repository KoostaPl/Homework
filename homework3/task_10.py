
import random

N = random.randint(0, 100)
A = 5
print(N)
for i in range(A):
    num = int(input("Угадайте число: "))
    if num > N:
        print(f"Число {num} больше искомого. Всего попыток: {A - 1}")
        A -= 1
    elif num < N:
        print(f"Число {num} меньше искомого. Всего попыток: {A - 1}")
        A -= 1
    else:
        print(f"Поздравляю, Вы угадали число {num}!")
        break

if A == 0:
    print("К сожалению Ваши попытки закончились:(")
