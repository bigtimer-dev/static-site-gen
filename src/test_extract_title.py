import unittest
from extract_title import extract_title  # update to your real module name


class TestExtractTitle(unittest.TestCase):
    def test_simple_title(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_title_with_extra_spaces(self):
        self.assertEqual(extract_title("#   My Title   "), "My Title")

    def test_title_not_first_line(self):
        md = "Some text\n# Title\nMore text"
        self.assertEqual(extract_title(md), "Title")

    def test_only_h1_matches(self):
        md = "## Not this one\n### Also not this\n# Correct Title"
        self.assertEqual(extract_title(md), "Correct Title")

    def test_no_h1_raises(self):
        md = "## Subtitle\nNo real title here"
        with self.assertRaises(Exception):
            extract_title(md)

    def test_multiline_sections(self):
        md = "# My Title\n\nParagraph text\nMore text"
        self.assertEqual(extract_title(md), "My Title")

    def test_title_with_tabs_and_spaces(self):
        self.assertEqual(extract_title("# \t Hello World  "), "Hello World")
