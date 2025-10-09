"""
GGx01.py

Модуль для шифрования и дешифрования текста с помощью шифра Цезаря

Основные функции:
 - cesar_cipher - кодирует список чисел в римские (примичание) step < 0 - дешифрация

 Автор: Иванов Владислав РИ-150911
 Версия: 1.0 (beta)
 Дата: 08.10.2025
"""

russian_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
english_alphabet = "abcdefghijklmnopqrstuvwxyz"


def get_language(text: str) -> str:
    is_russian = False
    is_english = False

    for char in text:
        if char in russian_alphabet:
            is_russian = True
        if char in english_alphabet:
            is_english = True

    if is_russian:
        return "russian"
    elif is_english:
        return "english"
    else:
        return "unknown"


def cesar_cipher(text: str, step: int = 0) -> str:
    """
    функция шифра Цезаря
    :param text: str - текст для шифрования
    :param step: int - шаг сдвига, при step < 0 - дешифрация
    :return: зашифрованный текст (str)
    """

    if get_language(text) == "russian":
        alphabet = russian_alphabet
        alphabet_length = len(russian_alphabet)
    elif get_language(text) == "english":
        alphabet = english_alphabet
        alphabet_length = len(english_alphabet)
    else:
        raise ValueError("Unknown language")

    new_text = ""

    for char in text:
        if char in alphabet:
            new_text += alphabet[(alphabet.find(char) + step) % alphabet_length]
        else:
            new_text += char
    return new_text


if __name__ == '__main__':
    test_word = "привет шифр цезаря"
    print(f"___ start_test___: func: cesar_cipher(ru mode), word: {test_word}")

    for number in range(35):
        word_encode = cesar_cipher(test_word, number)
        word_decode = cesar_cipher(word_encode, -number)

        if test_word != word_decode:
            print(f"!!! ERROR !!! | step: {number}")
            break
        else:
            print(f"{word_encode} -> {word_decode} | step: {number}")

    test_word = "hellow cesar cipher"

    print()
    print(f"___ start_test___: func: cesar_cipher(en mode), word: {test_word}")

    for number in range(28):
        word_encode = cesar_cipher(test_word, number)
        word_decode = cesar_cipher(word_encode, -number)

        if test_word != word_decode:
            print(f"!!! ERROR !!! | step: {number}")
            break
        else:
            print(f"{word_encode} -> {word_decode} | step: {number}")
