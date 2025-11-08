"""
Модуль для сбора информации о покемонах с сайта https://pokeapi.co/
"""


import requests

# url (api сайта)
base_url = r"https://pokeapi.co/"

# получаем список покемонов и преобразуем в json
response = requests.get(base_url + "api/v2/pokemon/")

pokemon_list = response.json()

# выводим список покемонов если пользователь этого хочет
answer = input("Do you want to see the pokemon list? (yes/no): ").lower()
if answer == "yes":
    for number, pokemon in enumerate(pokemon_list["results"]):
        print(f"pokemon {number + 1} hi's name is {pokemon['name']}")

# получаем имя покемона
name = input("Enter pokemon name: ").lower()

# получаем информацию о покемоне и выводим его характеристики
response = requests.get(base_url + f"api/v2/pokemon/{name}").json()

print(f"\nname: {response['name']}")

print("types:")
for pokemon_type in response['types']:
    print(f"\ttype: {pokemon_type['type']['name']}")

print(f"weight: {response['weight']}")
print(f"height: {response['height']}")

abilities = response['abilities']

print("abilities:")
for ability in abilities:
    print(f"\tability: {ability['ability']['name']}")

