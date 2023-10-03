# from static.Types.SystemType import SystemClass
from django.shortcuts import render
from static.StellarSystems.AlphaCentauri import System as Alpha
from static.StellarSystems.SolarSystem import System as Solar
from static.Types.DeckType import DeckClass
from static.Types.CardType import CardClass
from static.ServerScripts import (
    get_sql_system,
    get_sql_system_id,
    get_sql_systems_thumbnail,
    get_sql_cards,
)


def universe_page(request):
    cards = []

    cards.insert(
        0,
        CardClass(
            -2,
            "Alpha Centauri",
            "AlphaCentauri",
            "Alpha Centauri is a star system located in the constellation of Centaurus, which is the closest star system to our own solar system. The system consists of three stars: Alpha Centauri A, Alpha Centauri B, and Proxima Centauri.",
            ["#FF0000", "#FF5000"],
            "Alphacover",
            "Alpha",
        ),
    )
    cards.insert(
        0,
        CardClass(
            -1,
            "Solar",
            "Solar",
            "The Solar System is our neighborhood in space, where our planet Earth resides. It consists of the Sun, a yellow dwarf star at the center, and a collection of celestial bodies that orbit around it. It is a cradle of humankind.",
            ["#FBAB7E", "#ff792b"],
            "Solarcover",
            "Solar",
        ),
    )

    for card in get_sql_cards():
        cards.append(card)

    Deck = DeckClass(1, cards)
    return render(request, "Universe.html", {"cards": Deck.__repr__()})


def template_system_page(request, name):
    system_id = get_sql_system_id(name)
    System = get_sql_system(system_id)
    return render(
        request,
        "System.html",
        {
            "head": System.get_head,
            "mainpanels": System.get_main_panels,
            "accentbar": System.get_accent_bar,
            "objects": System.get_objects_str,
            "panels": System.get_object_panels,
            "sidepanel_objects": System.get_star_sidepanel,
            "sidepanel_buttons": System.get_side_buttons,
            "sidepanel_univ": System.get_univ_sidepanel(get_sql_systems_thumbnail()),
        },
    )


def alpha_system_page(request):
    return render(
        request,
        "System.html",
        {
            "head": Alpha.get_head,
            "mainpanels": Alpha.get_main_panels,
            "accentbar": Alpha.get_accent_bar,
            "objects": Alpha.get_objects_str,
            "panels": Alpha.get_object_panels,
            "sidepanel_objects": Alpha.get_star_sidepanel,
            "sidepanel_buttons": Alpha.get_side_buttons,
            "sidepanel_univ": Alpha.get_univ_sidepanel(get_sql_systems_thumbnail()),
        },
    )


def solar_system_page(request):
    return render(
        request,
        "System.html",
        {
            "head": Solar.get_head,
            "mainpanels": Solar.get_main_panels,
            "accentbar": Solar.get_accent_bar,
            "objects": Solar.get_objects_str,
            "panels": Solar.get_object_panels,
            "sidepanel_objects": Solar.get_star_sidepanel,
            "sidepanel_buttons": Solar.get_side_buttons,
            "sidepanel_univ": Solar.get_univ_sidepanel(get_sql_systems_thumbnail()),
        },
    )
