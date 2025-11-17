import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()
