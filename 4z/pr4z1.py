# Запрос ввода дробного числа
number = float(input("Введите дробное число: "))

# Проверка условия и вывод соответствующего знака
if number > 0:
    print("+")
elif number < 0:
    print("-")
else:
    print("0")
