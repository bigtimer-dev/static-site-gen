import unittest
from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_images, split_nodes_link


class TestSplitNode(unittest.TestCase):
    def test_nodes_image1(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.plain,
        )
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.plain),
                TextNode("image", TextType.image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.plain),
                TextNode(
                    "second image", TextType.image, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_nodes_link1(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.plain,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.plain),
                TextNode("link", TextType.link, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.plain),
                TextNode(
                    "second link", TextType.link, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_nodes_link_none(self):
        node = TextNode(
            "There are no links in this text.",
            TextType.plain,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("There are no links in this text.", TextType.plain),
            ],
            new_nodes,
        )

    def test_nodes_image_none(self):
        node = TextNode(
            "There are zero images here.",
            TextType.plain,
        )
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("There are zero images here.", TextType.plain),
            ],
            new_nodes,
        )

    def test_nodes_mixed_image_then_link(self):
        node = TextNode(
            "Here is an ![img](https://example.com/a.png) and a [link](https://example.com/b)",
            TextType.plain,
        )
        new_nodes = split_nodes_images([node])
        new_nodes = split_nodes_link(new_nodes)

        self.assertListEqual(
            [
                TextNode("Here is an ", TextType.plain),
                TextNode("img", TextType.image, "https://example.com/a.png"),
                TextNode(" and a ", TextType.plain),
                TextNode("link", TextType.link, "https://example.com/b"),
            ],
            new_nodes,
        )

    def test_nodes_mixed_link_then_image(self):
        node = TextNode(
            "Start with a [link](https://example.com/a) then an image ![img](https://example.com/b.png)",
            TextType.plain,
        )
        new_nodes = split_nodes_images([node])
        new_nodes = split_nodes_link(new_nodes)

        self.assertListEqual(
            [
                TextNode("Start with a ", TextType.plain),
                TextNode("link", TextType.link, "https://example.com/a"),
                TextNode(" then an image ", TextType.plain),
                TextNode("img", TextType.image, "https://example.com/b.png"),
            ],
            new_nodes,
        )
