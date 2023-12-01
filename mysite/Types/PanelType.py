from mysite.Types.StyleType import Style
from mysite.Types.StyleType import EventHandlers

"""
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
        SIMPLE_TABLE
}
"""


class BasePanel:
    def __init__(self, id: str):
        self.id = id
        self.embed_id = f'id="{self.id}"'


class SimpleTextPanel(BasePanel):
    def __init__(self, id: str, text: str, colors: list[str], slider=False):
        super().__init__(id)
        self.div_style = Style.Box.text_info(colors[0], colors[2], slider)
        self.p_style = Style.Text.normal()
        self.text = text
        if not slider:
            self.hover = EventHandlers.hover(self.id, "HoveredBorder")
        else:
            self.hover = ""

    def __repr__(self) -> str:
        return f"<div {self.div_style} {self.embed_id} {self.hover}><p {self.p_style}> {self.text} </p></div>"


class TopHeaderTextPanel(SimpleTextPanel):
    def __init__(
        self,
        id: str,
        title: str,
        text: str,
        colors: list[str],
        h_colors: list[str],
        slider=False,
    ):
        super().__init__(id, text, colors, slider)
        self.h_style = Style.Text.header_one(h_colors[0], h_colors[1])
        self.title = title
        if not slider:
            self.hover = EventHandlers.hover(self.id, "HoveredBorder")
        else:
            self.hover = ""

    def __repr__(self) -> str:
        return f"<div {self.div_style} {self.embed_id} {self.hover}><h2 {self.h_style}> {self.title} </h2><p {self.p_style}> {self.text} </p></div>"


class HeaderTextPanel(SimpleTextPanel):
    def __init__(
        self,
        id: str,
        title: str,
        text: str,
        colors: list[str],
        h_colors: list[str] = [],
        slider: bool = False,
        close_button: bool = False,
        extra_buttons: list[str] = [],
    ):
        super().__init__(id, text, colors, slider)
        self.title = title
        if len(h_colors) >= 2:
            self.h_style = Style.Text.header_two(h_colors[0], h_colors[1])
        else:
            self.h_style = Style.Text.header_two(colors[0], colors[1])
        if not slider:
            self.hover = EventHandlers.hover(self.id, "HoveredBorder")
        else:
            self.hover = ""
        self.close_button = ""
        if close_button:
            button_id = f"CLOSE_{self.id}"
            self.close_button = f'<button class="BorderButton" id="{button_id}" {Style.Button.on_border(colors[0])} {EventHandlers.object_click("SYSTEM_INFO")} {EventHandlers.hover(button_id, "HoveredBorderButton")}>&#10006;</button>'
        button_pos_start = 5.5
        button_pos_increment = 15
        self.extra_buttons = ""
        count = 1
        for href in extra_buttons:
            button_pos_start += button_pos_increment
            href_str = f'href="{href}"'
            button_id = f"EXTRA_INFO{self.id}{count}"
            self.extra_buttons += f'<a class="BorderButton" id="{button_id}" {Style.Button.on_border(colors[0], 3.5, str(button_pos_start)+"%")} {href_str} target="_blank" {EventHandlers.hover(button_id, "HoveredBorderButton")}>&#9783;</a>'
            count += 1

    def __repr__(self) -> str:
        return f"{self.close_button}{self.extra_buttons}<div {self.div_style} {self.embed_id} {self.hover}><h3 {self.h_style}> {self.title} </h3><p {self.p_style}> {self.text} </p></div>"


class CombinedHeaderPanel(HeaderTextPanel):
    def __init__(
        self,
        id: str,
        title: str,
        text: str,
        image_url: str,
        colors: list[str],
        h_colors: list[str],
        layout: int = 1,
        slider: bool = False,
    ):
        super().__init__(id, title, text, colors, h_colors, slider)
        self.img_style = Style.Image.original()
        self.image = f'src="{image_url}"'
        self.layout = layout
        if len(h_colors) >= 2:
            self.h_style = Style.Text.header_two(h_colors[0], h_colors[1])
        else:
            self.h_style = Style.Text.header_two(colors[0], colors[1])
        if not slider:
            self.hover = EventHandlers.hover(self.id, "HoveredBorder")
        else:
            self.hover = ""

    def __repr__(self) -> str:
        if self.layout == 1:
            return f'<div {self.div_style} {self.embed_id} {self.hover}><h3 {self.h_style}> {self.title} </h2><p {self.p_style}> {self.text} </p><img loading="lazy" class="LazyLoad" {self.image} {self.img_style}></div>'
        elif self.layout == 2:
            return f'<div {self.div_style} {self.embed_id} {self.hover}><h3 {self.h_style}> {self.title} </h2><img  loading="lazy" class="LazyLoad" {self.image} {self.img_style}><p {self.p_style}> {self.text} </p></div>'
        else:
            return f'<div {self.div_style} {self.embed_id} {self.hover}><img loading="lazy" class="LazyLoad" {self.image} {self.img_style}><h3 {self.h_style}> {self.title} </h2><p {self.p_style}> {self.text} </p></div>'


