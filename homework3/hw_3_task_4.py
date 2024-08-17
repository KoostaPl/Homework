M = int(input("Введите значение количества строк: "))
N = int(input("Введите значение количества столбцов: "))

matrix1 = []
matrix2 = []


def matrix(matrix):
    for i in range(M):
        row = []
        for j in range(N):
            value = int(input(f"Введите значения [{i}][{j}] для матрицы: "))
            row.append(value)
        matrix.append(row)


matrix(matrix1)
matrix(matrix2)


def sum_of_matrix(matrix1, matrix2):
    sum_matrix = []
    for i in range(M):
        row = []
        for j in range(N):
            value = matrix1[i][j] + matrix2[i][j]
            row.append(value)
        sum_matrix.append(row)
    return sum_matrix


result = sum_of_matrix(matrix1, matrix2)
print(f"Значение первой матрицы: {matrix1}")
print(f"Значение второй матрицы: {matrix2}")
print(f"Сумма матриц равняется: {result}")
