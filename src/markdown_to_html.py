from markdown_to_blocks import markdown_to_blocks, block_to_block_type, BlockType
from text_to_textnode import text_to_textnode
from textnode import TextNode, text_node_to_html_node
from htmlnode import LeafNode, ParentNode

def markdown_to_html_node(markdown):
    md_blocks = markdown_to_blocks(markdown)
    for md_block in md_blocks:
       

def block_to_childs(block):
    type_block = block_to_block_type(block)
    if type_block == BlockType.paragraph:
        childs = text_node_to_html_node(text_to_textnode(block))
        return ParentNode("p", childs)

    elif type_block == BlockType.code:
        lines = block.split("\n")
        code = "\n".join(lines[1:-1])
        child = LeafNode("code", code)
        return ParentNode("pre",child)

    elif type_block == BlockType.heading:
        lines = block.split("\n")
        i=0
        while i<len(lines[0]) and lines[0][i] == "#":
            i=+1
        char_string = i * "#"
        lines[0].replace(f"{char_string} ","")
        lines = "\n".join(lines)
        childs = text_node_to_html_node(text_to_textnode(lines))
        return ParentNode(f"h{i}", childs)
    
    elif type_block == BlockType.quote:
        lines = block.split("\n")
        for line in lines:
            line.replace(">", "")
        lines = "\n".join(lines)
        childs = text_node_to_html_node(text_to_textnode(lines))
        return ParentNode("blockquote", childs)
    
    elif type_block == BlockType.ordered_list:
        lines = 









