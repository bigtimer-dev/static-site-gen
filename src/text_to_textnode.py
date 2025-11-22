from textnode import TextType, TextNode
from split_nodes_delimiter import (
    split_nodes_dilimiter,
    split_nodes_link,
    split_nodes_images,
)


def text_to_textnode(text):
    node = [TextNode(text, TextType.plain)]
    bold = split_nodes_dilimiter(node, "**", TextType.bold)
    italic = split_nodes_dilimiter(bold, "_", TextType.italic)
    code = split_nodes_dilimiter(italic, "`", TextType.code)
    images = split_nodes_images(code)
    link = split_nodes_link(images)
    return link
