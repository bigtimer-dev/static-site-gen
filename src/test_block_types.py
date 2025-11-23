import unittest
from markdown_to_blocks import block_to_block_type, BlockType


class TestBlockToBlockType(unittest.TestCase):
    def test_heading1(self):
        block = "# Heading text"
        self.assertEqual(block_to_block_type(block), BlockType.heading)

    def test_heading6(self):
        block = "###### Heading 6"
        self.assertEqual(block_to_block_type(block), BlockType.heading)

    def test_code_block(self):
        block = "```\nprint('hi')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.code)

    def test_code_block2(self):
        block = "```print('hello word')\nprint('hi')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.code)

    def test_quote_block(self):
        block = "> a quote\n> another line"
        self.assertEqual(block_to_block_type(block), BlockType.quote)

    def test_unordered_list(self):
        block = "- item one\n- item two\n- item three"
        self.assertEqual(block_to_block_type(block), BlockType.unordered_list)

    def test_ordered_list(self):
        block = "1. first\n2. second\n3. third"
        self.assertEqual(block_to_block_type(block), BlockType.ordered_list)

    def test_ordered_list2(self):
        block = "2. first\n3. second"
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)

    def test_paragraph(self):
        block = "This is just a normal paragraph."
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)
