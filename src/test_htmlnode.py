import unittest

from htmlnode import HTMLNode


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
