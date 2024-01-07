from django.urls import path, URLPattern
from .views import *
from .models import Systems

urlpatterns = [path("", universe_page), path("AlphaCentauri", alpha_system_page), path("Solar", solar_system_page)]


def add_url_pattern(f_name: str) -> list[URLPattern]:
    urlpatterns.append(path(f_name, template_system_page, {"name": f_name}))
    return urlpatterns


all_systems = Systems.objects.all()
for system in all_systems:
    add_url_pattern(system.name_name)
