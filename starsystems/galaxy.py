"""
Galactic placement of star systems, plus reference landmarks, for the main page's
galaxy view.

Star systems are keyed by href (the system name without spaces). Positions use
galactic coordinates as seen from the Sun:
    l   galactic longitude, degrees (0 = towards the galactic centre)
    b   galactic latitude, degrees (+90 = north galactic pole)
    d   distance from the Sun, light-years
Fictional systems have no real sky position; they carry an explicit galactocentric
position instead (x, z in light-years, galactic centre at 0,0) and a "source" to
credit. "hidden" keeps an entry without drawing it.

A system without an entry here is simply left out of the galaxy view.

Sources: distance to the galactic centre from the GRAVITY collaboration's 2019
measurement of 8.178 kpc; the Sun sits ~65 ly north of the galactic plane. All
l/b values are computed from J2000 RA/Dec and verified against the catalogue
positions (Sgr A* lands on l=0, b=0 by definition, which checks the conversion).
"""

SUN_TO_GALACTIC_CENTRE_LY = 26_700
SUN_HEIGHT_ABOVE_PLANE_LY = 65

GALAXY_PLACEMENT = {
    "Solar": {"l": 0.0, "b": 0.0, "d": 0.0},
    "AlphaCentauri": {"l": 315.73, "b": -0.68, "d": 4.37},
    "Sirius": {"l": 227.23, "b": -8.89, "d": 8.6},
    "Trappist": {"l": 69.71, "b": -56.64, "d": 40.7},
    "Mira": {"l": 167.75, "b": -57.98, "d": 300.0},
    "Polaris": {"l": 123.28, "b": 26.46, "d": 433.0},
    "Trebia": {"fictional": True, "source": "Mass Effect", "x": 21_000, "z": -9_000, "hidden": True},
}

# Landmarks drawn at their true positions, as a reference for where our systems sit.
# kind: nebula | open | globular
DEEP_SKY = [
    {"name": "Orion Nebula", "alias": "M42", "kind": "nebula", "l": 209.01, "b": -19.38, "d": 1_344},
    {"name": "Eagle Nebula", "alias": "M16", "kind": "nebula", "l": 16.95, "b": 0.79, "d": 7_000},
    {"name": "Carina Nebula", "alias": "NGC 3372", "kind": "nebula", "l": 287.69, "b": -0.79, "d": 8_500},
    {"name": "Lagoon Nebula", "alias": "M8", "kind": "nebula", "l": 5.96, "b": -1.17, "d": 4_100},
    {"name": "Crab Nebula", "alias": "M1", "kind": "nebula", "l": 184.56, "b": -5.78, "d": 6_500},
    {"name": "Helix Nebula", "alias": "NGC 7293", "kind": "nebula", "l": 36.16, "b": -57.12, "d": 655},
    {"name": "Ring Nebula", "alias": "M57", "kind": "nebula", "l": 63.17, "b": 13.98, "d": 2_570},
    {"name": "Pleiades", "alias": "M45", "kind": "open", "l": 166.64, "b": -23.46, "d": 444},
    {"name": "Hyades", "alias": "Mel 25", "kind": "open", "l": 180.08, "b": -22.32, "d": 153},
    {"name": "Omega Centauri", "alias": "NGC 5139", "kind": "globular", "l": 309.10, "b": 14.97, "d": 17_090},
    {"name": "Great Cluster", "alias": "M13", "kind": "globular", "l": 59.01, "b": 40.91, "d": 22_200},
    {"name": "47 Tucanae", "alias": "NGC 104", "kind": "globular", "l": 305.89, "b": -44.89, "d": 13_000},
]
