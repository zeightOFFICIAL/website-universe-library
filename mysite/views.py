from django.shortcuts import render

def indexPage(request):
    return render(request, "index.html")

def solarPage(request):
    return render(request, "systems/solar.html")