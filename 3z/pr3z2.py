# Запрос ввода трех действительных чисел
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))

# Проверка и возведение чисел в квадрат или в четвертую степень
if a >= 0:
    a_square = a ** 2
    print(f"Квадрат числа a: {a_square}")
else:
    a_power4 = a ** 4
    print(f"Четвертая степень числа a: {a_power4}")

if b >= 0:
    b_square = b ** 2
    print(f"Квадрат числа b: {b_square}")
else:
    b_power4 = b ** 4
    print(f"Четвертая степень числа b: {b_power4}")

if c >= 0:
    c_square = c ** 2
    print(f"Квадрат числа c: {c_square}")
else:
    c_power4 = c ** 4
    print(f"Четвертая степень числа c: {c_power4}")
