numbers = [float(input(f"Введите {i+1}-е число: ")) for i in range(15)]

max_number = max(numbers)
max_index = numbers.index(max_number)

numbers[-1], numbers[max_index] = numbers[max_index], numbers[-1]

print("Список из 15 вещественных чисел:", numbers)
print("Наибольший элемент:", max_number)
