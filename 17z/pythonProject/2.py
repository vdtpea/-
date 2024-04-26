import random
def generate_exam_schedule(num_exams, subjects):
    days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]
    exam_times = ["9:00", "11:00", "14:00", "16:00"]

    for i in range(num_exams):
        day = random.choice(days_of_week)
        time = random.choice(exam_times)
        lucky_number = random.randint(1, 100)

        print(f"Экзамен по {subjects[i]}:")
        print(f"День недели: {day}")
        print(f"Время: {time}")
        print(f"Счастливый номер билета: {lucky_number}")
        print()


# Ввод данных от пользователя
num_exams = int(input("Введите количество экзаменов: "))
subjects = input("Введите наименования дисциплин через запятую и пробел: ").split(", ")

generate_exam_schedule(num_exams, subjects)
