from static.Types.StyleType import Style, EventHandlers

'''
{
    BASE
        SIMPLE_TEXT
            TOP_HEADER_TEXT
            HEADER_TEXT
                COMBINED_HEADER
            COMBINED_SIMPLE
        SIMPLE_IMAGE
        SIMPLE_VIDEO
        SLIDER
}
'''

class BasePanel:
    def __init__(self, id):
        self.id = id


class SimpleTextPanel(BasePanel):
    def __init__(self, id, text, box_color, slider=False):
        super().__init__(id)
        self.style_box = Style.Box.ReturnText(box_color[0], box_color[1], box_color[2], slider)
        self.style_text = Style.Text.ReturnNormal()
        self.text = text

    def __str__(self):
        return f'<div {self.style_box} class="{self.id}"><p {self.style_text}> {self.text} </p></div>'


class TopHeaderTextPanel(SimpleTextPanel):
    def __init__(self, id, header, text, box_color, header_color, slider=False):
        super().__init__(id, text, box_color, slider)
        self.style_header = Style.Text.ReturnHeader(header_color[0], header_color[1])
        self.header = header        

    def __str__(self):
        return f'<div {self.style_box} class="{self.id}"><h2 {self.style_header}> {self.header} </h2><p {self.style_text}> {self.text} </p></div>'


class HeaderTextPanel(SimpleTextPanel):
    def __init__(self, id, header, text, box_color, header_scheme, slider=False):
        super().__init__(id, text, box_color, slider)
        self.style_header = Style.Text.ReturnTitle(header_scheme[0], header_scheme[1])
        self.header = header

    def __str__(self):
        return f'<div {self.style_box} class="{self.id}"><h3 {self.style_header}> {self.header} </h3><p {self.style_text}> {self.text} </p></div>'


class CombinedHeaderPanel(HeaderTextPanel):
    def __init__(self, id, header, text, image, box_color, header_scheme, slider=False):
        super().__init__(id, header, text, box_color, header_scheme, slider)
        self.style_image = Style.Image.ReturnImageOriginal()
        self.image = image

    def __str__(self):
        return f'<div {self.style_box} class="{self.id}"><h3 {self.style_header}> {self.header} </h2><p {self.style_text}> {self.text} </p><img src="{self.image}" {self.style_image}></div>'


class SimpleImagePanel(BasePanel):
    def __init__(self, id, image, box_color, slider=False):
        super().__init__(id)
        self.style_box = Style.Box.ReturnImage(box_color[0], box_color[1], box_color[2], slider)
        self.style_image = Style.Image.ReturnImage()
        self.image = image

    def __str__(self):
        return f'<div {self.style_box} class="{self.id}"><img src="{self.image}" {self.style_image}></div>'


class CombinedSimplePanel(SimpleTextPanel):
    def __init__(self, id, text, image, box_color, slider=False):
        super().__init__(id, text, box_color, slider)
        self.style_image = Style.Image.ReturnImageOriginal()
        self.image = image

    def __str__(self):
        return f'<div {self.style_box} class="{self.id}"><p {self.style_text}> {self.text} </p><img src="{self.image}" {self.style_image}></div>'


class SimpleVideoPanel(BasePanel):
    def __init__(self, id, url, box_color):
        super().__init__(id)
        self.style_box = Style.Box.ReturnImage(box_color[0], box_color[1], box_color[2])
        self.style_video = Style.Video.ReturnVideo()
        self.url = url

    def __str__(self):
        return f'<div {self.style_box} class="{self.id}"><iframe {self.style_video} src="{self.url}"></iframe></div>'


class PanelSlider(BasePanel):
    def __init__(self, id, all_panels, box_scheme):
        super().__init__(id)
        self.hidden = Style.Misc.ReturnHidden()
        self.box_style = Style.Box.ReturnSliderText(
            box_scheme[0], box_scheme[1], box_scheme[2])
        self.button_left = Style.Button.ReturnSliderLeft(box_scheme[0])
        self.button_right = Style.Button.ReturnSliderRight(box_scheme[1])
        self.all_panels = all_panels

    def __str__(self):
        begin = f'<div {self.box_style}>'
        panelsstr = ""
        for panel in self.all_panels:
            panelsstr += panel.__str__()
        embedid = f"'{self.id}'"
        end_one = f'<button {self.button_left } {EventHandlers.SlidesButton(-1., embedid)}>&#10094;</button>'
        end_two = f'<button {self.button_right} {EventHandlers.SlidesButton(1.,  embedid)}>&#10095;</button>'
        ending = f'</div>'
        return f'{begin}{panelsstr}{end_one}{end_two}{ending}'


class ImagePanelSlider(PanelSlider):
    def __init__(self, id, all_panels, fore_color, back_color):
        super().__init__(id, all_panels, fore_color, back_color)
