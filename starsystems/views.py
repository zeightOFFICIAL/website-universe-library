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
    get_sql_systems_pair,
)


def universe_page(request):
    cards = []
    cards.insert(
        0,
        CardClass(
            -2,
            "Alpha Centauri",
            "alpha.png",
            ["#FF0000", "#FF5000"],
            "AlphaCentauri",
            "Alpha Centauri is a star system located in the constellation of Centaurus, which is the closest star system to our own solar system. The system consists of three stars: Alpha Centauri A, Alpha Centauri B, and Proxima Centauri.",
            "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Artist%27s_impression_of_the_planet_orbiting_Proxima_Centauri.jpg/1280px-Artist%27s_impression_of_the_planet_orbiting_Proxima_Centauri.jpg",
        ),
    )
    cards.insert(
        0,
        CardClass(
            -1,
            "Solar",
            "solar.png",
            ["#FBAB7E", "#ff792b"],
            "Solar",
            "The Solar System is our neighborhood in space, where our planet Earth resides. It consists of the Sun, a yellow dwarf star at the center, and a collection of celestial bodies that orbit around it. It is a cradle of humankind.",
            "https://images.unsplash.com/photo-1565739865381-f5df2ef21490?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1887&q=80",
        ),
    )

    for pair in get_sql_systems_pair():
        l_href = pair[1].replace(" ", "")
        card = CardClass(
            pair[0],
            pair[1],
            pair[2],
            [pair[3], pair[4]],
            l_href,
            pair[5],
            pair[6],
        )
        cards.append(card)

    cards.append(
        CardClass(
            -3,
            "Coming soon!",
            "placeholder1.png",
            ["white", "red"],
            "?",
            "Little is known about this particular place",
            "https://c4.wallpaperflare.com/wallpaper/996/46/567/planets-surface-sci-fi-digital-art-wallpaper-preview.jpg",
        ),
    )
    cards.append(
        CardClass(
            -4,
            "Coming soon!",
            "placeholder2.png",
            ["white", "white"],
            "?2",
            "Little is known about this particular place",
            "https://c4.wallpaperflare.com/wallpaper/996/46/567/planets-surface-sci-fi-digital-art-wallpaper-preview.jpg",
        ),
    )
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
