import static.Types.StyleType as Style

class Mimic:
    @staticmethod
    def get_falseborne_stars():
        solar_def = f'<a {Style.Style.Misc.sidepanel_univ_href("background-color:white;")}  class="TITLED_HREF_TEXT" href="solarsystem">Solar<br>System<img {Style.Style.Image.short("20vmin")}  class="TITLED_HREF_IMG" src="../static/jpg/shorts/solarshort.png" alt="sun"></a>'
        return f'{solar_def}'