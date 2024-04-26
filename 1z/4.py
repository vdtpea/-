import random

# Генерация случайного трехзначного числа
random_number = random.randint(100, 999)

# Разделение числа на отдельные цифры
digit1 = random_number // 100
digit2 = (random_number // 10) % 10
digit3 = random_number % 10

# Вывод отдельных цифр через запятую
print(f"Отдельные цифры случайного трехзначного числа {random_number}: {digit1}, {digit2}, {digit3}")
