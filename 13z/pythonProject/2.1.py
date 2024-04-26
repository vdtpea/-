def add_hyphens_and_uppercase(sentence):
    new_sentence = ""
    for word in sentence.split():
        new_word = "-".join(word.upper())
        new_sentence += new_word + " "
    return new_sentence.strip()
sentence = input("Введите строку с несколькими словами: ")

new_sentence = add_hyphens_and_uppercase(sentence)

print("Результат:", new_sentence)
