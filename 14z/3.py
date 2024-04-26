def transliterate(text):
    # Словарь для транслитерации русских букв
    translit_dict = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo',
        'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
        'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
        'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch',
        'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'
    }

    result = ""
    for char in text:
        if char.lower() in translit_dict:
            if char.islower():
                result += translit_dict[char.lower()]
            else:
                result += translit_dict[char.lower()].capitalize()
        else:
            result += char

    return result

# Ввод текста на русском языке
russian_text = input("Введите текст на русском языке: ")

# Транслитерация текста и вывод результата
transliterated_text = transliterate(russian_text)
print("Транслитерированный текст:", transliterated_text)
