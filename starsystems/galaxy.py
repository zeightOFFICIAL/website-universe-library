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
# kind: nebula | remnant | planetary | open | globular | structure
DEEP_SKY = [
    {"name": "Orion Nebula", "alias": "M42", "kind": "nebula", "l": 209.01, "b": -19.38, "d": 1_344},
    {"name": "Horsehead Nebula", "alias": "Barnard 33", "kind": "nebula", "l": 206.96, "b": -16.78, "d": 1_375},
    {"name": "Rosette Nebula", "alias": "NGC 2237", "kind": "nebula", "l": 206.47, "b": -1.64, "d": 5_200},
    {"name": "Cone Nebula", "alias": "NGC 2264", "kind": "nebula", "l": 202.98, "b": 2.25, "d": 2_700},
    {"name": "Eagle Nebula", "alias": "M16", "kind": "nebula", "l": 16.95, "b": 0.79, "d": 7_000},
    {"name": "Lagoon Nebula", "alias": "M8", "kind": "nebula", "l": 5.96, "b": -1.17, "d": 4_100},
    {"name": "Trifid Nebula", "alias": "M20", "kind": "nebula", "l": 7.00, "b": -0.25, "d": 4_100},
    {"name": "Omega Nebula", "alias": "M17", "kind": "nebula", "l": 15.05, "b": -0.67, "d": 5_500},
    {"name": "Carina Nebula", "alias": "NGC 3372", "kind": "nebula", "l": 287.69, "b": -0.79, "d": 8_500},
    {"name": "NGC 3603", "alias": "NGC 3603", "kind": "nebula", "l": 291.62, "b": -0.52, "d": 20_000},
    {"name": "W51 Complex", "alias": "W51", "kind": "nebula", "l": 49.40, "b": -0.32, "d": 17_000},
    {"name": "Bubble Nebula", "alias": "NGC 7635", "kind": "nebula", "l": 112.24, "b": 2.80, "d": 11_000},
    {"name": "North America Nebula", "alias": "NGC 7000", "kind": "nebula", "l": 84.66, "b": -3.52, "d": 2_590},
    {"name": "Tarantula Nebula", "alias": "NGC 2070", "kind": "nebula", "l": 279.46, "b": -31.67, "d": 160_000},
    {"name": "Crab Nebula", "alias": "M1", "kind": "remnant", "l": 184.56, "b": -5.78, "d": 6_500},
    {"name": "Veil Nebula", "alias": "NGC 6960", "kind": "remnant", "l": 74.23, "b": -8.61, "d": 2_400},
    {"name": "Helix Nebula", "alias": "NGC 7293", "kind": "planetary", "l": 36.16, "b": -57.12, "d": 655},
    {"name": "Ring Nebula", "alias": "M57", "kind": "planetary", "l": 63.17, "b": 13.98, "d": 2_570},
    {"name": "Dumbbell Nebula", "alias": "M27", "kind": "planetary", "l": 60.84, "b": -3.70, "d": 1_360},
    {"name": "Cat's Eye Nebula", "alias": "NGC 6543", "kind": "planetary", "l": 96.47, "b": 29.95, "d": 3_300},
    {"name": "Pleiades", "alias": "M45", "kind": "open", "l": 166.64, "b": -23.46, "d": 444},
    {"name": "Hyades", "alias": "Mel 25", "kind": "open", "l": 180.08, "b": -22.32, "d": 153},
    {"name": "Beehive Cluster", "alias": "M44", "kind": "open", "l": 205.92, "b": 32.48, "d": 577},
    {"name": "Coma Star Cluster", "alias": "Mel 111", "kind": "open", "l": 221.33, "b": 84.07, "d": 280},
    {"name": "Butterfly Cluster", "alias": "M6", "kind": "open", "l": 356.58, "b": -0.78, "d": 1_600},
    {"name": "Ptolemy Cluster", "alias": "M7", "kind": "open", "l": 355.79, "b": -4.50, "d": 980},
    {"name": "NGC 3532", "alias": "NGC 3532", "kind": "open", "l": 289.57, "b": 1.35, "d": 1_321},
    {"name": "Jewel Box", "alias": "NGC 4755", "kind": "open", "l": 303.20, "b": 2.50, "d": 6_400},
    {"name": "Wild Duck Cluster", "alias": "M11", "kind": "open", "l": 27.30, "b": -2.78, "d": 6_200},
    {"name": "Double Cluster", "alias": "NGC 869", "kind": "open", "l": 136.30, "b": -3.57, "d": 7_500},
    {"name": "Omega Centauri", "alias": "NGC 5139", "kind": "globular", "l": 309.10, "b": 14.97, "d": 17_090},
    {"name": "Great Cluster", "alias": "M13", "kind": "globular", "l": 59.01, "b": 40.91, "d": 22_200},
    {"name": "47 Tucanae", "alias": "NGC 104", "kind": "globular", "l": 305.89, "b": -44.89, "d": 13_000},
    {"name": "M4", "alias": "NGC 6121", "kind": "globular", "l": 350.97, "b": 15.97, "d": 7_200},
    {"name": "M22", "alias": "NGC 6656", "kind": "globular", "l": 9.89, "b": -7.55, "d": 10_600},
    {"name": "NGC 6397", "alias": "NGC 6397", "kind": "globular", "l": 338.17, "b": -11.96, "d": 7_800},
    {"name": "M5", "alias": "NGC 5904", "kind": "globular", "l": 3.86, "b": 46.80, "d": 24_500},
    {"name": "M15", "alias": "NGC 7078", "kind": "globular", "l": 65.01, "b": -27.31, "d": 33_600},
    {"name": "M2", "alias": "NGC 7089", "kind": "globular", "l": 53.37, "b": -35.77, "d": 37_500},
    {"name": "M79", "alias": "NGC 1904", "kind": "globular", "l": 227.23, "b": -29.35, "d": 41_000},
    {"name": "Intergalactic Wanderer", "alias": "NGC 2419", "kind": "globular", "l": 180.37, "b": 25.24, "d": 300_000},
    # Our own neighbourhood. The Sun is not in a star cluster: it sits inside the
    # Local Bubble, a low-density cavity blown by ancient supernovae, and the
    # nearest clusters are the Hyades and the Pleiades.
    {"name": "Local Bubble", "alias": "Local cavity", "kind": "structure", "l": 0.0, "b": 0.0, "d": 0.0, "radius": 500},
]

