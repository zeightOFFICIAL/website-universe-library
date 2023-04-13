from static.classes.StyleClass import Style


class Panel:
    def __init__(self, id):
        self.id = id


class SimpleTextPanel(Panel):
    def __init__(self, id, text, first_color, second_color, third_color):
        super().__init__(id)
        self.text = text
    def __str__(self):
        return f'<div style="border-width: 3px; border-style: solid; margin: 40px 15px; {self.border_image} {self.box_shadow}"><p style="{self.pclass}">{self.text}</p></div>'

class SimpleImagePanel(Panel):
    def __init__(self, id, image, first_color, second_color, third_color):
        super().__init__(id)
        self.image = image

    def __str__(self):
        return f'<div style="border-width: 3px; border-style: solid; margin: 40px 15px; {self.border_image} {self.box_shadow} {self.filling}"><img src="{self.image}" {Style.ReturnImageScalePanel()}></div>'
