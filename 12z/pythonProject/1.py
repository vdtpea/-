def print_matrix_in_snake_order(matrix):
    for i, row in enumerate(matrix):
        if i % 2 == 0:
            print(*row)
        else:
            print(*row[::-1])

# Пример матрицы 4x4
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print("Исходная матрица:")
for row in matrix:
    print(*row)

print("\nЭлементы матрицы в змеевидном порядке:")
print_matrix_in_snake_order(matrix)
