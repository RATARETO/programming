from abc import ABC, abstractmethod


""" Решение содержит абстрактный класс Employee и его наследников Manager и Developer. """


class Employee(ABC):
    def __init__(self, name: str, completed_tasks: int) -> None:
        """
        Абстрактный класс Employee
        :param name: str
        :param completed_tasks: int
        """
        self.__name = name
        self.completed_tasks = completed_tasks

    @property
    def title(self) -> str:
        return self.__name

    @abstractmethod
    def get_salary(self) -> float:
        """
        Метод для расчета зарплаты по формуле: коэффициент * количество выполненных задач * 100
        :return:
        """
        pass

    def __str__(self) -> str:
        return self.title


class Manager(Employee):
    def __init__(self, name: str, completed_tasks: int) -> None:
        """
        Класс Manager наследуется от класса Employee
        :param name: str
        :param completed_tasks:
        """
        super().__init__(name, completed_tasks)

        self.ratio = 1.2

    def get_salary(self) -> float:
        """
        Метод для расчета зарплаты
        :return: float
        """
        return self.ratio * self.completed_tasks * 100


class Developer(Employee):
    def __init__(self, name: str, completed_tasks: int) -> None:
        """
        Класс Developer наследуется от класса Employee
        :param name: str
        :param completed_tasks: int
        """
        super().__init__(name, completed_tasks)
        self.ratio = 0.7

    def get_salary(self) -> float:
        """
        Метод для расчета зарплаты
        :return: float
        """
        return self.ratio * self.completed_tasks * 100

