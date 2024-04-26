# Запрос ввода непустой последовательности символов у пользователя
sequence = input("Введите непустую последовательность символов: ")

# Построение множества из встречающихся символов от 'A' до 'Z' и от '0' до '5'
desired_set = set(char for char in sequence if char.isalnum() and (char.isalpha() and char.upper() <= 'Z' or char.isdigit() and char <= '5'))

# Вывод множества
print("Множество символов от 'A' до 'Z' и цифр от '0' до '5':", desired_set)
