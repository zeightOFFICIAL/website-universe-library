import static.Types.PanelType as PanelType


class SystemClass:
    def __init__(self, id, name, panels, objects, icon, coloring):
        self.id = id
        self.name = name
        self.panels = panels
        self.objects = objects
        self.icon = icon
        self.accent = PanelType.Style.Misc.accent_bar(coloring[0], coloring[1])

    def get_all_objects(self):
        object_list = []
        for object in self.objects:
            object_list.append(object)
            object_list += object.GetSubObj()
        return object_list

    def get_head(self):
        title = f"Hello, {self.name}!"
        meta = f'charset="utf-8"'
        link_icon = f'rel="icon" href="/static/{self.icon}"'
        link_style = f'rel="stylesheet" href="/static/SystemStyles.css"'
        return f"<meta {meta}/><title>{title}</title><link {link_icon}><link {link_style}>"

    def main_panels(self):
        prefix = "<div id=\"SYSTEM_INFO\" class=\"left-panel\">"
        postfix = "</div>"
        all = ""
        for each_panel in self.panels:
            all += f'{each_panel.__str__()}'
        return prefix+all+postfix

    def GetObjects(self):
        objectsstr = ""
        for object in self.objects:
            objectsstr += f'{object.__str__()}'
        return objectsstr

    def GetAccentBar(self):
        return f'<div {self.accent}></div>'

    def GetPanels(self):
        allInfo = ""
        for panel in self.objects:
            allInfo += panel.GetPanels()
        return allInfo

    def GetObjectsSidePanel(self):
        allInfo = ""
        allObjects = self.get_all_objects()
        for object in allObjects:
            info = f'<a {PanelType.Style.Text.sidepanel()} onclick="objClicked(\'{object.id+"_INFO"}\');closeSidepanel();">{object.name}</a>'
            allInfo += info
        return allInfo
