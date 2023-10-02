import static.Types.PanelType as PanelType
import static.Types.StyleType as StyleType
import static.Types.ObjectType as ObjectType
import os
from django.conf import settings


class SystemClass:
    def __init__(
        self,
        id: int,
        name: str,
        panels: list[PanelType.BasePanel],
        objects: list[ObjectType.ObjectClass],
        icon: str,
        coloring: list[str],
    ):
        self.id = id
        self.name = name

        self.panels = panels
        self.objects = objects
        self.icon = icon
        self.coloring = coloring

    def get_objects_list(self) -> list:
        object_list = []
        for object in self.objects:
            object_list.append(object)
            object_list += object.get_subobjects()
        return object_list

    def get_head(self) -> str:
        title = f"Hello, {self.name}!"
        meta = f'charset="utf-8" name="viewport" content="width=device-width, initial-scale=1"'
        link_icon = f'rel="icon" href="../static/{self.icon}"'
        link_style = f'rel="stylesheet" href="../static/Styles/SystemStyles.css"'
        head = f"<meta {meta}/><link {link_icon}><link {link_style}><title> {title} </title>"
        return head

    def get_main_panels(self) -> str:
        panels_str = ""
        for panel in self.panels:
            panels_str += f"{panel.__repr__()}"
        panels_str = f'<div id="SYSTEM_INFO" class="LeftPanel" onclick="closeSidepanel();closeSystempanel();"> {panels_str} </div>'
        return panels_str

    def get_objects_str(self) -> str:
        objects_str = ""
        tooltip_str = ""
        for object in self.objects:
            objects_str += f"{object.__repr__()}"
        for object in self.get_objects_list():
            tooltip_str += f"{object.get_tooltip()}"
        objects_str = f'<div class="StarSystem" onclick="closeSidepanel();closeSystempanel();"><div id="zeropoint" style="z-index:100;"></div>{tooltip_str}{objects_str}</div>'
        return objects_str

    def get_accent_bar(self) -> str:
        self.accent_bar = StyleType.Style.Misc.accent_bar(
            self.coloring[0], self.coloring[1]
        )
        return f"<div {self.accent_bar}></div>"

    def get_object_panels(self) -> str:
        panels_str = ""
        for object in self.objects:
            panels_str += object.get_panels()
        return panels_str

    def get_star_sidepanel(self) -> str:
        side_str = ""
        for object in self.get_objects_list():
            object_id = f"{object.id}_LABEL"
            side_str += f'<a id="{object_id}" {PanelType.Style.Text.sidepanel()} onclick="objClicked(\'{object.id}_INFO\');closeSidepanel();" {StyleType.EventHandlers.hover_side_name(object_id, object.main_color)}>   {object.name}</a>'
        side_str = f'<div id="STAR_SIDEPANEL" class="SidePanel" style="box-shadow: 1vmin 0 1vmin {self.coloring[0]};"><a id="STAR_CLOSEBUTTON" {PanelType.Style.Button.close_sidepanel(self.coloring[0], "2vmin")} onclick="closeSidepanel();" {StyleType.EventHandlers.hover_2d("STAR_CLOSEBUTTON", "STAR_SIDEPANEL", "HoveredBorderButton", "HoveredSidepanel")}>&#9776; Objects</a><hr>{side_str}</div>'
        return side_str

    def get_side_buttons(self) -> str:
        star_button = f'<a id="STAR_BUTTON" {StyleType.Style.Button.open_sidepanel()}         onclick="openSidepanel();"   {StyleType.EventHandlers.hover("STAR_BUTTON","HoveredBorderButton")}>&#9776;</a>'
        univ_button = f'<a id="UNIV_BUTTON" {StyleType.Style.Button.open_sidepanel("8vmin")}  onclick="openSystempanel();" {StyleType.EventHandlers.hover("UNIV_BUTTON","HoveredBorderButton")}>&#9733;</a>"'
        back_button = f'<a id="BACK_BUTTON" {StyleType.Style.Button.open_sidepanel("92.5vh")} href="/Universe/"                 {StyleType.EventHandlers.hover("BACK_BUTTON","HoveredBorderButton")}>&#8634;</a>'
        return star_button + univ_button + back_button

    def get_univ_sidepanel(self, all_systems: list[list[str, str, str]]) -> str:
        side_str = ""
        top_left = 20
        all_systems.insert(0, ["Alpha Centauri", "alpha.png", "#FF0000"])
        all_systems.insert(0, ["Solar", "solar.png", "#FBAB7E"])
        for system in all_systems:
            if system[0].split(" ").__len__() < 2:
                only_name = system[0] + " System"
            else:
                only_name = system[0]
            if not os.path.exists(f"{settings.BASE_DIR}\static\LinkImages\{system[1]}"):
                system[1] = "default.png"
            side_str += f'<a class="StarButton" id="{system[0].replace(" ", "").upper()}_STARBUTTON" href="{system[0].replace(" ", "")}" {StyleType.Style.Text.star_font(str(top_left)+"vmin", system[2])} {StyleType.EventHandlers.hover_2d(system[0].replace(" ", "").upper()+"_STARBUTTON",system[0].replace(" ", "").upper()+"_STARIMAGE","HoveredStarText","HoveredShortImage")}>{only_name.replace(" ", "<br>")}<img class="ShortImage" id="{system[0].replace(" ", "").upper()}_STARIMAGE" src="../static/LinkImages/{system[1]}" alt="{system[0].replace(" ","")}"></a>'
            top_left += 13

        side_str = f'<div id="UNIVERSE_SIDEPANEL" class="SidePanel" style="box-shadow: 1vmin 0 1vmin {self.coloring[0]};"><a id="UNIV_CLOSEBUTTON" {PanelType.Style.Button.close_sidepanel(self.coloring[0], "10vmin")} onclick="closeSystempanel();" {StyleType.EventHandlers.hover_2d("UNIV_CLOSEBUTTON", "UNIVERSE_SIDEPANEL", "HoveredBorderButton", "HoveredSidepanel")}>&#9733; Stars</a><hr>{side_str}</div>'
        return side_str
