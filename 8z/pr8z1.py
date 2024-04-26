# Ввод строки слов
sentence = input("Введите строку из слов, разделенных пробелами: ")

# Разделение строки на слова
words = sentence.split()

# Перестановка слов в обратном порядке
reversed_sentence = " ".join(reversed(words))

# Вывод результата
print("Строка с переставленными словами в обратном порядке:")
print(reversed_sentence)