class SimpleImagePanel(BasePanel):
    def __init__(
        self, id: str, image_url: str, colors: list[str], slider: bool = False
    ):
        super().__init__(id)
        self.div_style = Style.Box.image_info(colors[0], colors[2], slider)
        self.img_style = Style.Image.default()
        self.image = f'src="{image_url}"'
        if not slider:
            self.hover = EventHandlers.hover(self.id, "HoveredBorder")
        else:
            self.hover = ""

    def __repr__(self) -> str:
        return f'<div {self.div_style} {self.embed_id} {self.hover}><img {self.image} {self.img_style} class="LazyLoad" loading="lazy"></div>'


class CombinedSimplePanel(SimpleTextPanel):
    def __init__(
        self,
        id: str,
        text: str,
        image_url: str,
        colors: list[str],
        layout: int = 1,
        slider: bool = False,
    ):
        super().__init__(id, text, colors, slider)
        self.img_style = Style.Image.original()
        self.image = self.image = f'src="{image_url}"'
        self.layout = layout
        if not slider:
            self.hover = EventHandlers.hover(self.id, "HoveredBorder")
        else:
            self.hover = ""

    def __repr__(self) -> str:
        if self.layout == 1:
            return f'<div {self.div_style} {self.embed_id} {self.hover}><p {self.p_style}> {self.text} </p><img loading="lazy" class="LazyLoad" {self.image} {self.img_style}></div>'
        else:
            return f'<div {self.div_style} {self.embed_id} {self.hover}><img  loading="lazy" class="LazyLoad" {self.image} {self.img_style}><p {self.p_style}> {self.text} </p></div>'


class SimpleVideoPanel(BasePanel):
    def __init__(self, id: str, url: str, colors: list[str]):
        super().__init__(id)
        self.div_style = Style.Box.image_info(colors[0], colors[2])
        self.iframe_style = Style.Video.normal()
        self.video = f'src="{url}"'
        self.hover = EventHandlers.hover(self.id, "HoveredBorder")

    def __repr__(self) -> str:
        return f'<div {self.div_style} {self.embed_id} {self.hover}><iframe {self.video} {self.iframe_style} loading="lazy"></iframe></div>'


class PanelSlider(BasePanel):
    def __init__(self, id: str, panels: list[BasePanel], colors: list[str]):
        super().__init__(id)
        self.hidden = Style.Misc.overflow_hidden()
        self.div_style = Style.Box.slider_info(colors[0], colors[2])
        self.button_left = Style.Button.slider_left(colors[0])
        self.button_right = Style.Button.slider_right(colors[1])
        self.panels = panels
        self.hover = EventHandlers.hover(self.id + "_FACADE", "HoveredBorder")

    def __repr__(self) -> str:
        panels_str = ""
        for panel in self.panels:
            panels_str += panel.__repr__()
        buttons_postfix = f'<button id="{self.id}_LBUTTON" {self.button_left} {EventHandlers.slider_click(-1, self.id)} {EventHandlers.hover(self.id+"_LBUTTON", "HoveredBorderButton")}>&#10094;</button><button id="{self.id}_RBUTTON" {self.button_right} {EventHandlers.slider_click(1, self.id)} {EventHandlers.hover(self.id+"_RBUTTON", "HoveredBorderButton")}>&#10095;</button></div>'
        return f'<div id="{self.id}_FACADE" {self.div_style} {self.hover}>{panels_str}{buttons_postfix}'


class SimpleMusicSlider(BasePanel):
    def __init__(self, id: str, src: str, colors: list[str]):
        super().__init__(id)
        self.style_box = Style.Box.image_info(colors[0], colors[2])
        self.music = f'src="{src}"'
        self.hover = EventHandlers.hover(self.id, "HoveredBorderFilled")

    def __repr__(self) -> str:
        return f'<div {self.style_box} {self.embed_id} {self.hover} class="AudioDiv" loading="lazy"><audio controls class="Audio"><source {self.music}>Your browser does not support the audio element.</audio></div>'


class SimpleTable(BasePanel):
    def __init__(self, id: str, text: str, colors: list[str]):
        super().__init__(id)
        self.div_style = Style.Box.text_info(colors[0], colors[2])
        self.text_style = Style.Text.normal()
        self.table_style = Style.Tables.table()
        self.ths_style = Style.Tables.ths()
        self.hover = EventHandlers.hover(self.id, "HoveredBorder")
        self.text = text

    def __repr__(self) -> str:
        table_content = ""
        for values in self.text.split(";"):
            if len(values) < 2:
                continue
            print(values.split(":")[0])
            table_content += f"<tr {self.text_style}><th {self.ths_style}>{values.split(':')[0]}</th><th {self.ths_style}>{values.split(':')[1]}</th></tr>"

        return f"<div {self.div_style} {self.embed_id} {self.hover}><table {self.table_style}>{table_content}</table></div>"
