import datetime
from decimal import Decimal

"""
    name: GG x01
    Модуль для работы с холодильником
    
    функции:
        add(items, title, amount, expiration_date=None) - добавить продукт в холодильник
        add_by_note(items, note) - добавить продукт по строке из описания
        find(items, needle) - найти продукты по названию
        amount(items, needle) - найти количество продуктов по названию
    
"""


def add(items: dict, title: str, amount: Decimal, expiration_date: str=None) -> None:
    """
        Добавляет продукт в холодильник
    :param items: 
    :param title:
    :param amount:
    :param expiration_date:
    :return: None
    """
    if title in items.keys():
        items[title].append(
            {"amount": Decimal(float(amount)),
             "expiration_date": datetime.datetime.strptime(expiration_date, r"%Y-%m-%d").date()}
        )
    else:
        if expiration_date:
            items[title] = [
                {"amount": Decimal(float(amount)), "expiration_date": datetime.datetime.strptime(expiration_date, r"%Y-%m-%d").date()}
            ]
        else:
            items[title] = [{"amount": Decimal(float(amount)), "expiration_date": expiration_date}]


def add_by_note(items: dict, note: str) -> None:
    """
        Добавляет продукт по строке из описания
    :param items:
    :param note:
    :return: None
    """
    description = note.split()
    if "-" in description[-1]:
        title, amount, expiration_date = " ".join(description[:-2]), description[-2], description[-1]
    else:
        title, amount, expiration_date = " ".join(description[:-1]), description[-1], None

    add(items, title, amount, expiration_date)


def find(items: dict, needle: str) -> list[str]:
    """
        Найти продукты по строке
    :param items:
    :param needle:
    :return: list[str]
    """
    answer = []
    for key in items.keys():
        if needle.lower() in key.lower():
            answer.append(key)
    return answer


def amount(items: dict, needle: str) -> Decimal:
    """
        Найти количество продуктов по строке
    :param items:
    :param needle:
    :return: Decimal
    """
    data = find(items, needle)
    answer = 0
    for key in data:
        answer += sum([item["amount"] for item in items[key]])
    return Decimal(float(answer))