# Запрос ввода слова у пользователя
word = input("Введите слово: ")

# Проверка наличия четвертой буквы и вывод результата
if len(word) >= 4:
    print("Четвертая буква введённого слова:", word[3])
else:
    print("Введённое слово слишком короткое для определения четвертой буквы.")
