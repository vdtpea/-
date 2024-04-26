
numbers = [int(input(f"Введите {i+1}-е число: ")) for i in range(10)]
min_number = min(numbers)
min_index = numbers.index(min_number)
numbers[-1], numbers[min_index] = numbers[min_index], numbers[-1]
print("Список из 10 целых чисел:", numbers)
print("Наименьший элемент:", min_number)
