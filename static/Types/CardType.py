from static.Types.StyleType import Style, EventHandlers
import os
from django.conf import settings


class CardClass:
    def __init__(
        self,
        id: int,
        name: str,
        thumbnail_img: str,
        coloring_set: list[str],
        href: str,
        text: str,
        back_img: str,
    ):
        self.id = id
        self.name = name

        self.thumbnail_img_name = thumbnail_img
        self.coloring_set = coloring_set
        self.href = href
        self.text = text
        self.back_img_name = back_img

    def __repr__(self) -> str:
        if not os.path.exists(
            f"{settings.BASE_DIR}\static\LinkImages\{self.thumbnail_img_name}"
        ):
            self.thumbnail_img_name = "default.png"

        style_card = Style.Box.card_info(self.coloring_set[0], self.back_img_name)
        style_title = Style.Text.title_font(self.coloring_set[0])
        style_thumbnail = Style.Image.thumb()
        style_text = Style.Text.card_text_font(self.coloring_set[0])

        hover_handler = EventHandlers.hover_4d(
            f"{self.href}_CARD",
            f"{self.href}_TITLE",
            f"{self.href}_COVER",
            f"{self.href}_TEXT",
            "CardHovered",
            "TitleHovered",
            "CardCoverHovered",
            "CardTextHovered",
        )
        href = f'href="{self.href}"' if self.href.__len__() > 2 else ""

        img_div = f'<img id="{self.href}_COVER" src="../static/LinkImages/{self.thumbnail_img_name}" {style_thumbnail}></img>'
        card_div = f'<div id="{self.href}_CARD" class="Card" {style_card}></div>'
        title_div = f'<a {href} style="text-decoration:none;"><div id="{self.href}_TITLE" class="Title" {style_title} {hover_handler}>{self.name.upper()}</div></a>'
        text_div = f'<div id="{self.href}_TEXT" class="CardText" {style_text}>{self.text}</div>'

        main_div = (
            f'<div class="swiper-slide">{img_div}{card_div}{text_div}{title_div}</div>'
        )
        return main_div
