M = int(input("Введите значение количества строк: "))
N = int(input("Введите значиние количества столбцов: "))

matrix1 = []
for i in range(M):
    row = []
    for j in range(N):
        value = int(input(f"Введите значения [{i}][{j}] для первой матрицы: "))
        row.append(value)
    matrix1.append(row)

matrix2 = []
for i in range(M):
    row = []
    for j in range(N):
        value = int(input(f"Введите значения [{i}][{j}] для второй матрицы: "))
        row.append(value)
    matrix2.append(row)

sum_matrix = []
for i in range(M):
    row = []
    for j in range(N):
        value = matrix1[i][j] + matrix2[i][j]
        row.append(value)
    sum_matrix.append(row)
print(f"Значение первой матрицы: {matrix1}")
print(f"Значение второй матрицы: {matrix2}")
print(f"Сумма матриц равняется: {sum_matrix}")