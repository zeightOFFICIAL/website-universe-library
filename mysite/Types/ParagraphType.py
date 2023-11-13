"""
{
    BASE
        TEXT
        QUOTE
        SOLEIMAGE
        MULTIMAGE
}
"""

class BaseParagraphClass:
    def __init__(
        self,
        id: int,
        a_id: int,
        d_id: int,
        l_calling: str,
    ):
        self.id = id
        self.a_id = a_id
        self.d_id = d_id
        self.l_calling = l_calling
        
class TextParagraph(BaseParagraphClass):
    def __init__(
        self,
        id: int,
        a_id: int,
        d_id: int,
        l_calling: str,
    ):
        super().__init__(id, a_id, d_id, l_calling)
        
class SoleImageParagraph(BaseParagraphClass):
    def __init__(
        self,
        id: int,
        a_id: int,
        d_id: int,
        l_calling: str,
    ):
        super().__init__(id, a_id, d_id, l_calling)