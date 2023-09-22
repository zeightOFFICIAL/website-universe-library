from django.urls import path
from .views import *
from .models import Systems

urlpatterns = [path("AlphaCentauri", alpha_system_page), path("Solar", solar_system_page), path("", universe_page)]


def add_url_pattern(f_name: str):
    urlpatterns.append(path(f_name, template_system_page, {"name": f_name}))
    return urlpatterns


all_systems = Systems.objects.all()
for system in all_systems:
    add_url_pattern(system.name)
