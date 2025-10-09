from os import system
from random import choice, randint, shuffle

"""
GGx04.py

Скрипт генерирует пароль с заданными параметрами и выводит его на экран
Внимание! в модуле есть команда cls, поэтому рекомендуется запускать скрипт в консоли

Основные функции:
 - get_password - генерирует пароль с заданными параметрами

 Автор: Иванов Владислав РИ-150911
 Версия: 1.0 (beta)
 Дата: 08.10.2025
"""


def get_password(length_password, *args):
    """
    Функция генерирует пароль с заданными параметрами
    :param length_password: int
    :param args: str
    :return: str
    """
    assert args and length_password > 0, "Введите число и/или тип пароля"

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    password = ""
    while len(password) < length_password:
        if "lower" in args:
            password += choice(alphabet)
        if "upper" in args:
            password += choice(alphabet.upper())
        if "number" in args:
            password += str(randint(0, 9))
        if "special" in args:
            password += choice("!@#$%^&*()_+")
    password = list(password)
    shuffle(password)
    return "".join(password)[:length_password]


while True:
    command = input("Какой пароль вы хотите? чтобы задать длину пароля сначала введите число, \n"
                    "даллее через запятую указывайте тип пароля (lower, upper, number, special),\n"
                    "если хотите выйти напишите exit: ").replace(" ", "").split(",")
    if command == ["exit"]:
        break
    password = get_password(int(command[0]), *command[1:])
    system("cls")
    print(f"Ваш пароль: {password}")
