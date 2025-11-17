from enum import Enum


class TextType(Enum):
    plain = "plain"
    bold = "bold"
    italic = "italic"
    code = "code"
    link = "link"
    image = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text

        if not isinstance(text_type, TextType):
            raise TypeError(
                "the text_type is not allow.Allow types are: plain,bold,italic,code,link,image"
            )

        self.text_type = TextType(text_type)
        self.url = url

    def __eq__(self, other):
        if isinstance(other, TextNode):
            return (
                self.text == other.text
                and self.url == other.url
                and self.text_type == other.text_type
            )
        raise TypeError("The objects are not the same type")

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
