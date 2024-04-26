def calculate_average(input_list):
    if len(input_list) == 0:
        print("0")
    else:
        average = sum(input_list) / len(input_list)
        print(f"average: {average}")

input_list = []
n = int(input("Введите количество элементов в списке: "))
for i in range(n):
    element = int(input(f"Введите элемент {i + 1}: "))
    input_list.append(element)

calculate_average(input_list)
