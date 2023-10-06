from static.Types.StyleType import Style
from static.Types.StyleType import EventHandlers


class CardClass:
    def __init__(
        self,
        id: int,
        name: str,
        href: str,
        text: str,
        coloring_set: list[str],
        card_img: str,
        dropdown_img: str,
    ):
        self.id = id
        self.name = name
        self.href = href

        self.text = text
        self.coloring_set = coloring_set
        self.card_img_name = card_img
        self.dropdown_img_name = dropdown_img

    def __repr__(self) -> str:
        card_style = Style.Box.card_info(
            self.coloring_set[0], f"{self.card_img_name}-sml.jpg"
        )
        title_style = Style.Text.title_font(self.coloring_set[0])
        text_style = Style.Text.card_text_font(self.coloring_set[0])
        dropdown_img_style = Style.Image.thumb("load.png")
        href = f'href="{self.href}"' if self.href.__len__() > 2 else ""
        hover_handler = EventHandlers.hover_4d(
            f"{self.href}_CARD",
            f"{self.href}_TITLE",
            f"{self.href}_DROPIMG",
            f"{self.href}_TEXT",
            "CardHovered",
            "TitleHovered",
            "DropImageHovered",
            "TextHovered",
        )

        drop_img_div = f'<div id="{self.href}_IMG" class="DropDownImg LazyLoad"><img id="{self.href}_DROPIMG" src="../static/LinkImages/{self.dropdown_img_name}.png" {dropdown_img_style} alt="{self.href} image" loading="lazy" /></div>'

        card_div = f'<div id="{self.href}_CARD" class="Card LazyLoad" {card_style}><img id="{self.href}_BACK" src="../static/Images/{self.card_img_name}.jpg" class="BackCardImage" alt="{self.href} image" loading="lazy" /></div>'

        text_div = f'<div id="{self.href}_TEXT" class="CardText" {text_style}>{self.text}</div>'

        title_div = f'<a {href} class="Anchor"><div id="{self.href}_TITLE" class="Title" {title_style} {hover_handler}>{self.name.upper()}</div></a>'

        representation = f'<div class="swiper-slide"> {drop_img_div} {card_div} {text_div} {title_div} </div>'
        return representation
