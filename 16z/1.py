def filter_and_sum(lst, condition_func):
    filtered_elements = []
    sum_of_others = 0

    for num in lst:
        if condition_func(num):
            filtered_elements.append(num)
        else:
            sum_of_others += num

    return sum_of_others


def is_condition_met(num, a, b, c):
    return num > a and num < b and num % c == 0


def cube_of_three_digit_numbers_divisible_by_eight():
    numbers = input("Введите список чисел через пробел: ").split()
    a, b, c = map(int, input("Введите три числа a, b, c через пробел: ").split())

    filtered_sum = filter_and_sum(numbers, lambda x: len(x) == 3 and int(x) % 8 == 0)

    print("Сумма кубов всех трехзначных чисел, делящихся на 8:", filtered_sum)


cube_of_three_digit_numbers_divisible_by_eight()
