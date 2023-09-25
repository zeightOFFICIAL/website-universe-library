from static.Types.StyleType import Style


class CardClass:
    def __init__(
        self, id: int, name: str, coloring: list[str], href: str, description: str
    ):
        self.id = id
        self.name = name

        self.coloring = coloring
        self.href = href
        self.short_desc = description

    def __repr__():
        pass
