from static.Types.StyleType import Visual, EventHandlers

class ObjectClass:
    def __init__(self, id, name, z_index, object_args, orbit_args, spin_args, panels, subobjects = []):
        self.id = id
        self.name = name
        self.subobjects = subobjects
        self.panels = panels
        self.z_index = -998
        if len(self.subobjects) > 1:
            self.z_index = z_index - 1
        self.obj_description = Visual.Object(object_args, self.z_index)
        self.obj_click = EventHandlers.object_click(self.id+"_INFO")
        self.orb_description = Visual.Orbit(orbit_args)
        self.spn_description = Visual.Spin(spin_args, z_index)
    def __str__(self):
        objectstr = ""
        for object in self.subobjects:
            objectstr += object.__str__()
        div_orbit = f'<div {self.orb_description}></div>'
        div_spin  = f'<div {self.spn_description}>'
        div_obj   = f'<div {self.obj_description} {self.obj_click}></div>{objectstr}</div>'
        return f'{div_orbit}{div_spin}{div_obj}'
    def get_panels(self):
        combined = f'<div id="{self.id}_INFO" class="LeftPanel" onclick="closeSidepanel();">'
        for panel in self.panels:
            combined += panel.__str__()
        combined += "</div>"
        for subobj in self.subobjects:
            combined += subobj.get_panels()
        return combined
    def get_sub_objects(self):
        all = []
        for subobject in self.subobjects:
            all.append(subobject)
            all += subobject.get_sub_objects()
        return all
                