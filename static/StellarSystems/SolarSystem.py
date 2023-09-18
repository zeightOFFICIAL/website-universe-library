from static.Types.SystemType import SystemClass
from static.Types.ObjectType import ObjectClass
from static.Types.PanelType import *

# COLORS
MAIN_COLORS = ["#FBAB7E", "#ff792b", "#FBAB7E"]

# MAIN PANELS
main0 = TopHeaderTextPanel(
    "MAINPANEL0",
    "Solar System",
    "The Solar System is the gravitationally bound system of the Sun and the objects that orbit it. It formed 4.6 billion years ago from the gravitational collapse of a giant interstellar molecular cloud. The vast majority of the system's mass is in the Sun, with most of the remaining mass contained in the planet Jupiter.",
    MAIN_COLORS,
    ["orange", "yellow"],
)
main1 = SimpleImagePanel(
    "MAINPANEL1",
    "https://uprostim.com/wp-content/uploads/2021/04/image047-25.jpg",
    MAIN_COLORS,
)
main2 = SimpleTextPanel(
    "MAINPANEL2",
    "Our solar system is made up of a star, eight planets, and countless smaller bodies such as dwarf planets, asteroids, and comets.",
    MAIN_COLORS,
    True,
)
main3 = SimpleTextPanel(
    "MAINPANEL2",
    "Our solar system orbits the center of the Milky Way galaxy at about 828,000 kph. We're in one of the galaxy's four spiral arms.",
    MAIN_COLORS,
    True,
)
main4 = PanelSlider("MAINPANEL2", [main2, main3], MAIN_COLORS)
main5 = SimpleImagePanel(
    "MAINPANEL3",
    "https://i.pinimg.com/originals/2b/a0/2f/2ba02f9fa48b4eb28be0666bf52259c4.jpg",
    MAIN_COLORS,
)
main6 = SimpleTextPanel(
    "MAINPANEL4",
    "The planets of our solar system – and even some asteroids – hold more than 200 moons in their orbits.",
    MAIN_COLORS,
    True,
)
main7 = SimpleTextPanel(
    "MAINPANEL4",
    "It takes our solar system about 230 million years to complete one orbit around the galactic center.",
    MAIN_COLORS,
    True,
)
main8 = SimpleTextPanel(
    "MAINPANEL4",
    "Our solar system is the only one known to support life. So far, we only know of life on Earth.",
    MAIN_COLORS,
    True,
)
main9 = SimpleTextPanel(
    "MAINPANEL4",
    "The four giant planets and at least one asteroid have rings. None are as spectacular as Saturn'sgorgeous rings.",
    MAIN_COLORS,
    True,
)
main10 = PanelSlider("MAINPANEL4", [main6, main7, main8, main9], MAIN_COLORS)

# PANELS
sun0 = HeaderTextPanel(
    "SUNPANEL0",
    "Sun",
    "The sun is a star located at the center of our solar system. It is a massive, nearly perfect sphere of hot plasma, with internal convective motion that generates a magnetic field. The sun's diameter is about 109 times that of Earth, and its mass is about 330,000 times greater than Earth's. The sun is primarily composed of hydrogen and helium, and it is extremely hot, with temperatures reaching millions of degrees Celsius in its core.",
    ["#fbff00", "#ff5e00", "#fbff00"],
    [],
    False,
    True,
    [
        "https://en.wikipedia.org/wiki/Sun",
        "https://solarsystem.nasa.gov/solar-system/sun/overview/",
        "https://www.newworldencyclopedia.org/entry/Sun",
    ],
)
sun1 = SimpleTextPanel(
    "SUNPANEL1",
    "The sun is essential for life on Earth, as it provides the energy necessary for photosynthesis, which is the process by which plants convert sunlight into food. Additionally, the sun has a major impact on Earth's climate and weather patterns, and its activity can cause phenomena such as solar flares and coronal mass ejections, which can affect communication and power systems on Earth.",
    MAIN_COLORS,
)
sun2 = SimpleImagePanel(
    "SUNPANEL2",
    "https://i.pinimg.com/originals/5d/77/6d/5d776d9a17a081984af7b5a55f65738b.jpg",
    MAIN_COLORS,
)
sun3 = SimpleImagePanel(
    "SUNPANEL3",
    "https://obshe.net/upload/000/u10/37/80/14d731ec.jpg",
    MAIN_COLORS,
    True,
)
sun4 = SimpleImagePanel(
    "SUNPANEL3",
    "https://mobimg.b-cdn.net/v3/fetch/53/5358df17c30f1881562c39f3042d5726.jpeg",
    MAIN_COLORS,
    True,
)
sun5 = SimpleImagePanel(
    "SUNPANEL3", "https://pixy.org/src2/602/6025447.jpg", MAIN_COLORS, True
)
sun6 = PanelSlider("SUNPANEL3", [sun3, sun4, sun5], MAIN_COLORS)
sun7 = SimpleTextPanel(
    "SUNPANEL4",
    "Every second, the Sun's core fuses about 600 million tons of hydrogen into helium, and in the process converts 4 million tons of matter into energy. This energy, which can take between 10,000 and 170,000 years to escape the core, is the source of the Sun's light and heat.",
    MAIN_COLORS,
)
sun8 = SimpleImagePanel(
    "SUNPANEL5",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Sun_poster.svg/500px-Sun_poster.svg.png",
    MAIN_COLORS,
)

