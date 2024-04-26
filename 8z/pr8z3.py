# Ввод строки с английским текстом
english_text = input("Введите строку с английским текстом: ")

# Разделение строки на слова
words = english_text.split()

# Подсчет количества слов, начинающихся с буквы 'b'
b_words_count = sum(1 for word in words if word.lower().startswith('b'))

# Вывод результата
print(f"Количество слов, начинающихся с буквы 'b': {b_words_count}")
