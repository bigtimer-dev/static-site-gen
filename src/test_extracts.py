import unittest

from extract_markdown_links_images import extract_markdown_images, extract_markdown_link


class TestTextNode(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_link(self):
        matches = extract_markdown_link(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
            matches,
        )

    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images(
            "Here is ![one](http://a.com/1.png) and ![two](http://a.com/2.jpg)"
        )

        self.assertListEqual(
            [
                ("one", "http://a.com/1.png"),
                ("two", "http://a.com/2.jpg"),
            ],
            matches,
        )

    def test_extract_markdown_images_none(self):
        matches = extract_markdown_images("No images here at all")
        self.assertListEqual([], matches)

    def test_extract_markdown_images_empty_alt(self):
        matches = extract_markdown_images("Look ![](http://example.com/x.png)")
        self.assertListEqual([("", "http://example.com/x.png")], matches)

    def test_extract_markdown_images_malformed(self):
        # Should ignore malformed markdown
        matches = extract_markdown_images("Broken ![img(http://example.com/x.png)")
        self.assertListEqual([], matches)

    def test_extract_markdown_link_multiple(self):
        matches = extract_markdown_link(
            "Links: [a](http://a.com) and [b](http://b.com)"
        )
        self.assertListEqual(
            [
                ("a", "http://a.com"),
                ("b", "http://b.com"),
            ],
            matches,
        )

    def test_extract_markdown_link_none(self):
        matches = extract_markdown_link("Text without links")
        self.assertListEqual([], matches)

    def test_extract_markdown_link_empty_text(self):
        matches = extract_markdown_link("[](/empty/text)")
        self.assertListEqual([("", "/empty/text")], matches)

    def test_extract_markdown_link_malformed(self):
        matches = extract_markdown_link("Broken [link(http://example.com)")
        self.assertListEqual([], matches)
