def process_lists(lst, a, b, c):
    filtered_elements = []
    sum_of_others = 0

    for num in lst:
        if num > a and num < b and num % c == 0:
            filtered_elements.append(num)
        else:
            sum_of_others += num

    print("Элементы, которые соответствуют условиям:", filtered_elements)
    print("Сумма остальных элементов:", sum_of_others)


# Пример использования функции:
list1 = [1, 4, 6, 11, 14, 15, 21]
a, b, c = 2, 10, 4
process_lists(list1, a, b, c)
