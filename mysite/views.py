from django.shortcuts import render
from static.StellarSystems.AlphaCentauri import SystemObject as AS
from static.StellarSystems.SolarSystem import SystemObject as SolS

def indexPage(request):
    return render(request, "index.html")

def aboutPage(request):
    return render(request, "about.html")

def alphaSystem(request):
    return render(request, "systems/alphasystem.html", 
                  {'head':              AS.get_head, 
                   'mainpanels' :       AS.get_main_panels,
                   'accentbar':         AS.get_accent_bar,
                   'objects':           AS.get_objects_str,
                   'panels':            AS.get_object_panels,
                   'sidepanel_objects': AS.get_star_sidepanel,
                   'sidepanel_buttons': AS.get_side_buttons,
                   'sidepanel_univ':    AS.get_univ_sidepanel})
    
def solarSystem(request):
    return render(request, "systems/solarsystem.html", 
                  {'head':              SolS.get_head, 
                   'mainpanels' :       SolS.get_main_panels,
                   'accentbar':         SolS.get_accent_bar,
                   'objects':           SolS.get_objects_str,
                   'panels':            SolS.get_object_panels,
                   'sidepanel_objects': SolS.get_star_sidepanel,
                   'sidepanel_buttons': SolS.get_side_buttons,
                   'sidepanel_univ':    SolS.get_univ_sidepanel})