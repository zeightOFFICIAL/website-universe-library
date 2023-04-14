from static.Types.SystemType import SystemClass
from static.Types.ObjectType import ObjectClass
from static.Types.PanelType import *

fore_color = "#ff7500"
back_color = "red"

panel_main1 = TextPanel(1, "Alpha Centauri", "Alpha Centauri (Latinized from a Centauri and often abbreviated Alpha Cen or a Cen) is a triple star system in the constellation of Centaurus. It consists of 3 stars: Alpha Centauri A (officially Rigil Kentaurus), Alpha Centauri B (officially Toliman) and Alpha Centauri C (officially Proxima Centauri). Proxima Centauri is also the closest star to the Sun at 4.2465 light-years (1.3020 pc).", fore_color, back_color, fore_color)
panel_main2 = SimpleImagePanel(2, "../static/jpg/alphasystem/alphasystem1.jpg", fore_color, back_color, fore_color)
panel_main3 = SimpleImagePanel(3, "../static/jpg/alphasystem/alphasystem2.jpg", fore_color, back_color, fore_color)
    
Alpha = ObjectClass(1, "Alpha", 99, ["10vh", "-5vh", "#ffd000", "#f70", "30px"],
                                        ["2vh", "2vh", "-1vh", "-1vh"],
                                        ["2vh", "2vh", "-1vh", "-1vh", "10s", "100%"], [])
    


SystemObject = SystemClass(1, "Alpha Centauri", [panel_main1, panel_main2, panel_main3], [Alpha], "alternativeicon.ico") 