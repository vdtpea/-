def filter_even_above_10(numbers):
    result = [num for num in numbers if num % 2 == 0 and num > 10]
    return result

numbers = input("Введите список чисел через пробел: ").split()
numbers = [int(num) for num in numbers]

filtered_numbers = filter_even_above_10(numbers)

print(f"filtered_numbers: {filtered_numbers}")
