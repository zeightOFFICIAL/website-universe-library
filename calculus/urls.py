from django.urls import path
from .views import *

urlpatterns = [path("", calculus_view)]
