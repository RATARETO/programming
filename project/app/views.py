"""
    содержит функции для обработки запросов: index, get_dog
    index - главная страница
    get_dog - страница с изображением собаки
"""

from django.shortcuts import render

import requests


# Create your views here.
def index(request):
    """
        Главная страница
        загружает список всех парод собак и передает его в шаблон
    :param request: GET запрос
    :return: index.html & context
    """
    context = []

    base_url = r"https://dog.ceo/api/breeds/list/all"  # список все парод

    response = requests.get(base_url).json()

    for breed in response["message"].keys():
        context.append(
            {
                "breed": breed
            }
        )

    return render(request, "index.html", {"dogs": context})


def get_dog(request):
    """
        Страница, в зависимости от названия пароды, переданной в форму в index.html,
        выводит изображением собаки и названием пароды
    :param request: POST запрос
    :return: dog.html & context
    """
    breed = request.POST.get("breed")

    response = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random").json()

    context = {
        "breed": breed,
        "image": response["message"]
    }

    return render(request, r"posts\dog.html", context)
