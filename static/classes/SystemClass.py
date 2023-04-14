class SystemClass:
    def __init__(self, id, name, panels, objects, page_icon):
        self.id = id
        self.name = name
        self.panels = panels
        self.objects = objects
        self.page_icon = page_icon
    def GetHead(self):
        meta =  f'charset="utf-8"'
        title = f"Hello, {self.name}!"
        return f'<meta {meta}/><title>{title}</title>'