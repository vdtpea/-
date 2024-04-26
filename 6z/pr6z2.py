# Начальное количество амеб
amoeba_count = 1

# Время в часах
hours = 3

# Ввод времени
time_period = int(input("Введите количество часов: "))

# Цикл для определения количества амеб через указанный период времени
for i in range(hours, time_period + 1, hours):
    # Каждые 3 часа амеба делится на 2
    amoeba_count *= 2
    print(f"Через {i} часов будет {amoeba_count} {'амеба' if amoeba_count == 1 else 'амебы'}")
