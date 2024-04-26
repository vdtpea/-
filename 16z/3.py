def filter_and_print(lst, condition_func):
    for num in lst:
        if condition_func(num):
            print(num)


def is_even(num):
    return num % 2 == 0


def print_even_numbers():
    numbers = input("Введите список чисел через пробел: ").split()

    filter_and_print(numbers, lambda x: is_even(int(x)))


print_even_numbers()
