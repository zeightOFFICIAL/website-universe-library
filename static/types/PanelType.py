from static.Types.StyleType import Style, EventHandlers


class BasePanel:
    def __init__(self, id):
        self.id = id

class SimpleTextPanel(BasePanel):
    def __init__(self, id, text, first_color, second_color, third_color):
        super().__init__(id)
        self.text = text
        self.box_style = Style.Box.ReturnText(first_color, second_color, third_color)
        self.text_style = Style.Text.ReturnNormal()
    def __str__(self):
        return f'<div {self.box_style}><p {self.text_style}> {self.text} </p></div>'
class TextPanel(SimpleTextPanel):
    def __init__(self, id, header, text, first_color, second_color, third_color):
        super().__init__(id, text, first_color, second_color, third_color)
        self.header = header
        self.header_style = Style.Text.ReturnHeader(first_color, second_color)
    def __str__(self):
        return f'<div {self.box_style}><h2 {self.header_style}> {self.header} </h2><p {self.text_style}> {self.text} </p></div>'
    
class SimpleImagePanel(BasePanel):
    def __init__(self, id, image, first_color, second_color, third_color):
        super().__init__(id)
        self.image = image
        self.box_style = Style.Box.ReturnImage(first_color, second_color, third_color)
        self.image_style = Style.Image.ReturnImage()
    def __str__(self):
        return f'<div {self.box_style}><img src="{self.image}" {self.image_style}></div>'
    
class SimpleVideoPanel(BasePanel):
    def __init__(self, id, url, first_color, second_color, third_color):
        super().__init__(id)
        self.url = url
        self.box_style = Style.Box.ReturnImage(first_color, second_color, third_color)
        self.video_style = Style.Video.ReturnVideo()
    def __str__(self):
        return f'<div {self.box_style}><iframe {self.video_style} src="{self.url}"></iframe></div>'

class PanelSlider(BasePanel):
    def __init__(self, id, all_panels, fore_color, back_color):
        super().__init__(id)
        self.hidden = Style.Misc.ReturnHidden()
        self.box_style = Style.Box.ReturnText()
        self.button_left = Style.Button.ReturnSliderLeft(fore_color)
        self.button_right =Style.Button.ReturnSliderRight(back_color)
        self.all_panels = all_panels
    def __str__(self):
        begin = f'<div class="{self.id}" {self.hidden} {self.box_style}>'
        for panel in self.all_panels:
            
        end_one   = f'<button {self.button_left } {EventHandlers.SlidesButton(-1., "alphaSlide")}>&#10094;</button>'
        end_two   = f'<button {self.button_right} {EventHandlers.SlidesButton(1.,  "alphaSlide")}>&#10094;</button>'
        return f'{begin}'