from django.urls import path
from .views import *
from .models import Systems

urlpatterns = [path("AlphaCentauri", alpha_system), path("Solar", solar_system)]


def add_url_pattern(f_name: str):
    urlpatterns.append(path(f_name, template_system, {"name": f_name}))


all_systems = Systems.objects.all()
for system in all_systems:
    add_url_pattern(system.name)
