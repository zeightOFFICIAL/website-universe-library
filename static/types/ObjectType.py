from static.types.StyleType import Visual
import static.types.PanelType

class ObjectClass:
    def __init__(self, id, name, z_index, object_args, orbit_args, spin_args, panels):
        self.id = id
        self.name = name
        self.subobjects = []
        self.panels = panels
        self.z_index = z_index
        self.obj_description = Visual.Object(object_args[0], object_args[1], object_args[2], object_args[3], object_args[4])
        self.orb_description = Visual.Orbit(orbit_args[0], orbit_args[1], orbit_args[2], orbit_args[3])
        self.spn_description = Visual.Spin(spin_args[0], spin_args[1], spin_args[2], spin_args[3], spin_args[4], spin_args[5])
    def __str__(self):
        return 0