merc0 = HeaderTextPanel(
    "MERCURYPANEL0",
    "Mercury",
    "Mercury is the smallest planet in our solar system and the closest planet to the sun. It is named after the Roman messenger god, Mercury, who was known for his speed and agility. Mercury is a rocky planet with a heavily cratered surface, much like Earth's moon. It has a very thin atmosphere composed mostly of helium and traces of sodium, potassium, and oxygen.",
    ["#c34b4b", "rgb(140 118 119)", "#c34b4b"],
    [],
    False,
    True,
    ["https://en.wikipedia.org/wiki/Mercury_(planet)"],
)
merc1 = SimpleTextPanel(
    "MERCURYPANEL1",
    "Mercury completes one orbit around the sun every 88 Earth days, which means that a year on Mercury is only about 88 Earth days long. However, because it rotates so slowly on its axis, a day on Mercury (the time it takes to complete one rotation) lasts about 176 Earth days. This means that one side of the planet is scorching hot, while the other side is incredibly cold.",
    MAIN_COLORS,
)
merc2 = SimpleImagePanel(
    "MERCURYPANEL2",
    "https://cdn2.radioromantika.ru/vardata/modules/news/files/1/3253/news_file_3253_5b6afa90004c3.jpg",
    MAIN_COLORS,
)
merc3 = CombinedSimplePanel(
    "MERCURYPANEL3",
    "Mercury has been visited by two spacecraft: Mariner 10 in 1974-75 and Messenger in 2008-2015. These missions provided us with valuable information about the planet's surface, geology, composition, and magnetic field.",
    "https://o-kosmose.ru/wp-content/uploads/2019/09/s1200(104).jpg",
    MAIN_COLORS,
    2,
)
merc4 = SimpleTextPanel(
    "MERCURYPANEL4",
    "Mercury takes about 88 Earth days to complete one orbit around the sun, but due to its close proximity to the sun, its year is only about 0.24 Earth years long. The planet rotates slowly on its axis, with one day on Mercury lasting about 59 Earth days. Because of its proximity to the sun, temperatures on Mercury can vary greatly, ranging from extremely hot during the day to extremely cold at night. The planet has no atmosphere to speak of, which means that there is no protection from the sun's radiation or from impacts by meteors and other space debris.",
    MAIN_COLORS,
)
merc5 = SimpleTextPanel(
    "MERCURYPANEL5",
    "Mercury rotates in a way that is unique in the Solar System. It is tidally locked with the Sun in a 3:2 spin–orbit resonance, meaning that relative to the fixed stars, it rotates on its axis exactly three times for every two revolutions it makes around the Sun. As seen from the Sun, in a frame of reference that rotates with the orbital motion, it appears to rotate only once every two Mercurian years. An observer on Mercury would therefore see only one day every two Mercurian years.",
    MAIN_COLORS,
)

ven0 = HeaderTextPanel(
    "VENUSPANEL0",
    "Venus",
    "Venus is the second planet from the sun and is known as the Earth's sister planet due to its similar size, composition, and proximity to the sun. Venus has a thick atmosphere composed mostly of carbon dioxide that causes a greenhouse effect, making it the hottest planet in the solar system with surface temperatures that can reach up to 864 degrees Fahrenheit (462 degrees Celsius).",
    ["#ffdfa5", "rgb(211 139 51)", "pink"],
    [],
    False,
    True,
    ["https://en.wikipedia.org/wiki/Venus"],
)
ven1 = CombinedSimplePanel(
    "VENUSPANEL1",
    "Venus has no moons or rings and rotates in the opposite direction to most other planets, which means that its day is longer than its year. It takes Venus about 243 Earth days to complete one rotation on its axis and about 225 Earth days to orbit around the sun.",
    "https://imagesbase.ru/uploads/posts/2020-01/1577880900_imagesbase.ru.jpg",
    MAIN_COLORS,
    2,
)
ven2 = SimpleTextPanel(
    "VENUSPANEL2",
    "Venus has been visited by several spacecraft, including the Soviet Union's Venera program and NASA's Magellan orbiter, which mapped the planet's surface with radar. The European Space Agency's Venus Express mission also studied the planet's atmosphere and climate.",
    MAIN_COLORS,
)
ven3 = CombinedSimplePanel(
    "VENUSPANEL3",
    "Venus rotates very slowly, taking about 243 Earth days to complete one rotation, but it orbits around the sun in only 225 Earth days. This means that a day on Venus (the time it takes to rotate once on its axis) is actually longer than a year on Venus (the time it takes to orbit around the sun).",
    "https://astronomy.com/~/media/E25B598FC280411696C0A3D5B3D92EED.jpg",
    MAIN_COLORS,
)
ven4 = SimpleTextPanel(
    "VENUSPANEL4",
    "The planet has been visited by several spacecraft, including the Soviet Union's Venera probes and NASA's Magellan orbiter, which have provided us with valuable information about its geology and surface features, such as mountains, volcanoes, and vast plains.",
    MAIN_COLORS,
)

