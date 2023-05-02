from static.Types.SystemType import SystemClass
from static.Types.ObjectType import ObjectClass
from static.Types.PanelType import *

# COLORS
MAIN_COLOR = ["#FF0000","#FF4500","#FF0000"]

# MAIN PANELS
panel_starter = TopHeaderTextPanel("MPNL00", "Alpha Centauri", "Alpha Centauri is a star system located in the constellation of Centaurus, which is the closest star system to our own solar system. The system consists of three stars: Alpha Centauri A, Alpha Centauri B, and Proxima Centauri.", MAIN_COLOR, ["orange", "red", "orange"])
panel_middle1 = SimpleImagePanel("MPNL01", "https://gamerwall.pro/uploads/posts/2022-02/1645544590_35-gamerwall-pro-p-alfa-tsentavra-zvezda-krasivie-oboi-46.jpg", MAIN_COLOR)
panel_middle2 = CombinedSimplePanel("MPNL02", "Alpha Centauri A and B are a binary star system, meaning they orbit around a common center of mass. Alpha Centauri A is a slightly larger and brighter star than our Sun, while Alpha Centauri B is slightly smaller and dimmer. Both stars are similar in age to our Sun and are estimated to be around 4.5 billion years old.", "https://www.astronomiskungdom.se/wp-content/uploads/2016/04/Sun-Alpha-Centauri.jpg", MAIN_COLOR)
panel_middle3_1 = SimpleTextPanel("MPNL03", "The Alpha Centauri system is made up of three stars: Alpha Centauri A, Alpha Centauri B, and Proxima Centauri.", MAIN_COLOR, True)
panel_middle3_2 = SimpleTextPanel("MPNL03", "Alpha Centauri A and B are a binary star system, meaning they orbit around a common center of mass.", MAIN_COLOR, True)
panel_middle3_3 = SimpleTextPanel("MPNL03", "In 2016, an Earth-sized exoplanet called Proxima b was discovered in the habitable zone of Proxima Centauri.", MAIN_COLOR, True)
panel_middle3_4 = SimpleTextPanel("MPNL03", "The Alpha Centauri system is believed to be a member of the Centaurus-Crux stellar association.", MAIN_COLOR, True)
panel_middle3 = PanelSlider("MPNL03", [panel_middle3_1, panel_middle3_2, panel_middle3_3, panel_middle3_4], MAIN_COLOR)
panel_middle4 = CombinedHeaderPanel("MPNL04", "Almost there", "There has been much interest in Alpha Centauri as a possible destination for interstellar exploration and colonization due to its proximity to our solar system. In fact, several proposed interstellar missions have included Alpha Centauri as a target, such as Breakthrough Starshot, which aims to send tiny spacecraft to the star system using laser propulsion. Additionally, the possibility of habitable planets in the Alpha Centauri system has also been explored, and in 2016, an Earth-sized exoplanet was discovered in the habitable zone of Proxima Centauri.", "https://nypost.com/wp-content/uploads/sites/2/2022/03/Space-sex-feature.jpg?quality=75&amp;strip=all&amp;w=1024", MAIN_COLOR, ["white", "white"])
panel_middle5_1 = SimpleImagePanel("MPNL05", "https://i.pinimg.com/originals/35/f7/93/35f793477b6391a06d497234030fa51d.jpg", MAIN_COLOR, True)
panel_middle5_2 = SimpleImagePanel("MPNL05", "https://www.mirf.ru/wp-content/uploads/2016/09/Proxima-b-3-2048x1330.jpg", MAIN_COLOR, True)
panel_middle5_3 = SimpleImagePanel("MPNL05", "https://i.ytimg.com/vi/p0jVtw2UiO0/maxresdefault.jpg", MAIN_COLOR, True)
panel_middle5 = PanelSlider("MPNL05", [panel_middle5_1, panel_middle5_2, panel_middle5_3], MAIN_COLOR)
panel_middle6 = SimpleImagePanel("MPNL06", "https://qph.cf2.quoracdn.net/main-qimg-eaa83733f851357753819fa41973b423", MAIN_COLOR)

