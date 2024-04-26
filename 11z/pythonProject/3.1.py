
numbers = [int(input(f"Введите {i+1}-е число: ")) for i in range(20)]


max_number = max(numbers)
max_index = numbers.index(max_number)

numbers[0], numbers[max_index] = numbers[max_index], numbers[0]

print("Список из 20 целых чисел:", numbers)
print("Наибольший элемент:", max_number)
