def find_specialty(dictionary, query_group):
    for specialty, groups in dictionary.items():
        if query_group in groups:
            return specialty
    return ""

# Ввод количества специальностей
n = int(input("Введите количество специальностей: "))

# Создание словаря специальностей
specialties = {}
for _ in range(n):
    specialty, groups_str = input().split(" - ")
    groups = groups_str.split(", ")
    for group in groups:
        if group not in specialties:
            specialties[group] = []
        specialties[group].append(specialty)

# Запрос номера группы для поиска специальности
query_group = input("Введите номер группы: ")

# Поиск специальности по номеру группы и вывод результата
result_specialty = find_specialty(specialties, query_group)
print("result_specialty:", result_specialty)
