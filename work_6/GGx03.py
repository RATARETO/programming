"""
Модуль 3. Задание 3
содержит классы: MyParser, Pokemon, MyCommand
MyParser - класс сбора данных с сайта, Pokemon - класс для покемона, MyCommand - команда с покемонами
"""

from random import randint

import requests
from tqdm import tqdm


class MyParser:
    # имя файла для сохранения данных (добавил, чтобы позже можно было использовать для сохранения данных)
    file_name = "pokemons.json"

    def __init__(self, base_url: str) -> None:
        """
            Класс для сбора данных с сайта

        :param base_url: ссылка на api сайта
        """
        self.base_url = base_url

    def parse(self) -> dict[str, dict]:
        """
            Метод для сбора данных с сайта
            собирает данные: имя, вес, рост, способности, тип покемона
        :return: None
        """
        pokemon_data = dict()

        response = requests.get(self.base_url)

        for result in tqdm(response.json()["results"], desc="Парсинг покемонов"):
            response = requests.get(result["url"]).json()
            pokemon_data[response["name"]] = {
                "weight": response["weight"],
                "height": response["height"],
                "abilities": [ability["ability"]["name"] for ability in response["abilities"]],
                "types": [pokemon_type["type"]["name"] for pokemon_type in response["types"]],
            }

        return pokemon_data


class Pokemon:
    def __init__(self, name: str, state: dict) -> None:
        """
            Класс для покемона, нужен для более удобного хранения данных о покемонах
        :param name: str
        :param state: dict
        """
        self.name = name
        self.state = state

    def __str__(self) -> str:
        """
            Метод для вывода имени покемона
        :return: self.name: str
        """
        return self.name


class MyCommand:
    def __init__(self) -> None:
        """"
            Класс для команды с покемонами
            """
        self.command = []

    def __add__(self, other):
        """
        Метод для добавления покемона в команду
        :param other: Pokemon
        :return: self
        """
        assert isinstance(other, Pokemon), "В команду можно добавлять только покемонов"
        if other not in self.command:
            self.command.append(other)

        return self

    def __sub__(self, other):
        """
        Метод для удаления покемона из команды
        :param other: Pokemon
        :return: self
        """
        assert isinstance(other, Pokemon), "Из команды можно удалить только покемонов"
        if other in self.command:
            self.command.remove(other)

        return self

    @staticmethod
    def fight(pokemon1, pokemon2):
        """Статический метод для боя покемонов
        рандомно определяет победителя, выводит имя победителя
        """
        return f"победитель: {[pokemon1, pokemon2][randint(0, 1)]}"


if __name__ == "__main__":

    my_url = r"https://pokeapi.co/api/v2/pokemon/"

    parser = MyParser(my_url)
    parser.parse()

    pokemons = parser.parse()

    command = MyCommand()
    # pprint(pokemons)

    pokemon_1 = Pokemon("blastoise", pokemons["blastoise"])
    pokemon_2 = Pokemon("bulbasaur", pokemons["bulbasaur"])

    command += pokemon_1
    command += pokemon_2

    print(command.fight(pokemon_1, pokemon_2))
