from static.Types.SystemType import SystemClass
from static.Types.ObjectType import ObjectClass
from static.Types.PanelType import *

# MAIN COLORS
fore_color = "#FF0000"
back_color = "#FF4500"

# MAIN PANELS
panel_starter = TextPanel("MPNL00", "Alpha Centauri", "Alpha Centauri is a star system located in the constellation of Centaurus, which is the closest star system to our own solar system. The system consists of three stars: Alpha Centauri A, Alpha Centauri B, and Proxima Centauri.", fore_color, back_color, fore_color)
panel_middle1 = SimpleImagePanel("MPNL01", "https://gamerwall.pro/uploads/posts/2022-02/1645544590_35-gamerwall-pro-p-alfa-tsentavra-zvezda-krasivie-oboi-46.jpg", fore_color, back_color, fore_color)
panel_middle2 = CombinedSimplePanel("MPNL02", "Alpha Centauri A and B are a binary star system, meaning they orbit around a common center of mass. Alpha Centauri A is a slightly larger and brighter star than our Sun, while Alpha Centauri B is slightly smaller and dimmer. Both stars are similar in age to our Sun and are estimated to be around 4.5 billion years old.", "https://www.astronomiskungdom.se/wp-content/uploads/2016/04/Sun-Alpha-Centauri.jpg", fore_color, back_color, fore_color)
panel_middle3_1 = SimpleTextPanel("MPNL03", "The Alpha Centauri system is made up of three stars: Alpha Centauri A, Alpha Centauri B, and Proxima Centauri.", fore_color, back_color, fore_color)
panel_middle3_2 = SimpleTextPanel("MPNL03", "Alpha Centauri A and B are a binary star system, meaning they orbit around a common center of mass.", fore_color, back_color, fore_color)
panel_middle3_3 = SimpleTextPanel("MPNL03", "In 2016, an Earth-sized exoplanet called Proxima b was discovered in the habitable zone of Proxima Centauri.", fore_color, back_color, fore_color)
panel_middle3_4 = SimpleTextPanel("MPNL03", "The Alpha Centauri system is believed to be a member of the Centaurus-Crux stellar association, a group of stars that formed together about 50 million years ago.", fore_color, back_color, fore_color)
panel_middle3 = PanelSlider("MPNL03", [panel_middle3_1, panel_middle3_2, panel_middle3_3, panel_middle3_4], fore_color, back_color)

# OBJECT PANELS

# OBJECTS

# SYSTEM
SystemObject = SystemClass(1, "Alpha Centauri", [panel_starter, panel_middle1, panel_middle2, panel_middle3], [], "alternativeicon.ico") 