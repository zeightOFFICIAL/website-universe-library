from django.shortcuts import render
from static.StellarSystems.AlphaCentauri import SystemObject

def indexPage(request):
    return render(request, "index.html")

def aboutPage(request):
    return render(request, "about.html")

def alphaSystem(request):
    return render(request, "systems/alphasystem.html", 
                  {'head':              SystemObject.get_head, 
                   'mainpanels' :       SystemObject.get_main_panels,
                   'accentbar':         SystemObject.get_accent_bar,
                   'objects':           SystemObject.get_objects_str,
                   'panels':            SystemObject.get_object_panels,
                   'sidepanel_objects': SystemObject.get_star_sidepanel,
                   'sidepanel_buttons': SystemObject.get_side_buttons,
                   'sidepanel_univ':    SystemObject.get_univ_sidepanel})