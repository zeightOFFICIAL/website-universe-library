from mysite.Types.StyleType import Style, Visual, EventHandlers
from mysite.Types.PanelType import BasePanel


class ObjectClass:
    def __init__(
        self,
        id: str,
        name: str,
        obj_type: str,
        obj_args: list[str],
        orb_args: list[str],
        spin_arg: str,
        panels: list[BasePanel],
        subobjects=[],
    ):
        self.id = id
        self.name = name
        self.type = obj_type

        self.obj_args = obj_args
        self.orb_args = orb_args
        self.spin_args = orb_args + [spin_arg]

        self.panels = panels
        self.subobjects = subobjects

        self.main_color = obj_args[2]
        self.second_color = obj_args[3]
        self.object_description = Visual.Object(obj_args)
        self.orbit_description = Visual.Orbit(orb_args)
        self.spin_description = Visual.Spin(self.spin_args)
        self.object_click_conf = EventHandlers.object_click(self.id + "_INFO")
        self.hovering_conf = EventHandlers.hover_object(
            id + "_OBJ", "HoveredObject", id + "_TOOLTIP"
        )

    def __repr__(self) -> str:
        objects_str = ""
        for object in self.subobjects:
            objects_str += object.__repr__()
        div_orbit = f"<div {self.orbit_description}></div>"
        div_spin = f"<div {self.spin_description}>"
        div_obj = f'<div id="{self.id}_OBJ" class="Object" {self.object_description} {self.object_click_conf} {self.hovering_conf}></div>{objects_str}</div>'
        return f"{div_orbit}{div_spin}{div_obj}"

    def get_panels(self) -> str:
        combined = f'<div id="{self.id}_INFO" class="LeftPanel" onclick="closeSidepanel();closeSystempanel();">'
        for panel in self.panels:
            combined += panel.__repr__()
        combined += "</div>"
        for subobject in self.subobjects:
            combined += subobject.get_panels()
        return combined

    def get_subobjects(self) -> list:
        all = []
        for subobject in self.subobjects:
            all.append(subobject)
            all += subobject.get_subobjects()
        return all

    def get_tooltip(self) -> str:
        div = f'<div id="{self.id}_TOOLTIP" {Style.Box.tooltip_info(self.main_color, self.second_color, self.main_color)}><h {Style.Text.tooltip_h(self.main_color, self.second_color)}>{self.name}</h><p {Style.Text.tooltip_h2()}>{self.type}</p></div>'
        return div
