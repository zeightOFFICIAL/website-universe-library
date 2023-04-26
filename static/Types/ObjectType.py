from static.Types.StyleType import Style
from static.Types.StyleType import Visual
from static.Types.StyleType import EventHandlers


class ObjectClass:
    def __init__(self, id, name, object_args, orbit_args, spin_args, panels, z_index, obj_type, subobjects=[]):
        self.id = id
        self.name = name
        self.subobjects = subobjects
        self.type = obj_type
        self.panels = panels
        self.z_index = -998
        if len(self.subobjects) > 1:
            self.z_index = z_index - 1
        self.color = object_args[2]
        self.second_color = object_args[3]
        self.object_description = Visual.Object(object_args, self.z_index)
        self.object_click = EventHandlers.object_click(self.id+"_INFO")
        self.orbit_description = Visual.Orbit(orbit_args)
        self.spin_description = Visual.Spin(spin_args, z_index)
        self.hovering = EventHandlers.hover_object(
            id+"_OBJ", "HoveredObject", id+"_TOOLTIP")

    def __str__(self):
        objects_str = ""
        for object in self.subobjects:
            objects_str += object.__str__()
        div_orbit = f'<div {self.orbit_description}></div>'
        div_spin = f'<div {self.spin_description}>'
        div_obj = f'<div id="{self.id}_OBJ" class="Object" {self.object_description} {self.object_click} {self.hovering}></div>{objects_str}</div>'
        return f'{div_orbit}{div_spin}{div_obj}'

    def get_panels(self):
        combined = f'<div id="{self.id}_INFO" class="LeftPanel" onclick="closeSidepanel();onHoverLeaveForced();">'
        for panel in self.panels:
            combined += panel.__str__()
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
        div = f'<div id="{self.id}_TOOLTIP" {Style.Box.tooltip_info(self.color, self.second_color, self.color)}><h {Style.Text.tooltip_h(self.color, self.second_color)}>{self.name}</h><p {Style.Text.tooltip_h2()}>{self.type}</p></div>'
        return div
