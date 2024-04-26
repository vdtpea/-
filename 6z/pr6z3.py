# Инициализация суммы и произведения
sum_result = 0
product_result = 1

# Количество чисел
n = 15

# Цикл для ввода и вычисления суммы и произведения
for _ in range(n):
    num = float(input("Введите число: "))
    sum_result += num
    product_result *= num

# Вывод результатов
print(f"Сумма введенных чисел: {sum_result}")
print(f"Произведение введенных чисел: {product_result}")
