from datetime import datetime, timedelta


def is_happy_date(date):
    return date.day % 4 != 0 and date.weekday() != 0


def find_happy_dates(start_date, n):
    happy_dates = []
    current_date = start_date
    while len(happy_dates) < 3:
        if is_happy_date(current_date):
            happy_dates.append(current_date)
        current_date += timedelta(days=n)

    return happy_dates


# Ввод данных от пользователя
start_date_str = input("Введите исходную дату в формате YYYY/MM/DD: ")
n = int(input("Введите число n: "))

start_date = datetime.strptime(start_date_str, "%Y/%m/%d")
happy_dates = find_happy_dates(start_date, n)

for date in happy_dates:
    print(date.strftime("%d %B, %A"))