moon0 = HeaderTextPanel(
    "MOONPNL0",
    "Moon",
    "The Moon is Earth's only natural satellite. Its diameter is about one-quarter the diameter of the Earth. The Moon is the fifth largest satellite in the Solar System. It is larger than any of the known dwarf planets and is the largest satellite relative to its parent planet. ons of the term. It lacks any significant atmosphere, hydrosphere, or magnetic field.",
    ["white", "grey", "white"],
    [],
    False,
    True,
    ["https://en.wikipedia.org/wiki/Moon"],
)
moon1 = CombinedHeaderPanel(
    "MOONPNL1",
    "Too Close To Not Love",
    "The surface of the Moon is rocky and dusty, with a lot of craters caused by meteor impacts. There are also mountains, valleys, and plains on the Moon's surface. One of the most famous features on the Moon's surface is the \"man in the Moon\" pattern, which is a result of the way that shadows fall on the lunar surface.",
    "https://i.pinimg.com/originals/60/bd/85/60bd8515c1f758d5d293daf3d1e6dc4a.jpg",
    MAIN_COLORS,
    ["white", "lightblue", "lightblue"],
    3,
)
moon2 = SimpleImagePanel(
    "MOONPNL2",
    "https://i.pinimg.com/originals/64/30/4f/64304fceab4a20259a100109ac62ce34.jpg",
    MAIN_COLORS,
    True,
)
moon3 = SimpleImagePanel(
    "MOONPNL2",
    "https://img3.goodfon.ru/original/1366x768/d/d6/luna-moon-zvezdy-lunnyy.jpg",
    MAIN_COLORS,
    True,
)
moon4 = SimpleImagePanel(
    "MOONPNL2",
    "https://i.pinimg.com/originals/12/71/af/1271afb2bb388862de4038f6e1e03166.jpg",
    MAIN_COLORS,
    True,
)
moon5 = SimpleImagePanel(
    "MOONPNL2",
    "https://i.pinimg.com/originals/e3/27/c2/e327c234ae4014ebdf1c16bb7740826a.jpg",
    MAIN_COLORS,
    True,
)
moon6 = SimpleImagePanel(
    "MOONPNL2",
    "https://all-aforizmy.ru/wp-content/uploads/2022/03/1614640423_1-p-fon-luni-dlya-fotoshopa-1.jpg",
    MAIN_COLORS,
    True,
)
moon7 = PanelSlider("MOONPNL2", [moon2, moon3, moon4, moon5, moon6], MAIN_COLORS)
moon8 = SimpleTextPanel(
    "MOONPNL3",
    "The Moon is a natural satellite of the Earth, meaning that it orbits around our planet. It is the fifth-largest moon in our solar system and the largest relative to the size of its host planet. The Moon is approximately 238,855 miles away from Earth and takes about 27.3 days to orbit once around our planet.",
    MAIN_COLORS,
)
moon9 = SimpleTextPanel(
    "MOONPNL4",
    "The Moon has no atmosphere, so there is no weather or wind on its surface. It is also very cold, with temperatures ranging from -173 degrees Celsius (-279 degrees Fahrenheit) at night to 127 degrees Celsius (261 degrees Fahrenheit) during the day. Despite these challenging conditions, several missions have been sent to the Moon by various countries, including manned missions by the United States.",
    MAIN_COLORS,
)

earth0 = HeaderTextPanel(
    "EARTHPANEL0",
    "Earth",
    "Earth is the third planet from the sun and the only known planet to support life. It has a diameter of approximately 12,742 kilometers and is located about 149.6 million kilometers away from the sun. Earth has a complex system of geology, atmosphere, and biology that together create a unique and diverse environment.",
    ["#1afcff", "rgb(92 100 255)", "#1afcff"],
    [],
    False,
    True,
    [
        "https://en.wikipedia.org/wiki/Earth",
        "https://solarsystem.nasa.gov/planets/earth/overview/",
        "https://www.britannica.com/place/Earth",
        "https://earth.google.com/web/@0,-11.6615,0a,22251752.77375655d,35y,0h,0t,0r",
    ],
)
earth1 = SimpleTextPanel(
    "EARTHPANEL1",
    "The planet is characterized by its solid surface, which is divided into continents and oceans. The atmosphere is composed mostly of nitrogen, oxygen, and trace amounts of other gases, which provide the air we breathe and protect us from harmful radiation from the sun. Earth's magnetic field also helps protect the planet from solar winds and other space weather phenomena.",
    MAIN_COLORS,
)
earth2 = SimpleImagePanel(
    "EARTHPANEL2",
    "https://theaustincommon.com/wp-content/uploads/2015/12/Earth.jpg",
    MAIN_COLORS,
)
earth3 = SimpleImagePanel(
    "EARTHPANEL3",
    "https://steamuserimages-a.akamaihd.net/ugc/931553779123923625/210C91D09AFC0384CD6C78D8955CE64C6DB9C167/?imw=512&amp;imh=340&amp;ima=fit&amp;impolicy=Letterbox&amp;imcolor=%23000000&amp;letterbox=true",
    MAIN_COLORS,
)
earth4 = CombinedHeaderPanel(
    "EARTHPANEL4",
    "The first/last stand",
    "Humans emerged 300,000 years ago, and have reached a population of almost 8 billion today. Humans depend on Earth's biosphere and natural resources for their survival, but have increasingly impacted Earth's environment.",
    "https://www.brianhonigman.com/wp-content/uploads/2015/10/Large-crowd-of-people-014.jpg",
    MAIN_COLORS,
    ["blue", "lightblue", "white"],
)
earth5 = CombinedSimplePanel(
    "EARTHPANEL5",
    "Today, humanity's impact on Earth's climate, soils, waters, and ecosystems is unsustainable, threatening people's lives and causing widespread extinction of other life.",
    "https://img2.thejournal.ie/article/5869397/river?version=5869398&width=1340",
    MAIN_COLORS,
)
earth6 = SimpleTextPanel(
    "EARTHPANEL6",
    "The Modern English word Earth developed, via Middle English, from an Old English noun most often spelled eorde. It has cognates in every Germanic language, and their ancestral root has been reconstructed. In its earliest attestation, the word eorde was already being used to translate the many senses of Latin terra and Greek: the ground, its soil, dry land, the human world, the surface of the world (including the sea), and the globe itself. As with Roman Terra/Tellus and Greek Gaia, Earth may have been a personified goddess in Germanic paganism: late Norse mythology included Jord ('Earth'), a giantess often given as the mother of Thor.",
    MAIN_COLORS,
)
earth7 = SimpleImagePanel(
    "EARTHPANEL7",
    "https://i.pinimg.com/originals/d7/d7/5c/d7d75c3e25335e55d06767571ce477cb.jpg",
    MAIN_COLORS,
)
earth8 = SimpleImagePanel(
    "EARTHPANEL8",
    "https://i.pinimg.com/originals/c2/5c/a2/c25ca205a16b7e0b48f78ab7f6388c42.png",
    MAIN_COLORS,
)
earth9 = SimpleTextPanel(
    "EARTHPANEL9",
    "The biosphere on Earth is incredibly diverse, with millions of species of plants and animals inhabiting virtually every corner of the planet. Humans are the dominant species on Earth, and our activities have had a significant impact on the environment.",
    MAIN_COLORS,
)
earth10 = SimpleTextPanel(
    "EARTHPANEL10",
    "Overall, Earth is a fascinating and complex place that continues to inspire curiosity and awe.",
    MAIN_COLORS,
)

