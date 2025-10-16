"""
Решение учебных заданий
"""

# case 1


class Book:
    def __init__(self, title, author, year) -> None:
        """
        __init__ - конструктор класса
        :param title: str
        :param author: str
        :param year: float
        """
        self.title: str = title
        self.author: str = author
        self.year: float = year

    def info(self) -> str:
        """
        функция, которая выводит информацию о книге
        :return: str
        """
        return f"{self.title} by {self.author} ({self.year})"

