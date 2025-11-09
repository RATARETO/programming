from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("target_dog/", views.get_dog, name="target_dog"),
]
