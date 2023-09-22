from static.Types.StyleType import Style
from static.Types.StyleType import Visual
from static.Types.StyleType import EventHandlers
from static.Types.PanelType import BasePanel


class ObjectClass:
    def __init__(
        self,
        id: str,
        name: str,
        obj_type: str,
        object_args: list[str],
        orbit_args: list[str],
        spin_arg: str,
        panels: list[BasePanel],
        subobjects=[],
    ):
        self.id = id
        self.name = name
        self.type = obj_type

        self.object_args = object_args
        self.orbit_args = orbit_args
        self.spin_args = orbit_args + [spin_arg]

        self.panels = panels
        self.subobjects = subobjects

        self.main_color = object_args[2]
        self.second_color = object_args[3]
        self.object_description = Visual.Object(object_args)
        self.object_click = EventHandlers.object_click(self.id + "_INFO")
        self.orbit_description = Visual.Orbit(orbit_args)
        self.spin_description = Visual.Spin(self.spin_args)
        self.hovering = EventHandlers.hover_object(
            id + "_OBJ", "HoveredObject", id + "_TOOLTIP"
        )

    def __repr__(self):
        objects_str = ""
        for object in self.subobjects:
            objects_str += object.__repr__()
        div_orbit = f"<div {self.orbit_description}></div>"
        div_spin = f"<div {self.spin_description}>"
        div_obj = f'<div id="{self.id}_OBJ" class="Object" {self.object_description} {self.object_click} {self.hovering}></div>{objects_str}</div>'
        return f"{div_orbit}{div_spin}{div_obj}"

    def get_panels(self):
        combined = f'<div id="{self.id}_INFO" class="LeftPanel" onclick="closeSidepanel();closeSystempanel();">'
        for panel in self.panels:
            combined += panel.__repr__()
        combined += "</div>"
        for subobject in self.subobjects:
            combined += subobject.get_panels()
        return combined

    def get_subobjects(self):
        all = []
        for subobject in self.subobjects:
            all.append(subobject)
            all += subobject.get_subobjects()
        return all

    def get_tooltip(self):
        div = f'<div id="{self.id}_TOOLTIP" {Style.Box.tooltip_info(self.main_color, self.second_color, self.main_color)}><h {Style.Text.tooltip_h(self.main_color, self.second_color)}>{self.name}</h><p {Style.Text.tooltip_h2()}>{self.type}</p></div>'
        return div

    def add_subobj(self, object):
        self.subobjects.append(object)
