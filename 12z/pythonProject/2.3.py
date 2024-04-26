def sum_positive_below_diagonal(matrix):
    n = len(matrix)
    total_sum = 0

    for i in range(n):
        for j in range(i+1, n):
            if matrix[i][j] > 0:
                total_sum += matrix[i][j]

    return total_sum
n = int(input("Введите размер квадратной матрицы: "))

matrix = []
print("Введите элементы матрицы:")
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
print("\nИсходная матрица:")
for row in matrix:
    print(*row)
total_positive_sum = sum_positive_below_diagonal(matrix)
print(f"\nСумма положительных элементов под главной диагональю и на ней: {total_positive_sum}")
