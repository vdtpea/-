# Ввод цены пирожка (рубли и копейки)
price_rubles = int(input("Введите стоимость пирожка в рублях: "))
price_kopeks = int(input("Введите стоимость пирожка в копейках: "))

# Ввод количества пирожков
quantity = int(input("Введите количество пирожков: "))

# Вычисление общей суммы
total_price_kopeks = price_rubles * 100 + price_kopeks
total_price = total_price_kopeks * quantity

# Разделение общей суммы на рубли и копейки
total_rubles = total_price // 100
total_kopeks = total_price % 100

# Вывод общей суммы
print(f"К оплате: {total_rubles} рублей {total_kopeks} копеек")
