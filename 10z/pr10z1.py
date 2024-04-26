# Ввод первого множества чисел
set1_input = input("Введите элементы первого множества через пробел: ")

# Преобразование ввода в множество чисел
set1 = set(map(int, set1_input.split()))

# Ввод второго множества чисел
set2_input = input("Введите элементы второго множества через пробел: ")

# Преобразование ввода в множество чисел
set2 = set(map(int, set2_input.split()))

# Нахождение всех различных чисел в обоих множествах
different_numbers = set1.union(set2)

# Нахождение пересечения множеств для чисел, входящих как в первое, так и во второе множество
common_numbers = sorted(set1.intersection(set2))

# Вывод результатов
print("Различные числа в обоих множествах:", different_numbers)
print("Числа, входящие как в первое, так и во второе множество в порядке возрастания:", common_numbers)
