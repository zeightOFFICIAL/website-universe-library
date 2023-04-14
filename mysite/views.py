from django.shortcuts import render
from static.types.SystemType import SystemClass
from static.types.ObjectType import ObjectClass
from static.types.PanelType import *

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

def tempSystem(request):
    fore_color = "#ff7500"
    back_color = "red"
    
    Alpha = ObjectClass(1, "Alpha", 99, ["10vh", "-5vh", "#ffd000", "#f70", "30px"],
                                        ["2vh", "2vh", "-1vh", "-1vh"],
                                        ["2vh", "2vh", "-1vh", "-1vh", "10s", "100%"], [])
    
    panel1 = TextPanel(1, "Alpha Centauri", "Alpha Centauri (Latinized from a Centauri and often abbreviated Alpha Cen or a Cen) is a triple star system in the constellation of Centaurus. It consists of 3 stars: Alpha Centauri A (officially Rigil Kentaurus), Alpha Centauri B (officially Toliman) and Alpha Centauri C (officially Proxima Centauri). Proxima Centauri is also the closest star to the Sun at 4.2465 light-years (1.3020 pc).", fore_color, back_color, fore_color)
    panel2 = SimpleImagePanel(2, "../static/jpg/alphasystem/alphasystem1.jpg", fore_color, back_color, fore_color)
    panel3 = SimpleImagePanel(3, "../static/jpg/alphasystem/alphasystem2.jpg", fore_color, back_color, fore_color)
    
    system = SystemClass(1, "Alpha Centauri", [panel1, panel2, panel3], [], "alternativeicon.ico") 
    return render(request, "systems/temp.html", {'head': system.GetHead, 'mainpanels' : system.GetMainPanels})