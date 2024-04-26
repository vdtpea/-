from datetime import datetime, timedelta
def exam_date(days_until_exam):
    current_date = datetime.now()
    exam_date = current_date + timedelta(days=days_until_exam)

    return exam_date.strftime("%d.%m")
# Ввод данных от пользователя
days_until_exam = int(input("Введите количество дней до экзамена: "))

exam_day = exam_date(days_until_exam)
print(f"Экзамен состоится {exam_day}")
