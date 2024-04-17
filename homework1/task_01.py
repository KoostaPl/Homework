# ДЗ из лекции 2
val = int(input('Введите число: '))
if val % 17:
    if val % 2:
        print('Число:', 'odd')
    else:
        print('Число:','even')
else:
    print('Число:','odd')