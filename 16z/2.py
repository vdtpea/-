def filter_and_sum(lst, condition_func):
    filtered_elements = []
    sum_of_others = 0

    for num in lst:
        if condition_func(num):
            filtered_elements.append(num)
        else:
            sum_of_others += num

    return sum_of_others


def is_negative(num):
    return num < 0


def sum_of_cubed_negatives():
    numbers = input("Введите список чисел через пробел: ").split()

    filtered_sum = filter_and_sum(numbers, lambda x: is_negative(int(x)))

    cubed_sum = sum(int(x) ** 3 for x in numbers if is_negative(int(x)))

    print("Сумма кубов отрицательных чисел списка:", cubed_sum)


sum_of_cubed_negatives()
