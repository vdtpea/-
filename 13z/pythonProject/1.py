def create_sentence(word_indexes, words):
    word_list = words.split()
    sentence = " ".join([word_list[int(index)-1] for index in word_indexes.split()])
    return sentence.capitalize()
word_indexes = input("Введите номера слов через пробел: ")
words = input("Введите сами слова через пробел: ")
new_sentence = create_sentence(word_indexes, words)
print("Новое предложение:", new_sentence)
