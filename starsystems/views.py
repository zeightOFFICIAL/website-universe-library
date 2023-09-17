from django.shortcuts import render
from static.StellarSystems.AlphaCentauri import System as Alpha
from static.StellarSystems.SolarSystem import System as Solar
from static.ServerScripts import (
    get_sql_system,
    get_sql_id_from_name,
    get_sql_system_univ,
)


def template_system(request, name):
    id = get_sql_id_from_name(name)
    System = get_sql_system(id)
    return render(
        request,
        "templatesystem.html",
        {
            "head": System.get_head,
            "mainpanels": System.get_main_panels,
            "accentbar": System.get_accent_bar,
            "objects": System.get_objects_str,
            "panels": System.get_object_panels,
            "sidepanel_objects": System.get_star_sidepanel,
            "sidepanel_buttons": System.get_side_buttons,
            "sidepanel_univ": System.get_univ_sidepanel(get_sql_system_univ()),
        },
    )


def alpha_system(request):
    return render(
        request,
        "templatesystem.html",
        {
            "head": Alpha.get_head,
            "mainpanels": Alpha.get_main_panels,
            "accentbar": Alpha.get_accent_bar,
            "objects": Alpha.get_objects_str,
            "panels": Alpha.get_object_panels,
            "sidepanel_objects": Alpha.get_star_sidepanel,
            "sidepanel_buttons": Alpha.get_side_buttons,
            "sidepanel_univ": Alpha.get_univ_sidepanel(get_sql_system_univ),
        },
    )


def solar_system(request):
    return render(
        request,
        "templatesystem.html",
        {
            "head": Solar.get_head,
            "mainpanels": Solar.get_main_panels,
            "accentbar": Solar.get_accent_bar,
            "objects": Solar.get_objects_str,
            "panels": Solar.get_object_panels,
            "sidepanel_objects": Solar.get_star_sidepanel,
            "sidepanel_buttons": Solar.get_side_buttons,
            "sidepanel_univ": Solar.get_univ_sidepanel(get_sql_system_univ),
        },
    )