# Galaxies, built as oriented 3D star discs rather than camera-facing images.
# "display" is the distance we draw them at, in light-years: the satellites sit at
# their true distance, Andromeda and Triangulum are pulled in so they stay in frame,
# and labels always state the true distance. "size" is the real diameter.
# Each one is drawn as its photograph on a plane whose normal points back at the
# Sun, which is where the photograph was taken from, so the picture already carries
# the galaxy's real tilt. "inclination" and "pa" (position angle of the major axis,
# from celestial north) are kept as a record of that tilt; "imageScale" says how
# much wider than the galaxy its frame is, and "roll" spins the plane in place.
GALAXIES = [
    # no photograph reads as itself at this size, so it stays a diffuse glow
    {"name": "Sagittarius Dwarf", "alias": "SagDEG", "kind": "satellite", "type": "blob",
     "l": 5.57, "b": -14.17, "d": 65_000, "display": 65_000, "size": 16_000,
     "image": None, "colors": ["#ffe3c0", "#c9b5ff"]},
    {"name": "Large Magellanic Cloud", "alias": "LMC", "kind": "satellite", "type": "irregular",
     "l": 280.47, "b": -32.89, "d": 163_000, "display": 163_000, "size": 32_000,
     "inclination": 35.0, "pa": 170.0, "image": "lmc.jpg", "imageScale": 1.8,
     "colors": ["#fff0d6", "#9fc4ff"]},
    {"name": "Small Magellanic Cloud", "alias": "SMC", "kind": "satellite", "type": "irregular",
     "l": 302.80, "b": -44.30, "d": 200_000, "display": 200_000, "size": 18_000,
     "inclination": 60.0, "pa": 45.0, "image": "smc.jpg", "imageScale": 1.8,
     "colors": ["#ffeccf", "#a8c8ff"]},
    {"name": "Andromeda Galaxy", "alias": "M31", "kind": "spiral", "type": "spiral",
     "l": 121.17, "b": -21.57, "d": 2_537_000, "display": 1_250_000, "size": 152_000,
     "inclination": 77.0, "pa": 38.0, "image": "m31.jpg", "imageScale": 1.9,
     "colors": ["#ffd9a0", "#a9c7ff"]},
    {"name": "Triangulum Galaxy", "alias": "M33", "kind": "spiral", "type": "spiral",
     "l": 133.61, "b": -31.33, "d": 2_730_000, "display": 1_550_000, "size": 60_000,
     "inclination": 56.0, "pa": 23.0, "image": "m33.jpg", "imageScale": 1.9,
     "colors": ["#ffe6bb", "#93b9ff"]},
]

# Direction of the celestial north pole in galactic coordinates, which is what the
# position angles above are measured from.
CELESTIAL_POLE_GALACTIC = {"l": 122.93192, "b": 27.12825}

# Decorative far-field galaxies: real photographs on fixed, randomly oriented
# planes - not billboards - scattered rather than placed, so they carry no names
# and no distances.
BACKGROUND_GALAXY_IMAGES = ["spiral1.jpg", "spiral2.jpg", "m33.jpg", "m31.jpg"]

IMAGE_CREDITS = (
    "Milky Way backdrop: NASA/JPL-Caltech (R. Hurt). Far-field galaxy images: "
    "NASA/ESA Hubble, NASA/Spitzer, Adam Evans (CC BY 2.0)."
)
