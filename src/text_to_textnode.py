from textnode import TextType, TextNode
from split_nodes_delimiter import (
    split_nodes_dilimiter,
    split_nodes_link,
    split_nodes_images,
)


def text_to_textnode(text):
    node = [TextNode(text, TextType.plain)]
    node = split_nodes_dilimiter(node, "**", TextType.bold)
    node = split_nodes_dilimiter(node, "_", TextType.italic)
    node = split_nodes_dilimiter(node, "`", TextType.code)
    node = split_nodes_images(node)
    node = split_nodes_link(node)
    return node
