from static.Types.SystemType import SystemClass
from static.Types.ObjectType import ObjectClass
from static.Types.PanelType import *

# COLORS
MAIN_COLOR = ["#FBAB7E","#F7CE68","#FBAB7E"]

# MAIN PANELS
panel_starter = TopHeaderTextPanel("MPNL00", "Solar System", "The Solar System is the gravitationally bound system of the Sun and the objects that orbit it. It formed 4.6 billion years ago from the gravitational collapse of a giant interstellar molecular cloud. The vast majority of the system's mass is in the Sun, with most of the remaining mass contained in the planet Jupiter.", MAIN_COLOR, ["orange", "yellow"])
panel_middle1 = SimpleImagePanel("MPNL01", "https://uprostim.com/wp-content/uploads/2021/04/image047-25.jpg", MAIN_COLOR)
panel_middle2_1 = SimpleTextPanel("MPNL02", "Our solar system is made up of a star, eight planets, and countless smaller bodies such as dwarf planets, asteroids, and comets.", MAIN_COLOR, True)
panel_middle2_2 = SimpleTextPanel("MPNL02", "Our solar system orbits the center of the Milky Way galaxy at about 828,000 kph. We're in one of the galaxy's four spiral arms.", MAIN_COLOR, True)
panel_middle2 = PanelSlider("MPNL02", [panel_middle2_1, panel_middle2_2], MAIN_COLOR)
panel_middle3 = SimpleImagePanel("MPNL03", "https://i.pinimg.com/originals/2b/a0/2f/2ba02f9fa48b4eb28be0666bf52259c4.jpg", MAIN_COLOR)
panel_middle4_1 = SimpleTextPanel("MPNL04", "The planets of our solar system – and even some asteroids – hold more than 200 moons in their orbits.", MAIN_COLOR, True)
panel_middle4_2 = SimpleTextPanel("MPNL04", "It takes our solar system about 230 million years to complete one orbit around the galactic center.", MAIN_COLOR, True)
panel_middle4_3 = SimpleTextPanel("MPNL04", "Our solar system is the only one known to support life. So far, we only know of life on Earth.", MAIN_COLOR, True)
panel_middle4_4 = SimpleTextPanel("MPNL04", "The four giant planets and at least one asteroid have rings. None are as spectacular as Saturn'sgorgeous rings.", MAIN_COLOR, True)
panel_middle4 = PanelSlider("MPNL04", [panel_middle4_1, panel_middle4_2, panel_middle4_3, panel_middle4_4], MAIN_COLOR)

# PANELS
sun_starter = HeaderTextPanel("SPNL00", "Sun", "The sun is a star located at the center of our solar system. It is a massive, nearly perfect sphere of hot plasma, with internal convective motion that generates a magnetic field. The sun's diameter is about 109 times that of Earth, and its mass is about 330,000 times greater than Earth's. The sun is primarily composed of hydrogen and helium, and it is extremely hot, with temperatures reaching millions of degrees Celsius in its core.", MAIN_COLOR, ["orange", "yellow"], False, True, [])
sun_middle1 = SimpleTextPanel("SPNL01", "The sun is essential for life on Earth, as it provides the energy necessary for photosynthesis, which is the process by which plants convert sunlight into food. Additionally, the sun has a major impact on Earth's climate and weather patterns, and its activity can cause phenomena such as solar flares and coronal mass ejections, which can affect communication and power systems on Earth.", MAIN_COLOR)
sun_middle2 = SimpleImagePanel("SPNL02", "https://i.pinimg.com/originals/5d/77/6d/5d776d9a17a081984af7b5a55f65738b.jpg", MAIN_COLOR)
sun_middle3_1 = SimpleImagePanel("SPNL03", "https://get.pxhere.com/photo/beach-sea-coast-nature-ocean-horizon-sky-sun-sunrise-sunset-sunlight-dawn-atmosphere-dusk-evening-afterglow-red-sky-at-morning-771530.jpg", MAIN_COLOR, True)
sun_middle3_2 = SimpleImagePanel("SPNL03", "https://mobimg.b-cdn.net/v3/fetch/53/5358df17c30f1881562c39f3042d5726.jpeg", MAIN_COLOR, True)
sun_middle3_3 = SimpleImagePanel("SPNL03", "https://pixy.org/src2/602/6025447.jpg", MAIN_COLOR, True)
sun_middle3 = PanelSlider("SPNL03", [sun_middle3_1, sun_middle3_2, sun_middle3_3], MAIN_COLOR)
sun_middle4 = SimpleTextPanel("SPNL04", "Every second, the Sun's core fuses about 600 million tons of hydrogen into helium, and in the process converts 4 million tons of matter into energy. This energy, which can take between 10,000 and 170,000 years to escape the core, is the source of the Sun's light and heat.", MAIN_COLOR)
sun_middle5 = SimpleImagePanel("SPNL05", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Sun_poster.svg/500px-Sun_poster.svg.png", MAIN_COLOR)

# OBJECTS

Sun = ObjectClass("SUN", "Sun",
                  ["8vh", "-4vh", "#fbff00", "red", "20px", "#ffa600"],
                  ["0vh", "0vh"],
                  ["0vh", "0vh", "0"],
                  [sun_starter, sun_middle1, sun_middle2, sun_middle3, sun_middle4, sun_middle5], 100, "Star - Yellow dwarf", [])

Mercury = ObjectClass("MERC", "Mercury",
                      ["2vh", "-1vh", "#964747", "rgba(107,72,72,1)", "0px", "#964747"],
                      ["11vh", "-5.5vh"],
                      ["11vh", "-5.5vh", "8"],
                      [], 99, "Rocky planet", [])

Venus = ObjectClass("VEN", "Venus",
                    ["4vh", "-2vh", "#ffe2b0", "rgb(255, 230, 255, 1)", "5px", "pink"],
                    ["18vh", "-9vh"],
                    ["18vh", "-9vh", "22"],
                    [], 98, "Greenhouse planet", [])

Moon = ObjectClass("MOON", "Moon",
                   ["1vh", "-0.5vh", "grey", "white", "0px", "grey"],
                   ["6vh", "-3vh"],
                   ["6vh", "-3vh", "3"],
                   [], 95, "Satelite", [])

Earth = ObjectClass("ERTH", "Earth",
                    ["4vh", "-2vh", "#1afcff", "rgba(122, 128, 255, 1)", "5px", "#d7d9f5"],
                    ["29vh", "-14.5vh"],
                    ["29vh", "-14.5vh", "36"],
                    [], 97, "Exoplanet - Habitable", [Moon])

Phobos = ObjectClass("PHBS", "Phobos",
                     ["1vh", "-0.5vh", "#aaa", "#aaa", "0px", "#aaa"],
                     ["7vh", "-3.5vh"],
                     ["7vh", "-3.5vh", "1"],
                     [], 91, "Satelite", [])

Mars = ObjectClass("MARS", "Mars", 
                   ["3vh", "-1.5vh", "red", "#be1616", "5px", "red"],
                   ["44vh", "-22vh"],
                   ["44vh", "-22vh", "68"],
                   [], 93, "Rocky planet", [Phobos])


SystemObject = SystemClass(2, "Solar System", 
                            [panel_starter, panel_middle1, panel_middle2, panel_middle3, panel_middle4], 
                            [Sun, Mercury, Venus, Earth, Mars], 
                            "icons/SolarIcon.ico", MAIN_COLOR) 