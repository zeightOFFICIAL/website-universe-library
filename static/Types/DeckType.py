from static.Types.CardType import CardClass


class DeckClass:
    def __init__(self, id: int, cards: list[CardClass]):
        self.id = id
        self.cards = cards

    def __repr__(self) -> str:
        cards_str = ""
        for card in self.cards:
            cards_str += card.__repr__()
        wrapper_div = f'<div class="swiper-wrapper">{cards_str}</div>'
        swiper_div = f'<div class="swiper">{wrapper_div}</div>'
        section_div = f"<section>{swiper_div}</section>"
        return section_div
