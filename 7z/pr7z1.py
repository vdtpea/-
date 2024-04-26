# Внешний цикл для чисел от 1 до 9
for i in range(1, 10):
    row = ""  # Переменная для хранения строки таблицы
    # Внутренний цикл для чисел от 1 до 9
    for j in range(1, 10):
        # Добавление результата умножения в строку
        row += f"{i * j:2} "  # :2 задает ширину поля для каждого числа
    print(row)  # Вывод строки таблицы
