from static.Types.SystemType import SystemClass
from static.Types.ObjectType import ObjectClass
from static.Types.PanelType import *

# COLORS
MAIN_COLOR = ["#FF0000","#FF4500","#FF0000"]
HEAD_COLOR = ["RED", "ORANGE", "RED"]

# MAIN PANELS
panel_starter = TopHeaderTextPanel("MPNL00", "Alpha Centauri", "Alpha Centauri is a star system located in the constellation of Centaurus, which is the closest star system to our own solar system. The system consists of three stars: Alpha Centauri A, Alpha Centauri B, and Proxima Centauri.", MAIN_COLOR, HEAD_COLOR)
panel_middle1 = SimpleImagePanel("MPNL01", "https://gamerwall.pro/uploads/posts/2022-02/1645544590_35-gamerwall-pro-p-alfa-tsentavra-zvezda-krasivie-oboi-46.jpg", MAIN_COLOR)
panel_middle2 = CombinedSimplePanel("MPNL02", "Alpha Centauri A and B are a binary star system, meaning they orbit around a common center of mass. Alpha Centauri A is a slightly larger and brighter star than our Sun, while Alpha Centauri B is slightly smaller and dimmer. Both stars are similar in age to our Sun and are estimated to be around 4.5 billion years old.", "https://www.astronomiskungdom.se/wp-content/uploads/2016/04/Sun-Alpha-Centauri.jpg", MAIN_COLOR)
panel_middle3_1 = SimpleTextPanel("MPNL03", "The Alpha Centauri system is made up of three stars: Alpha Centauri A, Alpha Centauri B, and Proxima Centauri.", MAIN_COLOR, True)
panel_middle3_2 = SimpleTextPanel("MPNL03", "Alpha Centauri A and B are a binary star system, meaning they orbit around a common center of mass.", MAIN_COLOR, True)
panel_middle3_3 = SimpleTextPanel("MPNL03", "In 2016, an Earth-sized exoplanet called Proxima b was discovered in the habitable zone of Proxima Centauri.", MAIN_COLOR, True)
panel_middle3_4 = SimpleTextPanel("MPNL03", "The Alpha Centauri system is believed to be a member of the Centaurus-Crux stellar association.", MAIN_COLOR, True)
panel_middle3 = PanelSlider("MPNL03", [panel_middle3_1, panel_middle3_2, panel_middle3_3, panel_middle3_4], MAIN_COLOR)
panel_middle4 = CombinedHeaderPanel("MPNL04", "Almost there", "There has been much interest in Alpha Centauri as a possible destination for interstellar exploration and colonization due to its proximity to our solar system. In fact, several proposed interstellar missions have included Alpha Centauri as a target, such as Breakthrough Starshot, which aims to send tiny spacecraft to the star system using laser propulsion. Additionally, the possibility of habitable planets in the Alpha Centauri system has also been explored, and in 2016, an Earth-sized exoplanet was discovered in the habitable zone of Proxima Centauri.", "https://nypost.com/wp-content/uploads/sites/2/2022/03/Space-sex-feature.jpg?quality=75&amp;strip=all&amp;w=1024", MAIN_COLOR, ["white", "white"])

# OBJECT PANELS
alpha_starter = HeaderTextPanel("APNL00", "Alpha", "Alpha Centauri A is one of the three stars in the Alpha Centauri star system, and it is the brightest and largest of the three. It is a yellow dwarf star, similar to our own Sun, with a mass of about 1.1 times that of the Sun and a radius of about 1.2 times that of the Sun.", MAIN_COLOR, ["orangered", "yellow"])

# OBJECTS
pbetd = ObjectClass("PROXD", "Proxima D", 95,
                    ['10vh', '-5vh', '#ffd000', '#f70', '30px'],
                    ['2vh', '2vh', '-1vh', '-1vh'],
                    ['2vh', '2vh', "-1vh", '-1vh', '10s', '100%'],
                    [alpha_starter])
alpha = ObjectClass("ALPHA", "Alpha", 99, 
                    ['10vh', '-5vh', '#ffd000', '#f70', '30px'],
                    ['2vh', '2vh', '-1vh', '-1vh'],
                    ['2vh', '2vh', "-1vh", '-1vh', '10s', '100%'],
                    [alpha_starter])
beta  = ObjectClass("BETA", "Beta", 98,
                    ['7vh', '-3.5vh', '#ff9100', '#f70', '20px'],
                    ['20vh', '20vh', '-10vh', '-10vh'],
                    ['20vh', '20vh', "-10vh", '-10vh', '45s', '100%'],
                    [alpha_starter])
prox  = ObjectClass("PROX", "Proxima", 97,
                    ['4vh', '-2vh', 'red', '#61', '20px'],
                    ['64vh', '64vh', '-32vh', '-32vh'],
                    ['64vh', '64vh', "-32vh", '-32vh', '325s', '100%'],
                    [alpha_starter])

# SYSTEM
SystemObject = SystemClass(1, "Alpha Centauri", [panel_starter, panel_middle1, panel_middle2, panel_middle3, panel_middle4], [alpha, beta, prox], "alternativeicon.ico", MAIN_COLOR) 