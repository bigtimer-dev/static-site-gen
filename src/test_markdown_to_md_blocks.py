import unittest
from markdown_to_blocks import markdown_to_blocks


class TestMDBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_extra_whitespace(self):
        md = """

            First paragraph with indentation

        
            Second paragraph after multiple blank lines

        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "First paragraph with indentation",
                "Second paragraph after multiple blank lines",
            ],
        )

    def test_markdown_to_blocks_list(self):
        md = """
        Start paragraph

        - a
        - b
        - c

        End paragraph
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "Start paragraph",
                "- a\n- b\n- c",
                "End paragraph",
            ],
        )
