from django.urls import path
from .views import *

urlpatterns = [
    path('Alpha_Centauri', alphaSystem),
    path('Solar_System', solarSystem)
]


def add_url_pattern(name: str):
    urlpatterns.append(path(name, templateSystem))


def remove_url_patten(name: str):
    urlpatterns.remove(path(name, templateSystem))
