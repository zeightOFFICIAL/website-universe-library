import static.Types.PanelType as PanelType
import static.Types.StyleType as StyleType


class SystemClass:
    def __init__(self, id, name, panels, objects, icon, coloring):
        self.id = id
        self.name = name
        self.panels = panels
        self.objects = objects
        self.icon = icon
        self.accent_bar = StyleType.Style.Misc.accent_bar(coloring[0], coloring[1])

    def get_all_objects(self):
        object_list = []
        for object in self.objects:
            object_list.append(object)
            object_list += object.get_sub_objects()
        return object_list

    def get_head(self):
        title = f"Hello, {self.name}!"
        meta = f'charset="utf-8"'
        link_icon = f'rel="icon" href="static/{self.icon}"'
        link_style = f'rel="stylesheet" href="static/SystemStyles.css"'
        head = f"<meta {meta}/><title> {title} </title><link {link_icon}><link {link_style}>"
        return head

    def get_main_panels(self):
        panels_str = ""
        for panel in self.panels:
            panels_str += f'{panel.__str__()}'
        panels_str = f'<div id=\"SYSTEM_INFO\" class=\"LeftPanel\">{panels_str}</div>'
        return panels_str

    def get_objects(self):
        objects_str = ""
        for object in self.objects:
            objects_str += f'{object.__str__()}'
        objects_str = f'<div class="star-system" onclick="closeSidepanel();closeSystempanel();"><div id="zeropoint" style="z-index:100;"></div>{objects_str}</div>'
        return objects_str

    def get_accent_bar(self):
        return f'<div {self.accent_bar}></div>'

    def get_panels(self):
        panels_str = ""
        for object in self.objects:
            panels_str += object.get_panels()
        return panels_str

    def get_side_panel_obj(self):
        side_str = ""
        for object in self.get_all_objects():
            side_str += f'<a {PanelType.Style.Text.sidepanel()} onclick="objClicked(\'{object.id+"_INFO"}\');closeSidepanel();">{object.name}</a>'
        # side_str = f'<div class="SidePanel" id="sidepanel"><'
        return side_str
