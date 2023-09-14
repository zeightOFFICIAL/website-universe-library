from django.urls import path
from .views import *
from .models import Systems

urlpatterns = [
    path('AlphaCentauri', alphaSystem),
    path('Sun', solarSystem)
]


def add_url_pattern(f_name: str):
    urlpatterns.append(path(f_name, templateSystem, {'name': f_name}))


systems = Systems.objects.all()
for system in systems:
    add_url_pattern(system.name)