phbs0 = HeaderTextPanel(
    "PHOBOSPANEL0",
    "Phobos and Deimos",
    "Phobos and Deimos are the two moons of Mars. They are relatively small compared to the planet they orbit, with Phobos being the larger of the two at about 22 kilometers in diameter, and Deimos being only about 12 kilometers in diameter. Both moons were discovered by American astronomer Asaph Hall in 1877.",
    ["white", "#aaa", "white"],
    [],
    False,
    True,
    [
        "https://en.wikipedia.org/wiki/Phobos_(moon)",
        "https://en.wikipedia.org/wiki/Deimos_(moon)",
    ],
)
phbs1 = CombinedHeaderPanel(
    "PHOBOSPANEL1",
    "Phobos",
    "Phobos orbits Mars at a distance of only about 6,000 kilometers, which is closer than any other moon in the solar system orbits its planet. It takes just 7 hours and 39 minutes for Phobos to complete one orbit around Mars. Due to its close proximity, Phobos orbits faster than Mars rotates on its axis, which means that from the perspective of an observer on the surface of Mars, Phobos rises in the west and sets in the east, moving across the sky in just a few hours.",
    "http://virtoo.ru/wp-content/uploads/2011/11/mx-phobos.jpg",
    MAIN_COLORS,
    [],
    1,
    True,
)
phbs2 = CombinedHeaderPanel(
    "PHOBOSPANEL1",
    "Deimos",
    "Deimos has a very irregular shape and is covered in craters, which suggests that it may be a captured asteroid or a piece of Mars that was ejected into orbit. It has a diameter of about 12 kilometers and orbits Mars at an average distance of 23,460 kilometers. Although Deimos is much smaller than Mars, its gravity is still strong enough to affect the planet's atmosphere. It also plays a role in the study of Mars, as its orbit can be used to measure the planet's mass and gravitational field.",
    "https://i.pinimg.com/originals/3f/37/b5/3f37b51be50c5b6931f3ac039d2bbfa8.jpg",
    MAIN_COLORS,
    [],
    1,
    True,
)
phbs3 = PanelSlider("PHOBOSPANEL1", [phbs1, phbs2], MAIN_COLORS)
phbs4 = SimpleImagePanel(
    "PHOBOSPANEL2",
    "https://o-kosmose.ru/wp-content/uploads/2019/10/maxresdefault(157).jpg",
    MAIN_COLORS,
)
phbs5 = SimpleImagePanel(
    "PHOBOSPANEL3", "http://kosmos-x.net.ru/_nw/59/90937030.jpg", MAIN_COLORS
)
phbs6 = SimpleTextPanel(
    "PHOBOSPANEL4",
    "Both moons are thought to be captured asteroids that were pulled into Mars' gravitational field early in the planet's history. Both moons were discovered in 1877 by Asaph Hall.",
    MAIN_COLORS,
)
phbs7 = SimpleTextPanel(
    "PHOBOSPANEL5",
    "Phobos is one of the darkest objects in the solar system, with a very low albedo, or reflectivity. Its surface is heavily cratered and marked by grooves and striations, possibly caused by the impact that created the Stickney crater, which dominates one end of the moon. Phobos orbits Mars at a distance of only 9,378 kilometers, completing one orbit every 7.7 hours. It is gradually getting closer to Mars and is expected to either crash into the planet or break apart to form a ring in the next 50 million years.",
    MAIN_COLORS,
)

mars0 = HeaderTextPanel(
    "MARSPANEL0",
    "Mars",
    'Mars is the fourth planet from the sun in our solar system and is often referred to as the "Red Planet" due to its rusty-red appearance. It has a thin atmosphere primarily composed of carbon dioxide, which makes it difficult for liquid water to exist on its surface. The surface of Mars is covered with canyons, valleys, and giant volcanoes, including Olympus Mons, the largest volcano in the solar system. Mars also has two small moons, Phobos and Deimos.',
    ["red", "#be1616", "red"],
    [],
    False,
    True,
    [
        "https://en.wikipedia.org/wiki/Mars",
        "https://www.newworldencyclopedia.org/entry/Mars",
    ],
)
mars1 = SimpleImagePanel(
    "MARSPANEL1",
    "https://pic.rutubelist.ru/video/e8/9a/e89afc2b37191e0684ac77a1a6744060.jpg",
    MAIN_COLORS,
)
mars2 = SimpleTextPanel(
    "MARSPANEL2",
    "Mars has been a focus of scientific exploration because of its potential to support life. NASA has sent several missions to Mars, including the Mars rovers Opportunity and Curiosity, to study the planet's geology, climate, and search for any signs of past or present life. There are also plans for future human missions to Mars, with the goal of establishing a permanent human settlement on the planet.",
    MAIN_COLORS,
)
mars3 = SimpleTextPanel(
    "MARSPANEL3",
    "One of the most interesting aspects of Mars is the possibility of finding evidence of past or present microbial life on the planet. NASA and other space agencies have sent numerous robotic missions to Mars over the years to study its geology, climate, and potential habitability. In recent years, there have also been plans by private companies like SpaceX to eventually send humans to Mars, although this is still in the early stages of development. Overall, Mars remains a fascinating subject of study and exploration for scientists and space enthusiasts alike.",
    MAIN_COLORS,
)
mars4 = CombinedHeaderPanel(
    "MARSPANEL4",
    "Pseudoscience",
    'The idea that Mars was populated by intelligent Martians became widespread in the late 19th century. Schiaparelli\'s "canali" observations combined with Percival Lowell\'s books on the subject put forward the standard notion of a planet that was a drying, cooling, dying world with ancient civilizations. Other observations added to what has been termed "Mars Fever".',
    "https://ic.pics.livejournal.com/tigerofsiberia/8415303/220545/220545_900.jpg",
    MAIN_COLORS,
    ["orangered", "green"],
)
mars5 = CombinedHeaderPanel(
    "MARSPANEL5",
    "Water on Mars",
    "There is evidence to suggest that there may be water on Mars. In fact, in 2015, NASA announced the discovery of hydrated salts on the surface of the planet, which are believed to have formed as a result of water flowing across the Martian surface. Additionally, there is strong evidence to suggest that there are subsurface reservoirs of water hidden beneath the Martian surface. This has been confirmed by a number of different studies, including measurements made by the Mars Reconnaissance Orbiter and the Mars Odyssey spacecraft.",
    "https://klike.net/uploads/posts/2023-01/1674455108_3-111.jpg",
    MAIN_COLORS,
    ["blue", "red"],
    2,
)
mars6 = CombinedSimplePanel(
    "MARSPANEL6",
    'Mars is named after the Roman god of war. This association between Mars and war dates back at least to Babylonian astronomy, in which the planet was named for the god Nergal, deity of war and destruction. It persisted into modern times, as exemplified by Gustav Holst\'s orchestral suite The Planets, whose famous first movement labels Mars "the bringer of war".',
    "https://upload.wikimedia.org/wikipedia/commons/f/f5/LouvreCoustouMars1.jpg",
    MAIN_COLORS,
)
mars7 = SimpleImagePanel(
    "MARSPANEL7",
    "https://damion.club/uploads/posts/2022-03/1646881817_33-damion-club-p-mars-krasivie-foto-36.jpg",
    MAIN_COLORS,
)
mars8 = SimpleImagePanel(
    "MARSPANEL8",
    "https://catherineasquithgallery.com/uploads/posts/2021-02/1612885197_41-p-oranzhevo-krasnii-fon-na-marse-62.jpg",
    MAIN_COLORS,
)

