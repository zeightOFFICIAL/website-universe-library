import static.Types.PanelType as PanelType

class SystemClass:
    def __init__(self, id, name, main_panels, objects, page_icon, coloring):
        self.id = id
        self.name = name
        self.panels = main_panels
        self.objects = objects
        self.page_icon = page_icon
        self.accent_bar = PanelType.Style.Misc.ReturnAccentBar(coloring[0], coloring[1])
    def GetHead(self):
        title = f"Hello, {self.name}!"
        meta =  f'charset="utf-8"'
        link_icon =  f'rel="icon" href="/static/{self.page_icon}"'
        link_style = f'rel="stylesheet" href="/static/systemstyles.css"'
        return f"<meta {meta}/><title>{title}</title><link {link_icon}><link {link_style}>"
    def GetMainPanels(self):
        panelstr = ""
        for panel in self.panels:
            panelstr += f'{panel.__str__()}'
        return panelstr
    def GetObjects(self):
        objectsstr = ""
        for object in self.objects:
            objectsstr += f'{object.__str__()}'
        return objectsstr
    def GetAccentBar(self):
        return f'<div {self.accent_bar}></div>'
    def GetPanels(self):
        allInfo = ""
        for panelsInfo in self.objects:
            allInfo += panelsInfo.__str__()
        return allInfo