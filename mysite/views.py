from django.shortcuts import render
from static.classes.PanelsClass import SimpleTextPanel, SimpleImagePanel

def indexPage(request):
    return render(request, "index.html")

def solarPage(request):
    return render(request, "systems/solar.html", {'panel': SimpleImagePanel(1000, "../static/jpg/solarsystem/solar1.png", "#FBAB7E", "#F7CE68", "#ff0").__str__}, content_type="text/html")

def alphaPage(request):
    return render(request, "systems/alpha.html")

def trappPage(request):
    return render(request, "systems/trapp.html")

def trebiaPage(request):
    return render(request, "systems/trebia.html")

def aboutPage(request):
    return render(request, "about.html")