jup0 = HeaderTextPanel(
    "JUPPANEL0",
    "Jupiter",
    "Jupiter is the fifth planet from the Sun and the largest planet in our solar system. It is a gas giant, consisting mainly of hydrogen and helium, with a large and complex weather system featuring the famous Great Red Spot, a persistent anticyclonic storm in the planet's atmosphere. Jupiter has at least 79 moons, including four large Galilean moons discovered by Galileo Galilei in 1610: Io, Europa, Ganymede, and Callisto. These moons are some of the most fascinating objects in our solar system, with their own unique features and phenomena. Jupiter is also notable for its strong magnetic field, which creates intense radiation belts around the planet and makes Jupiter a dangerous environment for spacecraft to explore.",
    ["#ff8200", "#c5a572", "#ff8200"],
    [],
    False,
    True,
    [
        "https://en.wikipedia.org/wiki/Jupiter",
        "https://solarsystem.nasa.gov/planets/jupiter/overview/",
    ],
)
jup1 = CombinedSimplePanel(
    "JUPPANEL1",
    "One of the most notable features of Jupiter is its Great Red Spot, which is a massive storm that has been raging on the planet's surface for at least 350 years. The Great Red Spot is larger than the size of Earth and can be seen through a telescope from Earth.",
    "https://spacegid.com/wp-content/uploads/2014/11/Obrabotannyiy-snimok-Bolshogo-Krasnogo-Pyatna-na-YUpitere.jpg",
    MAIN_COLORS,
)
jup2 = SimpleTextPanel(
    "JUPPANEL2",
    "Jupiter's magnetic field is also incredibly strong, about 20,000 times stronger than Earth's magnetic field. This creates intense radiation belts around the planet that can be dangerous to spacecraft.",
    MAIN_COLORS,
)
jup3 = SimpleImagePanel(
    "JUPPANEL3",
    "https://mobimg.b-cdn.net/v3/fetch/ff/ff795cd1c96297def792e6b71e4fc3f5.jpeg",
    MAIN_COLORS,
)
jup4 = SimpleImagePanel(
    "JUPPANEL4",
    "https://fikiwiki.com/uploads/posts/2022-02/1644888184_9-fikiwiki-com-p-yupiter-krasivie-kartinki-11.jpg",
    MAIN_COLORS,
)
jup5 = SimpleMusicSlider(
    "JUPPANEL5",
    "http://www.astrosurf.com/luxorion/Radio/juno-plasma-near-eq-17-033-1246-1250.mp3",
    MAIN_COLORS,
)
jup6 = SimpleTextPanel(
    "JUPPANEL6",
    "Jupiter has at least 79 known moons, the four largest being Io, Europa, Ganymede, and Callisto. These four moons are known as the Galilean moons because they were first discovered by Galileo Galilei in 1610.",
    MAIN_COLORS,
)

