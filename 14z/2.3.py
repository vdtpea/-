def find_word_description(dictionary, query_word):
    if query_word in dictionary:
        return dictionary[query_word]
    else:
        return "Нет в словаре"

# Ввод количества записей в словаре
n = int(input("Введите количество записей в словаре: "))

# Создание словаря
dictionary = {}
for _ in range(n):
    word, description = input().split(" - ")
    dictionary[word] = description

# Запрос слова для поиска его описания
query_word = input("Введите слово для поиска его описания: ")

# Поиск описания слова в словаре и вывод результата
result_description = find_word_description(dictionary, query_word)
print("result_description:", result_description)
