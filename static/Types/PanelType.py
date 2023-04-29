from static.Types.StyleType import Style
from static.Types.StyleType import EventHandlers

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
            colors[0], colors[2], slider)
        self.p_style = Style.Text.normal()
        self.text = text
        self.hover = ""
        if not slider:
            self.hover = EventHandlers.hover(self.id, "HoveredBorder")

    def __str__(self):
        return f'<div {self.div_style} {self.embed_id} {self.hover}><p {self.p_style}> {self.text} </p></div>'


class TopHeaderTextPanel(SimpleTextPanel):
    def __init__(self, id, title, text, colors, h_colors, slider=False):
        super().__init__(id, text, colors, slider)
        self.h_style = Style.Text.header_one(
            h_colors[0], h_colors[1])
        self.title = title
        self.hover = ""
        if not slider:
            self.hover = EventHandlers.hover(self.id, "HoveredBorder")

    def __str__(self):
        return f'<div {self.div_style} {self.embed_id} {self.hover}><h2 {self.h_style}> {self.title} </h2><p {self.p_style}> {self.text} </p></div>'


class HeaderTextPanel(SimpleTextPanel):
    def __init__(self, id, title, text, colors, h_colors=[], slider=False, close_button=False, extra_buttons=[]):
        super().__init__(id, text, colors, slider)        
        self.title = title
        self.close_button = ""
        self.extra_buttons = ""
        top_start = 5.5
        top_increment = 15
        self.hover = ""
        self.h_colors = h_colors
        count = 1
        self.h_style = Style.Text.header_two(
            colors[0], colors[1])
        if (len(h_colors) != 2):
            self.h_style = Style.Text.header_two(
            colors[0], colors[1])
        if not slider:
            self.hover = EventHandlers.hover(self.id, "HoveredBorder")
        if close_button:
            button_id = f'CLOSE_{self.id}'
            self.close_button = f'<button class="BorderButton" id="{button_id}" {Style.Button.on_border(colors[0])} {EventHandlers.object_click("SYSTEM_INFO")} {EventHandlers.hover(button_id, "HoveredBorderButton")}>&#10006;</button>'
        for href in extra_buttons:
            top_start += top_increment
            href_str = f'href="{href}"'
            button_id = f'EXTRA_INFO{self.id}{count}'
            self.extra_buttons += f'<a class="BorderButton" id="{button_id}" {Style.Button.on_border(colors[0], 27, str(top_start)+"%")} {href_str} target="_blank" {EventHandlers.hover(button_id, "HoveredBorderButton")}>&#9783;</a>'
            count += 1

    def __str__(self):
        return f'{self.close_button}{self.extra_buttons}<div {self.div_style} {self.embed_id} {self.hover}><h3 {self.h_style}> {self.title} </h3><p {self.p_style}> {self.text} </p></div>'


class CombinedHeaderPanel(HeaderTextPanel):
    def __init__(self, id, title, text, image_url, colors, h_colors, layout=1, slider=False):
        super().__init__(id, title, text, colors, h_colors, slider)
        self.img_style = Style.Image.original()
        self.image = f'src="{image_url}"'
        self.layout = layout
        self.hover = ""
        if not slider:
            self.hover = EventHandlers.hover(self.id, "HoveredBorder")

    def __str__(self):
        if self.layout == 1:
            return f'<div {self.div_style} {self.embed_id} {self.hover}><h3 {self.h_style}> {self.title} </h2><p {self.p_style}> {self.text} </p><img {self.image} {self.img_style}></div>'
        elif self.layout == 2:
            return f'<div {self.div_style} {self.embed_id} {self.hover}><h3 {self.h_style}> {self.title} </h2><img {self.image} {self.img_style}><p {self.p_style}> {self.text} </p></div>'
        else:
            return f'<div {self.div_style} {self.embed_id} {self.hover}><img {self.image} {self.img_style}><h3 {self.h_style}> {self.title} </h2><p {self.p_style}> {self.text} </p></div>'