sat0 = HeaderTextPanel(
    "SATURNPANEL0",
    "Saturn",
    "Saturn is the sixth planet from the Sun and the second-largest planet in our solar system, after Jupiter. It is a gas giant with an average radius about nine times that of Earth, and it has a prominent set of rings made up of ice particles, dust, and small rocks.",
    ["rgba(182, 115, 53, 1)", "rgba(255, 185, 151, 1)", "rgba(182, 115, 53, 1)"],
    [],
    False,
    True,
    [
        "https://en.wikipedia.org/wiki/Saturn",
        "https://solarsystem.nasa.gov/planets/saturn/overview/",
    ],
)
sat1 = SimpleTextPanel(
    "SATURNPANEL1",
    "Saturn takes about 29.5 Earth years to orbit the Sun, and it rotates on its axis once every 10.7 hours. Its atmosphere is mostly hydrogen and helium, with small amounts of other gases such as methane, ammonia, and water vapor. The clouds on Saturn are very dynamic, featuring many swirling storms and bands of different colors.",
    MAIN_COLORS,
)
sat2 = CombinedSimplePanel(
    "SATURNPANEL2",
    "Saturn's rings are one of the most striking features of the planet. They are made up of countless particles of ice and rock, ranging in size from tiny grains to large boulders, that orbit around Saturn in a flat disk-like structure.",
    "https://i.pinimg.com/originals/94/47/97/944797089d0ac281cd310d8b8c5f1701.jpg",
    MAIN_COLORS,
)
sat3 = SimpleImagePanel(
    "SATURNPANEL3",
    "https://kartinkin.net/uploads/posts/2021-07/1625675551_36-kartinkin-com-p-saturn-oboi-krasivie-38.jpg",
    MAIN_COLORS,
    True,
)
sat4 = SimpleImagePanel(
    "SATURNPANEL3",
    "https://kadet39.ru/wp-content/uploads/0/3/5/035bcdbed0d131e7366439962e2fee72.jpeg",
    MAIN_COLORS,
    True,
)
sat5 = SimpleImagePanel(
    "SATURNPANEL3",
    "https://kadet39.ru/wp-content/uploads/f/9/f/f9f9b92de3d666b4b1c068a3ebc9774b.jpeg",
    MAIN_COLORS,
    True,
)
sat6 = PanelSlider("SATURNPANEL3", [sat3, sat4, sat5], MAIN_COLORS)
sat7 = CombinedSimplePanel(
    "SATURNPANEL4",
    "Saturn has many moons - over 80 have been discovered so far - and some of them are quite large, with Titan being the largest moon in the solar system after Ganymede. Titan is also notable for having a thick atmosphere, lakes and seas of liquid methane and ethane on its surface, and possible subsurface oceans of water.",
    "https://i.sunhome.ru/journal/234/formirovanie-sputnikov-v-kolcah-saturna-v2.orig.jpg",
    MAIN_COLORS,
)
sat8 = SimpleTextPanel(
    "SATURNPANEL5",
    "Saturn was first observed by Galileo in 1610, but it wasn't until the 20th century that astronomers were able to study it in detail using telescopes and spacecraft. Many missions have visited Saturn, including NASA's Cassini spacecraft, which orbited the planet from 2004 to 2017 and provided us with a wealth of information about this fascinating world.",
    MAIN_COLORS,
)

ura0 = HeaderTextPanel(
    "URAPANEL0",
    "Uranus",
    "Uranus is the seventh planet from the Sun and the third-largest planet in our solar system. It is an ice giant, with a diameter of about four times that of Earth and a cloudy atmosphere composed mostly of hydrogen, helium, and methane.",
    ["rgba(134, 196, 255, 1)", "rgba(213, 206, 255, 1)", "rgba(134, 196, 255, 1)"],
    [],
    False,
    True,
    [
        "https://en.wikipedia.org/wiki/Uranus",
        "https://solarsystem.nasa.gov/planets/uranus/overview/",
    ],
)
ura1 = SimpleImagePanel(
    "URAPANEL1",
    "https://fikiwiki.com/uploads/posts/2022-02/1645007336_7-fikiwiki-com-p-kartinki-urana-8.jpg",
    MAIN_COLORS,
)
ura2 = CombinedSimplePanel(
    "URAPANEL2",
    "Uranus takes about 84 Earth years to complete one orbit around the Sun, and it rotates on its side, with its axis of rotation tilted at an angle of about 98 degrees relative to the plane of its orbit. This unusual orientation gives Uranus a very extreme seasonal cycle, with each pole experiencing more than 20 years of continuous sunlight or darkness during the course of its orbit.",
    "https://starcatalog.ru/images/2020/07/uran-2.jpg",
    MAIN_COLORS,
    2,
)
ura3 = SimpleTextPanel(
    "URAPANEL23",
    "Uranus has a system of faint rings, discovered in 1977 by astronomers studying the planet's atmosphere using telescopes. The rings are made up of dark particles, possibly consisting of organic compounds, and they are believed to have formed from the breakup of one or more small moons or moonlets.",
    MAIN_COLORS,
)
ura4 = CombinedSimplePanel(
    "URAPANEL4",
    "Uranus has 27 known moons, most of which are named after characters from the works of Shakespeare and Alexander Pope. The largest of these moons is Titania, which is about half the size of Earth's Moon.",
    "https://o-kosmose.ru/wp-content/uploads/2019/11/Uranus.jpg",
    MAIN_COLORS,
)
ura5 = SimpleTextPanel(
    "URAPANEL",
    "Despite being first observed in 1781 by astronomer William Herschel, Uranus remained poorly understood until the development of modern telescopes and space probes allowed scientists to study it in greater detail. NASA's Voyager 2 spacecraft flew by Uranus in 1986, providing us with much of our current knowledge of this fascinating planet.",
    MAIN_COLORS,
)

nep0 = HeaderTextPanel(
    "NEPPANEL0",
    "Neptune",
    "Neptune is the eighth and farthest known planet from the Sun in our solar system. It is a gas giant, meaning that it is composed mostly of hydrogen and helium with small amounts of methane and other trace gases.",
    ["rgba(99, 179, 255, 1)", "rgba(36, 0, 255, 1)", "rgba(99, 179, 255, 1)"],
    [],
    False,
    True,
    ["https://en.wikipedia.org/wiki/Neptune"],
)
nep1 = CombinedSimplePanel(
    "NEPPANEL1",
    "Neptune is about four times the size of Earth and takes almost 165 Earth years to orbit the Sun, making it the slowest-moving planet in the solar system. Its atmosphere is composed primarily of hydrogen and helium, with traces of water, ammonia, and methane. Like Uranus, Neptune also has an extreme tilt to its axis, which means that it experiences extreme seasons as well.",
    "https://phonoteka.org/uploads/posts/2021-05/1622272902_17-phonoteka_org-p-neptun-planeta-art-krasivo-17.jpg",
    MAIN_COLORS,
)
nep2 = SimpleImagePanel(
    "NEPPANEL2",
    "https://www.fonstola.ru/images/202008/fonstola.ru_404943.jpg",
    MAIN_COLORS,
)
nep3 = CombinedHeaderPanel(
    "NEPPANEL3",
    "Coldest out there",
    "Neptune is the coldest planet in our solar system. Its average temperature is about -353 degrees Fahrenheit (-214 degrees Celsius), which makes it even colder than Uranus, despite being slightly closer to the Sun. The extreme cold on Neptune is due to its great distance from the Sun, which means that it receives only a small amount of solar radiation to warm its atmosphere. The low temperatures also cause many of the gases in Neptune's atmosphere, such as methane and nitrogen, to freeze into solid form, creating a layer of ice on the planet's surface.",
    "https://d.ibtimes.co.uk/en/full/1607534/why-neptune-blue.jpg",
    MAIN_COLORS,
    ["blue", "white"],
)
nep4 = SimpleTextPanel(
    "NEPPANEL4",
    "Neptune was first observed in 1846, after astronomers used mathematical calculations to predict the existence of a previously unknown planet based on irregularities in the orbit of Uranus. The discovery of Neptune provided further evidence for the existence of the outer solar system and helped to refine our understanding of the laws that govern the motions of celestial bodies.",
    MAIN_COLORS,
)
nep5 = SimpleImagePanel(
    "NEPPANEL5",
    "https://bygirl.ru/wp-content/uploads/2021/08/r3m33oqkf.jpg",
    MAIN_COLORS,
)

