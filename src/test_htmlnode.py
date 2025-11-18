import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_op_Iqual(self):
        node = HTMLNode(
            None,
            None,
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        node2 = HTMLNode(
            None,
            None,
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        self.assertEqual(node.props_to_html(), node2.props_to_html())

    def test_op_notIqual(self):
        node = HTMLNode(
            None,
            None,
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        node2 = HTMLNode(
            None,
            None,
            None,
            {
                "href": "https://www.google.com",
                "target": "_blan",
            },
        )
        self.assertNotEqual(node.props_to_html(), node2.props_to_html())

    def test_op_Iqual2(self):
        node = HTMLNode(
            None,
            None,
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
                "random": "bullshit",
            },
        )
        node2 = HTMLNode(
            None,
            None,
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
                "random": "bullshit",
            },
        )
        self.assertEqual(node.props_to_html(), node2.props_to_html())

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_p1(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )

    def test_leaf_to_html_p2(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(), "<div><span><b>grandchild</b></span></div>"
        )

    def test_to_html_with_lot_of_child(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )
