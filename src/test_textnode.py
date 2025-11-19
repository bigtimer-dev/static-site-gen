import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.bold)
        node2 = TextNode("This is a text node", TextType.bold)
        self.assertEqual(node, node2)

    def test_eq1(self):
        node = TextNode("image", TextType.image, "https://www.google.com/")
        node2 = TextNode("image", TextType.image, "https://www.google.com/")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("this is image", TextType.image, "https://www.google.com/")
        node2 = TextNode("this is image", TextType.image)
        self.assertNotEqual(node, node2)

    def test_not_eq1(self):
        node = TextNode("This is italic", TextType.italic)
        node2 = TextNode("This is bold", TextType.bold)
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.plain)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text2(self):
        node = TextNode("This is bold", TextType.bold)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.to_html(), "<b>This is bold</b>")

    def test_text3(self):
        node = TextNode("This is italic", TextType.italic)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.to_html(), "<i>This is italic</i>")

    def test_text4(self):
        node = TextNode("this is alt text", TextType.image, "www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(
            html_node.to_html(),
            '<img src="www.google.com" alt="this is alt text"></img>',
        )


if __name__ == "__main__":
    unittest.main()
