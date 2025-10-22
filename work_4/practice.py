from datetime import datetime
from abc import ABC, abstractmethod

"""
Решение учебных заданий на практике
"""

# case 1, 3, 4


class Printable(ABC):
    """
    абстрактный класс для Book
    """
    @abstractmethod
    def info(self):
        pass


class AltBook:
    def __init__(self, title, author, year) -> None:
        self.title: str = title
        self.author: str = author
        self.year: int = year

    @classmethod
    def alt_init(cls, data):
        """
        Альтернативный конструктор
        :param data:
        :return:
        """
        title, author, year = data.split(";")
        print(data.split(";"))
        return cls(title, author, int(year))


class Book:
    def __init__(self, title, author) -> None:
        """
        :param title: str
        :param author: str
        :param year: float
        """
        self.title: str = title
        self.author: str = author
        self.year: int = datetime.now().year

    @property
    def age(self) -> int:
        return self.year

    @age.setter
    def age(self, value):
        assert isinstance(value, int), "Год должен быть int"
        if value <= int(datetime.now().year):
            self.year = value
        else:
            raise ValueError("Год не может быть больше текущего")

    def info(self) -> str:
        """
        функция, которая выводит информацию о книге
        :return: str
        """
        return f"{self.title} by {self.author} ({self.year})"

    def __str__(self) -> str:
        return self.info()

    def __eq__(self, other) -> bool:
        assert isinstance(other, Book), "Объект не является экземпляром класса Book"
        """
        Сравнение объектов по все полям
        :param other: 
        :return: bool
        """
        return vars(self) == vars(other)


# case 2

class EBook(Book):
    def __init__(self, title, author, year, format) -> None:
        """
        :param title: str
        :param author: str
        :param year: float
        :param format: str
        """
        super().__init__(title, author, year)
        self.format: float = format

    def info(self) -> str:
        """
        функция, которая выводит информацию о книге + формат
        :return: str
        """
        return f"{self.title} by {self.author} ({self.year}) ({self.format})"


# from abc import ABC, abstractmethod
# ABC - класс для создания абстрактного класса
# abstractmethod - декоратор для создания абстрактного метода
# abstractmethod - абстрактный метод, обязательный для наследников

# в property property создаёт геттер, а уже к нему создаётся сеттер value -> @value.setter

# - мысли в слух -
#
# class Base:
#     def __init__(self):
#         self.name = "base"
#
#     def __repr__(self):
#         return self.name
#
#
# base = Base()
#
# data = {
#     "base": "it's base"
# }
# print(data[base.__repr__()])


# class Base:
#     def __init__(self, name):
#         self.name = name
#
#     def __eq__(self, other):
#         return vars(self) == vars(other)
#
#
# base1 = Base("base1")
# base2 = Base("base2")
#
# print(f"base1 == base2 ?: {base1 == base2} | base1: {vars(base1)} : base2: {vars(base2)}")
#
# base1 = Base("base1")
# base2 = Base("base1")
#
# print(f"base1 == base2 ?: {base1 == base2} | base1: {vars(base1)} : base2: {vars(base2)}")

# base_1 = AltBook.alt_init("Война и наказание;Лев Толстой;1869")
# print(vars(base_1))

base_1 = Book("Война и наказание", "Лев Толстой")

base_1.age = 2010

print(base_1)
