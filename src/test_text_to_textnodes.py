from textnode import TextNode, TextType
from text_to_textnode import text_to_textnode
import unittest


class TestTextToNode(unittest.TestCase):
    def test_text_to_node(self):
        raw_text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        list_of_nodes = text_to_textnode(raw_text)
        self.assertEqual(
            list_of_nodes,
            [
                TextNode("This is ", TextType.plain),
                TextNode("text", TextType.bold),
                TextNode(" with an ", TextType.plain),
                TextNode("italic", TextType.italic),
                TextNode(" word and a ", TextType.plain),
                TextNode("code block", TextType.code),
                TextNode(" and an ", TextType.plain),
                TextNode(
                    "obi wan image", TextType.image, "https://i.imgur.com/fJRm4Vk.jpeg"
                ),
                TextNode(" and a ", TextType.plain),
                TextNode("link", TextType.link, "https://boot.dev"),
            ],
        )

    def test_text_to_node2(self):
        raw_text = "This is _text_ with an _italic_ word and a **bold block** and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        list_of_nodes = text_to_textnode(raw_text)
        self.assertEqual(
            list_of_nodes,
            [
                TextNode("This is ", TextType.plain),
                TextNode("text", TextType.italic),
                TextNode(" with an ", TextType.plain),
                TextNode("italic", TextType.italic),
                TextNode(" word and a ", TextType.plain),
                TextNode("bold block", TextType.bold),
                TextNode(" and an ", TextType.plain),
                TextNode(
                    "obi wan image", TextType.image, "https://i.imgur.com/fJRm4Vk.jpeg"
                ),
                TextNode(" and a ", TextType.plain),
                TextNode("link", TextType.link, "https://boot.dev"),
            ],
        )

    def test_text_to_node3(self):
        raw_text = "**bold**_italic_"
        list_of_nodes = text_to_textnode(raw_text)
        self.assertEqual(
            list_of_nodes,
            [
                TextNode("bold", TextType.bold),
                TextNode("italic", TextType.italic),
            ],
        )
