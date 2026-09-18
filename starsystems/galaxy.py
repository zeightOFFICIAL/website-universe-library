"""
Galactic placement of star systems for the main page's galaxy view.

Keyed by the system's href (name without spaces). Positions use galactic
coordinates as seen from the Sun:
    l   galactic longitude, degrees (0 = towards the galactic centre)
    b   galactic latitude, degrees (+90 = north galactic pole)
    d   distance from the Sun, light-years
Fictional systems have no real sky position; they carry an explicit
galactocentric position instead (x, z in light-years, galactic centre at 0,0)
and a "source" to credit.

A system without an entry here is simply left out of the galaxy view.
"""

SUN_TO_GALACTIC_CENTRE_LY = 26_000

GALAXY_PLACEMENT = {
    "Solar": {"l": 0.0, "b": 0.0, "d": 0.0},
    "AlphaCentauri": {"l": 315.73, "b": -0.68, "d": 4.37},
    "Sirius": {"l": 227.23, "b": -8.89, "d": 8.6},
    "Trappist": {"l": 69.71, "b": -56.64, "d": 40.7},
    "Mira": {"l": 167.75, "b": -57.98, "d": 300.0},
    "Polaris": {"l": 123.28, "b": 26.46, "d": 433.0},
    "Trebia": {"fictional": True, "source": "Mass Effect", "x": 21_000, "z": -9_000},
}