jov0 = HeaderTextPanel(
    "JOVPANEL0",
    "Jovian moons",
    "Jovian moons are a group of natural satellites that orbit the planet Jupiter. There are currently 79 known Jovian moons, with the four largest and most well-known being Io, Europa, Ganymede, and Callisto. These moons were first discovered by Galileo Galilei in 1610, and have since been studied extensively by astronomers and space missions such as Voyager and Galileo. They are named after characters from Greek and Roman mythology associated with the god Jupiter or Zeus. The Jovian moons vary greatly in size, composition, and surface features, and they provide insight into the formation and evolution of the solar system.",
    ["yellow", "white", "white"],
    [],
    False,
    True,
    [
        "https://en.wikipedia.org/wiki/Io_(moon)",
        "https://en.wikipedia.org/wiki/Europa_(moon)",
        "https://en.wikipedia.org/wiki/Ganymede_(moon)",
        "https://en.wikipedia.org/wiki/Callisto_(moon)",
    ],
)
jov1 = CombinedHeaderPanel(
    "JOVPANEL1",
    "IO",
    "Io is one of the four largest moons of Jupiter, commonly known as the Galilean moons, named after their discoverer Galileo Galilei. Io is the closest of the four to Jupiter and is the fourth-largest moon in the solar system. It is a highly volcanic world with over 400 active volcanoes, which makes it the most geologically active object in our solar system. The activity on Io is caused by the strong gravitational interaction between Jupiter and its other Galilean moons, which creates tidal forces that generate tremendous internal heat within Io's interior. This heat drives volcanic activity that can produce plumes of gas and material that extend up to 300 kilometers into space. Io is also unique in that its surface is colored with bright yellow, orange, red, and white materials, making it one of the most visually striking objects in the solar system.",
    "https://cdn.futura-sciences.com/buildsv6/images/largeoriginal/0/e/8/0e808d5870_105168_io-pillan-patera-nasa-01.jpg",
    ["yellow", "white", "orange"],
    [],
    2,
    True,
)
jov2 = CombinedHeaderPanel(
    "JOVPANEL1",
    "Europa",
    "Europa is another one of the four largest moons of Jupiter, along with Io, Ganymede, and Callisto. It is the smallest of the four Galilean moons but has attracted a lot of attention from scientists due to its potential to harbor extraterrestrial life. Europa's surface is covered in a layer of ice that is thought to be around 15-25 kilometers thick. Underneath this icy crust lies an ocean of liquid water which is believed to be twice as large as all the oceans on Earth combined. The presence of this vast subsurface ocean, which is kept in a liquid state by tidal forces generated by Jupiter's gravity, makes Europa one of the most promising places in the solar system for the existence of life beyond Earth.",
    "https://kosmolog.ru/assets/images/kategorii/solnechnay_systema/evropa.jpg",
    ["white", "white", "lightblue"],
    [],
    2,
    True,
)
jov3 = CombinedHeaderPanel(
    "JOVPANEL1",
    "Ganymede",
    "Ganymede is the largest moon in the solar system and also one of the four Galilean moons of Jupiter. It is about 8% larger than the planet Mercury and is the only moon known to have its own magnetic field. Like Europa, Ganymede also has a subsurface ocean of liquid water beneath its icy crust. However, Ganymede's interior is divided into multiple layers, including a large metallic core, which generates the moon's magnetic field. The presence of this internal structure has made Ganymede a subject of particular interest to planetary scientists, who hope to learn more about its formation and composition. Ganymede's surface is marked by numerous impact craters, as well as complex systems of grooves and ridges that are believed to have formed due to tectonic activity.  The moon's terrain also includes dark regions known as \"galloping grooves,\" which are thought to be caused by the displacement of ice.",
    "https://steemitimages.com/DQmWiEQfbLqjr7tJykFhCqRDB1mk9bozdBV9G6MqARDQ1WQ/steemit-title-large.jpg",
    ["white", "grey", "lightred"],
    [],
    2,
    True,
)
jov4 = CombinedHeaderPanel(
    "JOVPANEL1",
    "Callisto",
    "Callisto is another one of the four Galilean moons of Jupiter, along with Io, Europa, and Ganymede. It is the second-largest moon of Jupiter and the third-largest moon in the solar system. Callisto's surface is heavily cratered and is believed to be one of the oldest surfaces in the solar system, dating back more than 4 billion years. The moon has a relatively low density compared to other moons, suggesting that it may have a higher proportion of ice than rock. Unlike the other Galilean moons, Callisto does not have any detectable internal activity, such as a subsurface ocean or volcanoes. However, it is thought to have a small, rocky core surrounded by a mixture of water ice and rock. Callisto has been visited by only one spacecraft so far – NASA's Galileo mission, which orbited Jupiter and its moons between 1995 and 2003. While Callisto is not currently considered a top priority for future exploration missions, it remains an object of interest to planetary scientists who hope to learn more about the early history and evolution of the solar system.",
    "https://mirkosmosa.ru/download/news/7/6912.jpg",
    ["grey", "yellow", "white"],
    [],
    2,
    True,
)
jov5 = PanelSlider("JOVPANEL1", [jov1, jov2, jov3, jov4], MAIN_COLORS)
jov6 = SimpleImagePanel(
    "JOVPANEL2",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Jupiter_irregular_moon_orbits_Jan_2021.png/1024px-Jupiter_irregular_moon_orbits_Jan_2021.png",
    MAIN_COLORS,
)
jov7 = SimpleTextPanel(
    "JOVPANEL3",
    "Jupiter has dozens of smaller moons that are collectively referred to as the Jovian moons. Some of the most notable of these include: Amalthea: a small, elongated moon with a reddish-brown color and a heavily cratered surface. Himalia: one of the largest Jovian moons, with a diameter of about 170 kilometers. It has a highly irregular shape and is thought to be a captured asteroid or Kuiper belt object. Metis: a small, irregularly-shaped moon that orbits Jupiter within its main ring system. Thebe: a small, irregularly-shaped moon with a heavily-cratered surface that orbits close to Jupiter's rings. Overall, the Jovian moons are a diverse group of objects with a wide range of sizes, shapes, and surface features. Many of these moons are thought to be captured asteroids or comets, and they provide valuable insights into the formation and evolution of the Jupiter system and the solar system as a whole.",
    MAIN_COLORS,
)

