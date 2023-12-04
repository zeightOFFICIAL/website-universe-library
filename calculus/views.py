from django.shortcuts import render


def calculus_view(request):
    return render(request, "Calculus.html")
