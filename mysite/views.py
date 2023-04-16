from django.shortcuts import render
from static.StellarSystems.AlphaCentauri import SystemObject

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
    return render(request, "systems/temp.html", 
                  {'head':              SystemObject.get_head, 
                   'mainpanels' :       SystemObject.get_main_panels,
                   'accentbar':         SystemObject.get_accent_bar,
                   'objects':           SystemObject.get_objects,
                   'panels':            SystemObject.get_panels,
                   'sidepanel_objects': SystemObject.get_side_panel_obj})