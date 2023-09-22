from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index_page),
    path("About", views.about_page),
    path("Universe/", include("starsystems.urls"))
]
