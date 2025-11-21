import unittest

from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_dilimiter


class TestTextNode(unittest.TestCase):
    def test_delimiter1(self):
        node = TextNode(
            "This is a text node **this is bold** hello",
            TextType.plain,
        )
        old_node = []
        old_node.append(node)
        new_node = split_nodes_dilimiter(old_node, "**", TextType.bold)
        self.assertEqual(
            new_node,
            [
                TextNode("This is a text node ", TextType.plain, None),
                TextNode("this is bold", TextType.bold, None),
                TextNode(" hello", TextType.plain, None),
            ],
        )

    def test_delimiter2(self):
        node = TextNode(
            "This is a text node _this is italic_ hello",
            TextType.plain,
        )
        old_node = []
        old_node.append(node)
        new_node = split_nodes_dilimiter(old_node, "_", TextType.italic)
        self.assertEqual(
            new_node,
            [
                TextNode("This is a text node ", TextType.plain, None),
                TextNode("this is italic", TextType.italic, None),
                TextNode(" hello", TextType.plain, None),
            ],
        )

    def test_delimiter2(self):
        node = TextNode(
            "This is a text node _this is italic_ hello",
            TextType.plain,
        )
        old_node = []
        old_node.append(node)
        new_node = split_nodes_dilimiter(old_node, "_", TextType.italic)
        self.assertEqual(
            new_node,
            [
                TextNode("This is a text node ", TextType.plain, None),
                TextNode("this is italic", TextType.italic, None),
                TextNode(" hello", TextType.plain, None),
            ],
        )

    def test_delimiter3(self):
        node = TextNode(
            "This is `code` here",
            TextType.plain,
        )
        old_node = []
        old_node.append(node)
        new_node = split_nodes_dilimiter(old_node, "`", TextType.code)
        self.assertEqual(
            new_node,
            [
                TextNode("This is ", TextType.plain, None),
                TextNode("code", TextType.code, None),
                TextNode(" here", TextType.plain, None),
            ],
        )

    def test_delimiter4(self):
        node = TextNode(
            "This is text",
            TextType.plain,
        )
        old_node = []
        old_node.append(node)
        new_node = split_nodes_dilimiter(old_node, "_", TextType.italic)
        self.assertEqual(
            new_node,
            [
                TextNode("This is text", TextType.plain, None),
            ],
        )

    def test_delimiter5(self):
        node = TextNode(
            "Hello _one_ and _two_!",
            TextType.plain,
        )
        old_node = []
        old_node.append(node)
        new_node = split_nodes_dilimiter(old_node, "_", TextType.italic)
        self.assertEqual(
            new_node,
            [
                TextNode("Hello ", TextType.plain, None),
                TextNode("one", TextType.italic, None),
                TextNode(" and ", TextType.plain, None),
                TextNode("two", TextType.italic, None),
                TextNode("!", TextType.plain),
            ],
        )

    def test_delimiter6(self):
        node = TextNode(
            "This is _broken text",
            TextType.plain,
        )
        old_node = []
        old_node.append(node)
        with self.assertRaises(Exception):
            split_nodes_dilimiter(old_node, "_", TextType.italic)