# OBJECT PANELS
alpha_starter = HeaderTextPanel("APNL00", "Alpha", "Alpha Centauri A is one of the three stars in the Alpha Centauri star system, and it is the brightest and largest of the three. It is a yellow dwarf star, similar to our own Sun, with a mass of about 1.1 times that of the Sun and a radius of about 1.2 times that of the Sun.", ["#ffd000", "f70", "#ffd000"], [], False, True, ["https://en.wikipedia.org/wiki/Alpha_Centauri"])
alpha_middle1 = SimpleTextPanel("APNL01", "Alpha Centauri A, also known as Rigil Kentaurus, is the principal member, or primary, of the binary system. It is a solar-like main-sequence star with a similar yellowish colour, whose stellar classification is spectral type G2-V; it is about 10% more massive than the Sun, with a radius about 22% larger. When considered among the individual brightest stars in the night sky, it is the fourth-brightest at an apparent magnitude of +0.01, being slightly fainter than Arcturus at an apparent magnitude of -0.05.", MAIN_COLOR)
alpha_middle2 = SimpleImagePanel("APNL02", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Alpha%2C_Beta_and_Proxima_Centauri_%281%29.jpg/1024px-Alpha%2C_Beta_and_Proxima_Centauri_%281%29.jpg", MAIN_COLOR)
alpha_middle3 = SimpleTextPanel("APNL03", "The type of magnetic activity on Alpha Centauri A is comparable to that of the Sun, showing coronal variability due to star spots, as modulated by the rotation of the star. However, since 2005 the activity level has fallen into a deep minimum that might be similar to the Sun's historical Maunder Minimum. Alternatively, it may have a very long stellar activity cycle and is slowly recovering from a minimum phase.", MAIN_COLOR)
alpha_middle4 = CombinedSimplePanel("APNL04", "Asteroseismic studies, chromospheric activity, and stellar rotation (gyrochronology) are all consistent with the Alpha Centauri system being similar in age to, or slightly older than, the Sun. Asteroseismic analyses that incorporate tight observational constraints on the stellar parameters for the Alpha Centauri stars have yielded age estimates of 4.85±0.5 Gyr, 5.0±0.5 Gyr, 5.2 ± 1.9 Gyr, 6.4 Gyr, and 6.52±0.3 Gyr. Age estimates for the stars based on chromospheric activity (Calcium H & K emission) yield 4.4 ± 2.1 Gyr, whereas gyrochronology yields 5.0±0.3 Gyr. Stellar evolution theory implies both stars are slightly older than the Sun at 5 to 6 billion years, as derived by their mass and spectral characteristics.","https://scilogs.spektrum.de/himmelslichter/wp-content/blogs.dir/151/files/Alpha_Centauri_AB_1200px.jpg", MAIN_COLOR)

beta_starter = HeaderTextPanel("BPNL00", "Beta", "Alpha Centauri B, also known as Toliman, is the secondary star of the binary system. It is a main-sequence star of spectral type K1-V, making it more an orange colour than Alpha Centauri A; it has around 90% of the mass of the Sun and a 14% smaller diameter. Although it has a lower luminosity than A, Alpha Centauri B emits more energy in the X-ray band.", ["#ff9100","#f70", "#ff9100"], [], False, True)
beta_middle1_1 = SimpleTextPanel("BPNL01", "The A and B components of Alpha Centauri have an orbital period of 79.762 years. Their orbit is moderately eccentric, as it has an eccentricity of almost 0.52; their closest approach or periastron is 11.2 AU, or about the distance between the Sun and Saturn; and their furthest separation or apastron is 35.6 AU, about the distance between the Sun and Pluto.", MAIN_COLOR, True)
beta_middle1_2 = SimpleTextPanel("BPNL01", "Its light curve varies on a short time scale, and there has been at least one observed flare. It is more magnetically active than Alpha Centauri A, showing a cycle of 8.2±0.2 yr compared to 11 years for the Sun, and has about half the minimum-to-peak variation in coronal luminosity of the Sun. Alpha Centauri B has an apparent magnitude of +1.35.", MAIN_COLOR, True)
beta_middle1 = PanelSlider("BPNL01", [beta_middle1_1, beta_middle1_2], MAIN_COLOR)
beta_middle2 = SimpleImagePanel("BPNL02", "https://static.wikia.nocookie.net/remixfavoriteshowandgame/images/2/20/Alpha_Centauri_Bb.jpg/revision/latest?cb=20161208143541", MAIN_COLOR)
beta_middle3 = SimpleImagePanel("BPNL03", "https://images.techinsider.ru/upload/img_cache/9ab/9ab548ce1764cea87d7522892a89b532_ce_700x438x0x0_cropped_1332x888.jpg", MAIN_COLOR)

prox_starter = HeaderTextPanel("PPNL00", "Proxima", "Proxima Centauri is a small, low-mass star located 4.2465 light-years (1.3020 pc) away from the Sun in the southern constellation of Centaurus. Its Latin name means the 'nearest [star] of Centaurus'. It was discovered in 1915 by Robert Innes and is the nearest-known star to the Sun. With a quiescent apparent magnitude of 11.13, it is too faint to be seen with the unaided eye. Proxima Centauri is a member of the Alpha Centauri star system, being identified as component Alpha Centauri C, and is 2.18° to the southwest of the Alpha Centauri AB pair. It is currently 12,950 AU (0.2 ly) from AB, which it orbits with a period of about 550,000 years.", ["red","#61", "red"], [], False, True, ["https://en.wikipedia.org/wiki/Proxima_Centauri", "https://space.fandom.com/wiki/Proxima_Centauri"])
prox_middle1 = SimpleImagePanel("PPNL01", "https://kids.pplware.sapo.pt/wp-content/uploads/2017/11/Ross128b_3.jpg", MAIN_COLOR)
prox_middle2 = CombinedHeaderPanel("PPNL02", "Red dwarf", "Proxima Centauri is a red dwarf star with a mass about 12.5% of the Sun's mass (M☉), and average density about 33 times that of the Sun. Because of Proxima Centauri's proximity to Earth, its angular diameter can be measured directly. Its actual diameter is about one-seventh (14%) the diameter of the Sun. Although it has a very low average luminosity, Proxima Centauri is a flare star that randomly undergoes dramatic increases in brightness because of magnetic activity.", "https://upload.wikimedia.org/wikipedia/commons/9/95/New_shot_of_Proxima_Centauri%2C_our_nearest_neighbour.jpg", MAIN_COLOR, ["red", "orangered"])
prox_middle3 = SimpleTextPanel("PPNL03", "A red dwarf with the mass of Proxima Centauri will remain on the main sequence for about four trillion years. As the proportion of helium increases because of hydrogen fusion, the star will become smaller and hotter, gradually transforming into a so-called \"blue dwarf\". Near the end of this period it will become significantly more luminous, reaching 2.5% of the Sun's luminosity (L☉) and warming up any orbiting bodies for a period of several billion years. When the hydrogen fuel is exhausted, Proxima Centauri will then evolve into a helium white dwarf (without passing through the red giant phase) and steadily lose any remaining heat energy.", MAIN_COLOR)
prox_middle4 = SimpleImagePanel("PPNL04", "https://thealphacentauri.net/wp-content/uploads/2021/11/alSvAmS-Imgur-scaled.jpg", MAIN_COLOR)

proxc_starter = HeaderTextPanel("PcPNL00", "Proxima C", "The putative planet has been dubbed \"Proxima c\", but it has not yet been confirmed through independent observations or follow-up studies. If it does exist, Proxima c is thought to be a super-Earth with a mass between 5 and 10 times that of Earth, and it would orbit its star at a distance of roughly 1.5 astronomical units (AU) - about the same distance as Mars orbits our Sun.", ["#0051ff","#1e0ff", "#0051ff"], [], False, True)
proxc_middle1 = SimpleTextPanel("PcPNL01", "However, because the existence of Proxima c is still uncertain, and we don't know much about its properties, it's difficult to say whether it would be habitable or not. Further observations and analyses will be needed to confirm the existence of this planet and to better understand its potential for habitability.", MAIN_COLOR)
proxc_middle2 = SimpleImagePanel("PcPNL02", "https://preview.redd.it/ptgq8tn5k6s21.png?auto=webp&s=a19a0f86c50717e14d799c803015d83e95bbb824", MAIN_COLOR)
proxc_middle3 = SimpleImagePanel("PcPNL03", "https://2ch.hk/tv/src/3030035/16741761504620.png", MAIN_COLOR)
proxc_middle4 = SimpleTextPanel("PcPNL04", "One interesting possibility is that Proxima c could have a thick atmosphere that would help to insulate the planet and regulate its temperature. This could make it more hospitable for life, despite being located farther away from its star than Proxima b. However, this is purely speculative at this point, as we don't yet know enough about the planet to say for sure. Another factor that could influence the potential habitability of Proxima c is the activity of its host star. As I mentioned earlier, Proxima Centauri is a red dwarf star, which means that it can be prone to flares and other types of activity that could be harmful to any potential surface life. If Proxima c exists and is within the habitable zone of its star, these effects could be mitigated by a thick atmosphere or magnetic field, but we don't yet know whether either of these conditions exists on the planet.", MAIN_COLOR)

proxb_starter = HeaderTextPanel("PbPNL00", "Proxima B", "Proxima b is an exoplanet that orbits the star Proxima Centauri, which is the closest star to our Solar System. It was discovered in August 2016 and is about 1.3 times the mass of Earth. Proxima b is located in the habitable zone of its star, which means that it receives just the right amount of warmth from its star to allow liquid water to exist on its surface, making it a prime candidate for the search for extraterrestrial life. However, much remains unknown about the conditions on Proxima b, and further research is needed to determine whether it has an atmosphere and whether it could support life as we know it.", ["#ffadad","#ffd9a7", "#ffadad"], [], False, True)
proxb_middle1 = CombinedSimplePanel("PbPNL01", "Based on its mass and distance from its star, scientists believe that Proxima b is a rocky planet with a surface temperature that could allow water to exist in liquid form. However, it's important to note that other factors, such as the planet's atmosphere and magnetic field, could also play a role in determining its habitability.", "https://rwspace.ru/wp-content/uploads/2020/05/Zemlya-i-proksima-e1590730028822.jpg", MAIN_COLOR)
proxb_middle2 = SimpleTextPanel("PbPNL02", "In addition to its potential for harboring life, Proxima b has also been the subject of interest for future interstellar travel. Because it's relatively close to our Solar System, some scientists have proposed the idea of sending a robotic mission to investigate the planet and potentially even establish a human colony there in the distant future.", MAIN_COLOR)
proxb_middle3 = SimpleImagePanel("PbPNL03", "https://cdnb.artstation.com/p/assets/images/images/003/366/651/medium/greg-wisniewski-proximab.jpg?1472923093", MAIN_COLOR)
proxb_middle4 = SimpleTextPanel("PbPNL04", "Proxima b is located approximately 4.2 light-years away from Earth in the constellation of Centaurus. It was discovered using the radial velocity method, which involves measuring the wobble of a star caused by the gravitational pull of an orbiting planet.", MAIN_COLOR)

proxd_starter = HeaderTextPanel("PdPNL00", "Proxima D", "Proxima D is also known as Proxima Centauri b, which is an exoplanet that orbits in the habitable zone of the closest star to the Sun, Proxima Centauri. It was discovered in 2016 and is located about 4.24 light-years away from Earth in the Alpha Centauri star system. Proxima D has a similar mass to Earth and may have a surface temperature that is suitable for liquid water to exist, making it a potential target for future studies aimed at discovering signs of life beyond our Solar System. However, more research is needed to fully understand the characteristics of this planet.", ["#ffd0d0","#ff6363", "#ffd0d0"], [], False, True)
proxd_middle1 = CombinedHeaderPanel("PdPNL01", "Earth-like Rock", "Proxima D is a rocky, Earth-sized planet that orbits its star at a distance that puts it within the habitable zone. This means that it receives just the right amount of heat from its star to maintain liquid water on its surface, which is one of the key ingredients for life as we know it.", "https://22century.ru/wp-content/uploads/2016/12/proxima_surface.jpg", MAIN_COLOR, ["orange", "salmon"])
proxd_middle2 = SimpleTextPanel("PdPNL02", "One of the challenges of studying Proxima D is that it is so far away. At a distance of 4.24 light-years, it would take current spacecraft technology thousands of years to make the journey. This means that astronomers have had to rely on indirect methods to study the planet, such as observing its effects on the light of its host star.", MAIN_COLOR)
proxd_middle3 = SimpleImagePanel("PdPNL03", "https://i.ytimg.com/vi/dw82W1b7bd0/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGHIgUChGMA8=&rs=AOn4CLDAqjymZoU2M2W04Dcedscc6_K57g", MAIN_COLOR)
proxd_middle4 = SimpleTextPanel("PdPNL04", "In addition to its potential habitability, Proxima D has also been found to be bombarded by high levels of radiation from its star. This could make it difficult for life to survive on the planet's surface, but researchers are still investigating how life might adapt to these conditions.", MAIN_COLOR)
proxd_middle5 = HeaderTextPanel("PdPNL05", "Habitable?", "Proxima D is considered to be potentially habitable because it orbits within the habitable zone of its star - the region around a star where conditions are just right for liquid water to exist on the surface of a planet. Liquid water is a key ingredient for life as we know it, and so the fact that Proxima D may have liquid water makes it an exciting target for astrobiological research.", MAIN_COLOR, ["green", "salmon"])

# OBJECTS
proxc = ObjectClass("PROXC", "Proxima C",  
                    ['6vh', '-3vh', '#0051ff', '#1e00ff', '10px','#8a2be2'],
                    ['30vh', '-15vh'],
                    ['30vh', '-15vh', '1928'],
                    [proxc_starter, proxc_middle1, proxc_middle2, proxc_middle3, proxc_middle4], 93, "Exoplanet - Gas planet")
proxb = ObjectClass("PROXB", "Proxima B", 
                    ['4vh', '-2vh', '#ffadad', '#ffd9a7', '10px'],
                    ['18vh', '-9vh'],
                    ['18vh', '-9vh', '11'], 
                    [proxb_starter, proxb_middle1, proxb_middle2, proxb_middle3, proxd_middle4], 94, "Exoplanet - Rocky")
proxd = ObjectClass("PROXD", "Proxima D", 
                    ['2vh', '-1vh', '#ffd0d0', '#ff6363', '5px'],
                    ['10vh', '-5vh'],
                    ['10vh', '-5vh', '5'], 
                    [proxd_starter, proxd_middle1, proxd_middle2, proxd_middle3, proxd_middle4, proxd_middle5], 95, "Exoplanet - Rocky")

alpha = ObjectClass("ALPHA", "Alpha", 
                    ['10vh', '-5vh', '#ffd000', '#f70', '30px', '#fff'],
                    ['2vh', '-1vh'],
                    ['2vh', '-1vh', '10'],  
                    [alpha_starter, alpha_middle1, alpha_middle2, alpha_middle3, alpha_middle4], 99, "Star - Yellow dwarf")
beta =  ObjectClass("BETA", "Beta", 
                    ['7vh', '-3.5vh', '#ff9100', '#f70', "20px", "#ff0"],
                    ['20vh', '-10vh'],
                    ['20vh', '-10vh', '45'], 
                    [beta_starter, beta_middle1, beta_middle2, beta_middle3], 98, "Star - Yellow dwarf")
prox =  ObjectClass("PROX", "Proxima",
                    ['4vh', '-2vh', 'red', '#61', "35px", "red"],
                    ['64vh', '-32vh'],
                    ['64vh', '-32vh', '325'], 
                    [prox_starter, prox_middle1, prox_middle2, prox_middle3, prox_middle4], 97, "Star - Red dwarf", [proxd, proxb, proxc])


# SYSTEM
SystemObject = SystemClass(1, "Alpha Centauri", 
                            [panel_starter, panel_middle1, panel_middle2, panel_middle3, panel_middle4, panel_middle5, panel_middle6], 
                            [alpha, beta, prox], 
                            "icons/alternativeicon.ico", MAIN_COLOR) 