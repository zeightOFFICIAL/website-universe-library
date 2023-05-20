from django.shortcuts import render
from static.StellarSystems.AlphaCentauri import SystemObject as AlpS
from static.StellarSystems.SolarSystem import SystemObject as SolS
from static.ServerScripts import get_sql_system

def indexPage(request):
    return render(request, "index.html")

def aboutPage(request):
    return render(request, "about.html")

def templateSystem(request, name):
    SystemObject = get_sql_system(name)
    return render(request, f'{name}.html', 
                  {'head':              SystemObject.get_head, 
                   'mainpanels' :       SystemObject.get_main_panels,
                   'accentbar':         SystemObject.get_accent_bar,
                   'objects':           SystemObject.get_objects_str,
                   'panels':            SystemObject.get_object_panels,
                   'sidepanel_objects': SystemObject.get_star_sidepanel,
                   'sidepanel_buttons': SystemObject.get_side_buttons,
                   'sidepanel_univ':    SystemObject.get_univ_sidepanel})

def alphaSystem(request):
    return render(request, "systems/alphasystem.html", 
                  {'head':              AlpS.get_head, 
                   'mainpanels' :       AlpS.get_main_panels,
                   'accentbar':         AlpS.get_accent_bar,
                   'objects':           AlpS.get_objects_str,
                   'panels':            AlpS.get_object_panels,
                   'sidepanel_objects': AlpS.get_star_sidepanel,
                   'sidepanel_buttons': AlpS.get_side_buttons,
                   'sidepanel_univ':    AlpS.get_univ_sidepanel})
    
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