class SimpleImagePanel(BasePanel):
    def __init__(self, id, image_url, colors, slider=False):
        super().__init__(id)
        self.div_style = Style.Box.image_info(
            colors[0],  colors[2], slider)
        self.img_style = Style.Image.default()
        self.image = f'src="{image_url}"'
        self.hover = ""
        if not slider:
            self.hover = EventHandlers.hover(self.id, "HoveredBorderFilled")

    def __str__(self):
        return f'<div {self.div_style} {self.embed_id} {self.hover}><img {self.image} {self.img_style}></div>'


class CombinedSimplePanel(SimpleTextPanel):
    def __init__(self, id, text, image_url, colors, layout=1, slider=False):
        super().__init__(id, text, colors, slider)
        self.img_style = Style.Image.original()
        self.image = self.image = f'src="{image_url}"'
        self.layout = layout
        self.hover = ""
        if not slider:
            self.hover = EventHandlers.hover(self.id, "HoveredBorder")

    def __str__(self):
        if self.layout == 1:
            return f'<div {self.div_style} {self.embed_id} {self.hover}><p {self.p_style}> {self.text} </p><img {self.image} {self.img_style}></div>'
        else:
            return f'<div {self.div_style} {self.embed_id} {self.hover}><img {self.image} {self.img_style}><p {self.p_style}> {self.text} </p></div>'


class SimpleVideoPanel(BasePanel):
    def __init__(self, id, url, colors):
        super().__init__(id)
        self.div_style = Style.Box.image_info(
            colors[0],  colors[2])
        self.iframe_style = Style.Video.normal()
        self.video = f'src="{url}"'
        self.hover = EventHandlers.hover(self.id, "HoveredBorder")

    def __str__(self):
        return f'<div {self.div_style} {self.embed_id} {self.hover}><iframe {self.video} {self.iframe_style}></iframe></div>'


class PanelSlider(BasePanel):
    def __init__(self, id, panels, colors):
        super().__init__(id)
        self.hidden = Style.Misc.overflow_hidden()
        self.div_style = Style.Box.slider_info(
            colors[0],  colors[2])
        self.button_left = Style.Button.slider_left(colors[0])
        self.button_right = Style.Button.slider_right(colors[1])
        self.panels = panels
        self.hover = EventHandlers.hover(self.id+"_FACADE", "HoveredBorder")

    def __str__(self):
        panels_str = ""
        for panel in self.panels:
            panels_str += panel.__str__()
        buttons_postfix = f'<button id="{self.id}_LBUTTON" {self.button_left} {EventHandlers.slider_click(-1, self.id)} {EventHandlers.hover(self.id+"_LBUTTON", "HoveredBorderButton")}>&#10094;</button><button id="{self.id}_RBUTTON" {self.button_right} {EventHandlers.slider_click(1, self.id)} {EventHandlers.hover(self.id+"_RBUTTON", "HoveredBorderButton")}>&#10095;</button></div>'
        return f'<div id="{self.id}_FACADE" {self.div_style} {self.hover}>{panels_str}{buttons_postfix}'


class ImagePanelSlider(PanelSlider):
    def __init__(self, id, panels, colors):
        super().__init__(id, panels, colors)
        self.div_style = Style.Box.image_info(
            colors[0],  colors[2])

    def __str__(self):
        panels_str = ""
        for panel in self.panels:
            panels_str += panel.__str__()
        embed_ID = f"'{self.id}'"
        buttons_postfix = f'<button {self.button_left } {EventHandlers.slider_click(-1, embed_ID)}>&#10094;</button><button {self.button_right} {EventHandlers.slider_click(-1, embed_ID)}>&#10095;</button></div>'
        return f'<div {self.div_style} {self.hover}>{panels_str}{buttons_postfix}'


class SimpleMusicSlider(BasePanel):
    def __init__(self, id, src, colors):
        super().__init__(id)
        self.style_box = Style.Box.text_info(
            colors[0],  colors[2]
        )
        self.music = f'src="{src}"'
        self.hover = EventHandlers.hover(self.id, "HoveredBorder")

    def __str__(self):
        return f'<div {self.style_box} {self.embed_id} {self.hover} class="Audio"><audio controls><source {self.music}>Your browser does not support the audio element.</audio>'
