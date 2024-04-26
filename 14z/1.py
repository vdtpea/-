def find_phone_number(phone_book, query_name):
    for entry in phone_book:
        if entry[1] == query_name:
            return entry[0]
    return "Нет в телефонной книге"

# Ввод количества номеров телефонов
n = int(input("Введите количество номеров телефонов: "))

# Ввод имен и номеров телефонов
phone_book = []
for _ in range(n):
    phone, name = input().split()
    phone_book.append((phone, name))

# Запрос имени для поиска номера телефона
query_name = input("Введите имя для поиска номера телефона: ")

# Поиск номера телефона и вывод результата
result = find_phone_number(phone_book, query_name)
print(result)
