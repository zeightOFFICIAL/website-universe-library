import static.Types.PanelType as PanelType

class SystemClass:
    def __init__(self, id, name, main_panels, objects, page_icon):
        self.id = id
        self.name = name
        self.panels = main_panels
        self.objects = objects
        self.page_icon = page_icon
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