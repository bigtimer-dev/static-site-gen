from enum import Enum
from htmlnode import LeafNode


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


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.bold:
            return LeafNode("b", text_node.text)
        case TextType.plain:
            return LeafNode(None, text_node.text)
        case TextType.code:
            return LeafNode("code", text_node.text)
        case TextType.italic:
            return LeafNode("i", text_node.text)
        case TextType.link:
            my_dict = {}
            my_dict["href"] = text_node.url
            return LeafNode("a", text_node.text, my_dict)
        case TextType.image:
            my_dict = {
                "src": text_node.url,
                "alt": text_node.text,
            }
            return LeafNode("img", "", my_dict)

        case _:
            raise Exception("the text type does not exists")
