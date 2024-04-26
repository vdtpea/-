def sum_rows(matrix):
    sums = []

    for row in matrix:
        row_sum = sum(row)
        sums.append(row_sum)

    return sums
rows = int(input("Введите количество строк в матрице: "))
columns = int(input("Введите количество столбцов в матрице: "))

matrix = []
print("Введите элементы матрицы:")
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)
print("\nИсходная матрица:")
for row in matrix:
    print(*row)
row_sums = sum_rows(matrix)
print("\nСуммы элементов каждой строки:")
for i, row_sum in enumerate(row_sums):
    print(f"Сумма элементов строки {i + 1}: {row_sum}")
