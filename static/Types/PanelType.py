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
        IMAGE_SLIDER
}
'''


class BasePanel:
    def __init__(self, id):
        self.id = id


class SimpleTextPanel(BasePanel):
    def __init__(self, id, text, box_color, slider=False):
        super().__init__(id)
        self.style_box = Style.Box.text_info(
            box_color[0], box_color[1], box_color[2], slider)
        self.style_text = Style.Text.normal()
        self.text = text

    def __str__(self):
        return f'<div {self.style_box} class="{self.id}"><p {self.style_text}> {self.text} </p></div>'


class TopHeaderTextPanel(SimpleTextPanel):
    def __init__(self, id, header, text, box_color, title_color, slider=False):
        super().__init__(id, text, box_color, slider)
        self.style_header = Style.Text.header_one(
            title_color[0], title_color[1])
        self.header = header

    def __str__(self):
        return f'<div {self.style_box} class="{self.id}"><h2 {self.style_header}> {self.header} </h2><p {self.style_text}> {self.text} </p></div>'


class HeaderTextPanel(SimpleTextPanel):
    def __init__(self, id, header, text, box_color, title_color, slider=False):
        super().__init__(id, text, box_color, slider)
        self.style_header = Style.Text.header_two(
            title_color[0], title_color[1])
        self.header = header

    def __str__(self):
        return f'<div {self.style_box} class="{self.id}"><h3 {self.style_header}> {self.header} </h3><p {self.style_text}> {self.text} </p></div>'


class CombinedHeaderPanel(HeaderTextPanel):
    def __init__(self, id, header, text, image, box_color, title_color, order=1, slider=False):
        super().__init__(id, header, text, box_color, title_color, slider)
        self.style_image = Style.Image.original()
        self.image = image
        self.order = order

    def __str__(self):
        if self.order == 1:
            return f'<div {self.style_box} class="{self.id}"><h3 {self.style_header}> {self.header} </h2><p {self.style_text}> {self.text} </p><img src="{self.image}" {self.style_image}></div>'
        elif self.order == 2:
            return f'<div {self.style_box} class="{self.id}"><h3 {self.style_header}> {self.header} </h2><img src="{self.image}" {self.style_image}><p {self.style_text}> {self.text} </p></div>'
        else:
            return f'<div {self.style_box} class="{self.id}"><img src="{self.image}" {self.style_image}><h3 {self.style_header}> {self.header} </h2><p {self.style_text}> {self.text} </p></div>'


class SimpleImagePanel(BasePanel):
    def __init__(self, id, image, box_color, slider=False):
        super().__init__(id)
        self.style_box = Style.Box.image_info(
            box_color[0], box_color[1], box_color[2], slider)
        self.style_image = Style.Image.default()
        self.image = image

    def __str__(self):
        return f'<div {self.style_box} class="{self.id}"><img src="{self.image}" {self.style_image}></div>'


class CombinedSimplePanel(SimpleTextPanel):
    def __init__(self, id, text, image, box_color, order=1, slider=False):
        super().__init__(id, text, box_color, slider)
        self.style_image = Style.Image.original()
        self.image = image
        self.order = order

    def __str__(self):
        if self.order == 1:
            return f'<div {self.style_box} class="{self.id}"><p {self.style_text}> {self.text} </p><img src="{self.image}" {self.style_image}></div>'
        else:
            return f'<div {self.style_box} class="{self.id}"><img src="{self.image}" {self.style_image}><p {self.style_text}> {self.text} </p></div>'


class SimpleVideoPanel(BasePanel):
    def __init__(self, id, url, box_color):
        super().__init__(id)
        self.style_box = Style.Box.image_info(
            box_color[0], box_color[1], box_color[2])
        self.style_video = Style.Video.normal()
        self.url = url

    def __str__(self):
        return f'<div {self.style_box} class="{self.id}"><iframe {self.style_video} src="{self.url}"></iframe></div>'


class PanelSlider(BasePanel):
    def __init__(self, id, all_panels, box_color):
        super().__init__(id)
        self.hidden = Style.Misc.overflow_hidden()
        self.box_style = Style.Box.slider_info(
            box_color[0], box_color[1], box_color[2])
        self.button_left = Style.Button.slider_left(box_color[0])
        self.button_right = Style.Button.slider_right(box_color[1])
        self.all_panels = all_panels

    def __str__(self):
        prefix = f'<div {self.box_style} class="SLIDER">'
        panels_str = ""
        for panel in self.all_panels:
            panels_str += panel.__str__()
        embed_ID = f"'{self.id}'"
        postfix = f'<button {self.button_left } {EventHandlers.SlidesButton(-1., embed_ID)}>&#10094;</button><button {self.button_right} {EventHandlers.SlidesButton(1.,  embed_ID)}>&#10095;</button></div>'
        return f'{prefix}{panels_str}{postfix}'


class ImagePanelSlider(PanelSlider):
    def __init__(self, id, all_panels, box_color):
        super().__init__(id, all_panels, box_color)
        self.box_style = Style.Box.image_info(
            box_color[0], box_color[1], box_color[2])

    def __str__(self):
        prefix = f'<div {self.box_style} class="Slider">'
        panels_str = ""
        for panel in self.all_panels:
            panels_str += panel.__str__()
        embed_ID = f"'{self.id}'"
        postfix = f'<button {self.button_left } {EventHandlers.SlidesButton(-1., embed_ID)}>&#10094;</button><button {self.button_right} {EventHandlers.SlidesButton(1.,  embed_ID)}>&#10095;</button></div>'
        return f'{prefix}{panels_str}{postfix}'
