def sum_columns(matrix):
    sums = [0] * len(matrix[0])  # Создаем список для сумм столбцов, заполненный нулями

    for row in matrix:
        for j, value in enumerate(row):
            sums[j] += value  # Добавляем значение к сумме соответствующего столбца

    return sums


# Ввод матрицы
rows = int(input("Введите количество строк в матрице: "))
columns = int(input("Введите количество столбцов в матрице: "))

matrix = []
print("Введите элементы матрицы:")
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Вывод исходной матрицы
print("\nИсходная матрица:")
for row in matrix:
    print(*row)

# Вычисление суммы элементов каждого столбца
column_sums = sum_columns(matrix)

# Вывод сумм элементов каждого столбца
print("\nСуммы элементов каждого столбца:")
for i, column_sum in enumerate(column_sums):
    print(f"Сумма элементов столбца {i + 1}: {column_sum}")
