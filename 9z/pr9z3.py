# Программа выводит слова, вводимые пользователем, пока они начинаются на букву "с" (как заглавную, так и строчную)
while True:
    word = input("Введите слово: ")
    if word.lower().startswith('с'):
        print(word)
    else:
        break
