def create_sentence(word_numbers, words):
    word_list = words.split()
    sentence = " ".join(word_list[int(num)] for num in word_numbers.split())
    return sentence.capitalize()
def calculate_sum(numbers, start, end):
    numbers_list = numbers.split()
    sum_numbers = sum(int(num) for num in numbers_list[start:end+1])
    return sum_numbers
word_numbers = input("Введите номера слов через пробел: ")
words = input("Введите сами слова через пробел: ")

new_sentence = create_sentence(word_numbers, words)

print("Новое предложение:", new_sentence)
numbers = input("Введите набор целых чисел через пробел: ")
start, end = map(int, input("Введите два целых числа X и Y: ").split())
sum_result = calculate_sum(numbers, start, end)
print("Сумма чисел от {} до {}: {}".format(start, end, sum_result))
