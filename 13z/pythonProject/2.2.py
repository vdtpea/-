def create_sentence(word_numbers, words):
    word_list = words.split()
    sentence = " ".join(word_list[int(num) - 1] for num in word_numbers.split())
    return sentence.capitalize()
word_numbers = input("Введите номера слов через пробел: ")
words = input("Введите сами слова через пробел: ")
new_sentence = create_sentence(word_numbers, words)
print("Новое предложение:", new_sentence)
letters_count = {}
for letter in new_sentence.lower():
    if letter.isalpha():
        letters_count[letter] = letters_count.get(letter, 0) + 1

max_count = max(letters_count.values()) if letters_count else 0
print("Максимальное количество раз, которое встречается буква:", max_count)
