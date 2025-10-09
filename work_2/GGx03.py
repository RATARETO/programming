"""
GGx03.py

Модуль для расфасовки пирожных

Основные функции:
 - print_pack_report - расфасовка пирожных

Автор: Иванов Владислав РИ-150911
Версия: 1.0 (beta)
Дата: 08.10.2025
"""


def print_pack_report(number):
    """
    Функция расфасовки пирожных
    :param number: int
    :return: None -> print
    """
    assert type(number) == int and number > 1

    # Цикл в порядке убывания от number до 1
    for i in range(number, 0, -1):
        if i % 5 == 0 and i % 3 == 0:
            print(f"{i} - расфасуем по 3 или по 5")
        elif i % 5 == 0:
            print(f"{i} - расфасуем по 5")
        elif i % 3 == 0:
            print(f"{i} - расфасуем по 3")
        else:
            print(f"{i} - не заказываем!")


if __name__ == '__main__':
    # Пример использования
    print_pack_report(15)