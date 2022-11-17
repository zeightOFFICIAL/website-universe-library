from django.shortcuts import render

def indexPage(request):
    return render(request, "index.html")

def solarPage(request):
    return render(request, "systems/solar.html")

def alphaPage(request):
    return render(request, "systems/alpha.html")

def trappPage(request):
    return render(request, "systems/trapp.html")

def trebiaPage(request):
    return render(request, "systems/trebia.html")

def aboutPage(request):
    return render(request, "about.html")
