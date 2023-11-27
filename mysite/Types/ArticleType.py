class ArticleClass:
    def __init__(
        self,
        id: int,
        name: str,
        topic: str,
        date: str,
        author: str,
        title: str,
        title_img: str,
    ):
        self.id = id
        self.name = name
        self.topic = topic
        self.date = date
        self.author = author
        self.title = title
        self.title_img = title_img

    def __repr__(self):
        pass