# OBJECTS
Sun = ObjectClass(
    "SUN",
    "Sun",
    "Star - Yellow Dwarf",
    ["8vh", "-4vh", "#fbff00", "#ff5e00", "20", "#ffa600"],
    ["0vh", "0vh"],
    "0",
    [sun0, sun1, sun2, sun6, sun7, sun8],
)

Mercury = ObjectClass(
    "MERC",
    "Mercury",
    "Rocky planet",
    ["2vh", "-1vh", "#c34b4b", "rgb(140 118 119)", "0", "#c34b4"],
    ["11vh", "-5.5vh"],
    "8",
    [merc0, merc2, merc3, merc4, merc5],
)

Venus = ObjectClass(
    "VEN",
    "Venus",
    "Greenhouse planet",
    ["4vh", "-2vh", "#ffdfa5", "rgb(211 139 51)", "5", "pink"],
    ["18vh", "-9vh"],
    "22",
    [ven0, ven1, ven2, ven3, ven4],
)

Moon = ObjectClass(
    "MOON",
    "Moon",
    "Rocky satelite",
    ["1vh", "-0.5vh", "white", "grey", "0", "white"],
    ["6vh", "-3vh"],
    "7",
    [moon0, moon1, moon7, moon8, moon9],
)

Earth = ObjectClass(
    "ERTH",
    "Earth",
    "Home",
    ["4vh", "-2vh", "#1afcff", "rgb(92 100 255)", "5", "#d7d9f5"],
    ["29vh", "-14.5vh"],
    "36",
    [
        earth0,
        earth1,
        earth2,
        earth3,
        earth4,
        earth5,
        earth6,
        earth7,
        earth8,
        earth9,
        earth10,
    ],
    [Moon],
)

Phobos = ObjectClass(
    "PHBS",
    "Phobos",
    "Rocky satelite",
    ["1vh", "-0.5vh", "white", "#aaa", "0", "white"],
    ["7vh", "-3.5vh"],
    "9",
    [phbs0, phbs3, phbs4, phbs5, phbs6, phbs7],
)

Mars = ObjectClass(
    "MARS",
    "Mars",
    "Rocky planet",
    ["3vh", "-1.5vh", "red", "#be1616", "5", "red"],
    ["44vh", "-22vh"],
    "68",
    [mars0, mars1, mars2, mars3, mars4, mars5, mars6, mars7, mars8],
    [Phobos],
)

Jovian = ObjectClass(
    "JOV",
    "Jovian",
    "Rocky Satelites",
    ["1vh", "-0.5vh", "white", "white", "white"],
    ["9vh", "-4.5vh"],
    "10",
    [jov0, jov5, jov6, jov7],
)

Jupiter = ObjectClass(
    "JUP",
    "Jupiter",
    "Gas giant",
    ["7vh", "-3.5vh", "#ff8200", "#c5a572", "10", "#ff8200"],
    ["59vh", "-29.5vh"],
    "433",
    [jup0, jup1, jup2, jup3, jup4, jup5, jup6],
    [Jovian],
)

Saturn = ObjectClass(
    "SAT",
    "Saturn",
    "Gas giant",
    [
        "6vh",
        "-3vh",
        "rgba(182, 115, 53, 1)",
        "rgba(255, 185, 151, 1)",
        "15",
        "rgba(182, 115, 53, 1)",
    ],
    ["73vh", "-36.5vh"],
    "1075",
    [sat0, sat1, sat2, sat6, sat7, sat8],
)

Uranus = ObjectClass(
    "URA",
    "Uranus",
    "Gas giant",
    [
        "3vh",
        "-1.5vh",
        "rgba(134, 196, 255, 1)",
        "rgba(213, 206, 255, 1)",
        "25",
        "#a490ff",
    ],
    ["83vh", "-41.5vh"],
    "3068",
    [ura0, ura1, ura2, ura3, ura4, ura5],
)

Neptune = ObjectClass(
    "NEP",
    "Neptune",
    "Gas giant",
    [
        "3vh",
        "-1.5vh",
        "rgba(99, 179, 255, 1)",
        "rgba(36, 0, 255, 1)",
        "25",
        "#2f00ff",
    ],
    ["92vh", "-46vh"],
    "6000",
    [nep0, nep1, nep2, nep3, nep4, nep5],
)

System = SystemClass(
    1,
    "Solar",
    [main0, main1, main4, main5, main10],
    [Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune],
    "icons/SolarIcon.ico",
    MAIN_COLORS,
)
