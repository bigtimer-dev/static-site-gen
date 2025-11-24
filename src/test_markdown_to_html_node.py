import unittest
from markdown_to_html import markdown_to_html_node


class TestMarkdownToHtml(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
        ```
        This is text that _should_ remain
        the **same** even with inline stuff
        ```
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading(self):
        md = """
### This is a _heading_ with **inline** text
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>This is a <i>heading</i> with <b>inline</b> text</h3></div>",
        )

    def test_blockquote(self):
        md = """
> This is a quote
> with **bold** and _italic_
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote with <b>bold</b> and <i>italic</i></blockquote></div>",
        )

    def test_ordered_list(self):
        md = """
1. First **item**
2. Second _item_
3. Third `code`
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol>"
            "<li>First <b>item</b></li>"
            "<li>Second <i>item</i></li>"
            "<li>Third <code>code</code></li>"
            "</ol></div>",
        )

    def test_unordered_list(self):
        md = """
- One **bold**
- Two _italic_
- Three `code`
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul>"
            "<li>One <b>bold</b></li>"
            "<li>Two <i>italic</i></li>"
            "<li>Three <code>code</code></li>"
            "</ul></div>",
        )
