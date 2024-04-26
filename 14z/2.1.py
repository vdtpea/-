def find_students_by_specialty(students, query_specialty):
    students_list = [student[0] for student in students if student[1] == query_specialty]
    if students_list:
        return ", ".join(students_list)
    else:
        return "Проверьте запрос"

# Ввод количества студентов
n = int(input("Введите количество студентов: "))

# Ввод информации о студентах
students = []
for _ in range(n):
    last_name, specialty, group = input().split()
    students.append((last_name, specialty, group))

# Запрос названия специальности
query_specialty = input("Введите название специальности: ")

# Поиск студентов по специальности и вывод результата
result_students = find_students_by_specialty(students, query_specialty)
print("result_students:", result_students)
