a, b, c = int(input('Введите угол первой стороны треугольника: ')), int(input('Введите угол второй стороны треугольника: ')), int(input('Введите угол третьей стороны треугольника: '))
if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2 # Полупериметр
    S = (p*(p - a)*(p - b)*(p - c))**0.5 # Формула Герона
    print("Треугольник существует, его площадь равна:", S)
else:
    print('Треугольник не существует. Проверьте введенные данные.')