import mysite.Types.ParagraphType as ParagraphType


class ArticleClass:
    def __init__(self, 
        id : int, 
        name : str, 
        topic : str, 
        author : str,
        date: str,
        rating: int,
        paragraphs: list[ParagraphType.BaseParagraphClass]
    ):
        self.id = id
        self.name = name
        self.topic = topic
        self.author = author
        self.date = date
        self.rating = rating
        self.paragraphs = paragraphs
