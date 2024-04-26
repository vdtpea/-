def count_spaces_and_check_even(input_string):
    space_count = input_string.count(' ')
    if space_count % 2 == 0:
        print("Четное число")
    else:
        print("Нечетное число")
    return space_count

input_string = input("Введите строку: ")

space_count = count_spaces_and_check_even(input_string)

print(f"space_count: {space_count}")
