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
        SIMPLE_AUDIO
}
'''


class BasePanel:
    def __init__(self, id):
        self.id = id
        self.embed_id = f'id="{self.id}"'


class SimpleTextPanel(BasePanel):
    def __init__(self, id, text, colors, slider=False):
        super().__init__(id)
        self.div_style = Style.Box.text_info(
            colors[0], colors[1], colors[2], slider)
        self.p_style = Style.Text.normal()
        self.text = text

    def __str__(self):
        return f'<div {self.div_style} {self.embed_id}><p {self.p_style}> {self.text} </p></div>'


class TopHeaderTextPanel(SimpleTextPanel):
    def __init__(self, id, title, text, colors, h_colors, slider=False):
        super().__init__(id, text, colors, slider)
        self.h_style = Style.Text.header_one(
            h_colors[0], h_colors[1])
        self.title = title

    def __str__(self):
        return f'<div {self.div_style} {self.embed_id}><h2 {self.h_style}> {self.title} </h2><p {self.p_style}> {self.text} </p></div>'


class HeaderTextPanel(SimpleTextPanel):
    def __init__(self, id, title, text, colors, h_colors, slider=False, close_button=False, extra_buttons=[]):
        super().__init__(id, text, colors, slider)
        self.h_style = Style.Text.header_two(
            h_colors[0], h_colors[1])
        self.title = title
        self.close_button = ""
        self.extra_buttons = ""
        top_start = 5.5
        top_increment = 14
        if close_button:
            self.close_button = f'<button class="BorderButton" ID="CLOSE_INFO" {Style.Button.on_border(colors[0], colors[1])} {EventHandlers.object_click("SYSTEM_INFO")} {EventHandlers.hover("CLOSE_INFO", "HoveredBorderButton")}>&#10006;</button>'
        for href in extra_buttons:
            top_start += top_increment
            href_str = f'href="{href}"'
            button_id = f'id="EXTRA_INFO{(int)(top_start*10)}"'
            self.extra_buttons = f'<a class="BorderButton" {button_id} {Style.Button.on_border(colors[0], colors[1], 30, str(top_start)+"%")} {href_str} target="_blank" {EventHandlers.hover(button_id, "HoveredBorderButton")}>&#9783;</a>'

    def __str__(self):
        return f'{self.close_button}{self.extra_buttons}<div {self.div_style} {self.embed_id}><h3 {self.h_style}> {self.title} </h3><p {self.p_style}> {self.text} </p></div>'


class CombinedHeaderPanel(HeaderTextPanel):
    def __init__(self, id, title, text, image_url, colors, h_colors, layout=1, slider=False):
        super().__init__(id, title, text, colors, h_colors, slider)
        self.img_style = Style.Image.original()
        self.image = f'src="{image_url}"'
        self.layout = layout

    def __str__(self):
        if self.layout == 1:
            return f'<div {self.div_style} {self.embed_id}><h3 {self.h_style}> {self.title} </h2><p {self.p_style}> {self.text} </p><img {self.image} {self.img_style}></div>'
        elif self.layout == 2:
            return f'<div {self.div_style} {self.embed_id}><h3 {self.h_style}> {self.title} </h2><img {self.image} {self.img_style}><p {self.p_style}> {self.text} </p></div>'
        else:
            return f'<div {self.div_style} {self.embed_id}><img {self.image} {self.img_style}><h3 {self.h_style}> {self.title} </h2><p {self.p_style}> {self.text} </p></div>'


class SimpleImagePanel(BasePanel):
    def __init__(self, id, image_url, colors, slider=False):
        super().__init__(id)
        self.div_style = Style.Box.image_info(
            colors[0], colors[1], colors[2], slider)
        self.img_style = Style.Image.default()
        self.image = f'src="{image_url}"'

    def __str__(self):
        return f'<div {self.div_style} {self.embed_id}><img {self.image} {self.img_style}></div>'


class CombinedSimplePanel(SimpleTextPanel):
    def __init__(self, id, text, image_url, colors, layout=1, slider=False):
        super().__init__(id, text, colors, slider)
        self.img_style = Style.Image.original()
        self.image = self.image = f'src="{image_url}"'
        self.layout = layout

    def __str__(self):
        if self.layout == 1:
            return f'<div {self.div_style} {self.embed_id}><p {self.p_style}> {self.text} </p><img {self.image} {self.img_style}></div>'
        else:
            return f'<div {self.div_style} {self.embed_id}><img {self.image} {self.img_style}><p {self.p_style}> {self.text} </p></div>'


class SimpleVideoPanel(BasePanel):
    def __init__(self, id, url, colors):
        super().__init__(id)
        self.div_style = Style.Box.image_info(
            colors[0], colors[1], colors[2])
        self.iframe_style = Style.Video.normal()
        self.video = f'src="{url}"'

    def __str__(self):
        return f'<div {self.div_style} {self.embed_id}><iframe {self.video} {self.iframe_style}></iframe></div>'


class PanelSlider(BasePanel):
    def __init__(self, id, panels, colors):
        super().__init__(id)
        self.hidden = Style.Misc.overflow_hidden()
        self.div_style = Style.Box.slider_info(
            colors[0], colors[1], colors[2])
        self.button_left = Style.Button.slider_left(colors[0])
        self.button_right = Style.Button.slider_right(colors[1])
        self.panels = panels

    def __str__(self):
        panels_str = ""
        for panel in self.panels:
            panels_str += panel.__str__()
        buttons_postfix = f'<button {self.button_left} {EventHandlers.slider_click(-1, self.id)}>&#10094;</button><button {self.button_right} {EventHandlers.slider_click(1, self.id)}>&#10095;</button></div>'
        return f'<div {self.div_style}>{panels_str}{buttons_postfix}'


class ImagePanelSlider(PanelSlider):
    def __init__(self, id, panels, colors):
        super().__init__(id, panels, colors)
        self.div_style = Style.Box.image_info(
            colors[0], colors[1], colors[2])

    def __str__(self):
        panels_str = ""
        for panel in self.panels:
            panels_str += panel.__str__()
        embed_ID = f"'{self.id}'"
        buttons_postfix = f'<button {self.button_left } {EventHandlers.slider_click(-1, embed_ID)}>&#10094;</button><button {self.button_right} {EventHandlers.slider_click(-1, embed_ID)}>&#10095;</button></div>'
        return f'<div {self.div_style}>{panels_str}{buttons_postfix}'


class SimpleMusicSlider(BasePanel):
    def __init__(self, id, src, colors):
        super().__init__(id)
        self.style_box = Style.Box.text_info(
            colors[0], colors[1], colors[2]
        )
        self.music = f'src="{src}"'

    def __str__(self):
        return f'<div {self.style_box} {self.embed_id} class="Audio"><audio controls><source {self.music}>Your browser does not support the audio element.</audio>'
