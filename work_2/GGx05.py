"""
GGx05.py

Модуль для работы со списками римских чисел.

Основные функции:
 - numbers_encoder - кодирует список чисел в римские
 - numbers_encoder - декодирует список римских чисел в числа десятичные

 Автор: Иванов Владислав РИ-150911
 Версия: 1.0 (beta)
 Дата: 08.10.2025
"""


def numbers_encoder(list_numbers: list[int]) -> list[str]:
    """
    Функция кодирует список чисел в римские
    :param list_numbers: list[int] - список чисел для кодирования
    :return: list[str] - список римских чисел после кодирования
    """
    answer: list[str] = []
    new_number: str = ""
    for number in list_numbers:
        new_number += "M" * (number // 1000)

        new_number += "D" * (number % 1000 // 500)

        new_number += "C" * (number % 1000 % 500 // 100)

        new_number += "L" * (number % 1000 % 500 % 100 // 50)

        new_number += "X" * (number % 1000 % 500 % 100 % 50 // 10)

        new_number += "IX" * (number % 1000 % 500 % 100 % 10 // 9)

        new_number += "V" * (number % 1000 % 500 % 100 % 10 % 9 // 5)

        new_number += "IV" * (number % 1000 % 500 % 100 % 10 % 9 % 5 // 4)

        new_number += "I" * (number % 1000 % 500 % 100 % 10 % 9 % 5 % 4)

        answer.append(new_number)
    return answer


def numbers_decoder(list_numbers: list[str]) -> list[int]:
    """
        Функция декодирует список римских чисел в десятичные числа
        :param list_numbers: list[str] - список римских чисел после кодирования
        :returns:  list[int] - список чисел для кодирования

        """
    answer: list[int] = []
    alphabet: dict[str, int] = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "R": 9,
        "V": 5,
        "S": 4,
        "I": 1,
    }
    for number in list_numbers:
        new_number: int = 0
        target_string = number.replace("IX", "R").replace("IV", "S")

        for key, value in alphabet.items():
            new_number += value * target_string.count(key)
        answer.append(new_number)
    return answer


print(numbers_decoder(numbers_encoder([1234])))


