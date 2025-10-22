from abc import ABC, abstractmethod

""" Решение содержит абстрактный класс Base, классы Plane, Car, Ship, а также интерфейс для работы с ними. """


class Base(ABC):
    def __init__(self, name: str, speed: float) -> None:
        """
        Абстрактный класс для транспортных средств.
        :param name:
        :param speed:
        """
        self.name: str = name
        self.speed: float = speed

    @abstractmethod
    def move(self, time: float) -> str:
        """
        Метод для движения транспортного средства.
        :param time:
        :return: str
        """
        pass


class Plane(Base):
    def __init__(self, name: str, speed: float) -> None:
        """
        Класс самолета.
        :param name: str
        :param speed: float
        """
        super().__init__(name, speed)
        self.type: str = "plane"

    def move(self, time):
        return f"{self.name} is flying at {self.speed} km/h | hurts {time} "


class Car(Base):
    def __init__(self, name: str, speed: float) -> None:
        """
        Класс машины.
        :param name: str
        :param speed: float
        """
        super().__init__(name, speed)
        self.type: str = "car"

    def move(self, time: float) -> str:
        return f"{self.name} is driving at {self.speed} km/h | hurts {time} "


class Ship(Base):
    def __init__(self, name: str, speed: float) -> None:
        """
        Класс корабля.
        :param name: str
        :param speed: float
        """
        super().__init__(name, speed)
        self.type: str = "ship"

    def move(self, time: float) -> str:
        return f"{self.name} is sailing at {self.speed} km/h | hurts {time} "


def interface(obj, time_obj: float) -> str:
    """
    Интерфейс для работы с транспортными средствами.
    :param obj: класс транспортного средства, наследующегося от класса Base.
    :param time_obj: float
    :return: str
    """
    return obj.move(time_obj)


plane = Plane("Boeing 747", 800)
car = Car("Ford Focus", 100)
ship = Ship("Titanic", 20)

for obj in [plane, car, ship]:
    print(interface(obj, 100))
