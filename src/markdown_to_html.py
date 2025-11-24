from markdown_to_blocks import markdown_to_blocks, block_to_block_type, BlockType
from text_to_textnode import text_to_textnode
from textnode import text_node_to_html_node
from htmlnode import LeafNode, ParentNode


def markdown_to_html_node(markdown):
    md_blocks = markdown_to_blocks(markdown)
    childs = []
    for md_block in md_blocks:
        childs.append(block_to_childs(md_block))
    return ParentNode("div", childs)


def block_to_childs(block):
    type_block = block_to_block_type(block)
    if type_block == BlockType.paragraph:
        block = block.split("\n")
        block = " ".join(block)
        text_nodes = text_to_textnode(block)
        childs = help_txt_node_to_html_node(text_nodes)
        return ParentNode("p", childs)

    elif type_block == BlockType.code:
        lines = block.split("\n")
        inner = lines[1:-1]
        code = "\n".join(inner)
        code += "\n"
        child = [LeafNode("code", code)]
        return ParentNode("pre", child)

    elif type_block == BlockType.heading:
        lines = block.split("\n")
        i = 0
        while i < len(lines[0]) and lines[0][i] == "#":
            i += 1
        char_string = i * "#"
        lines[0] = lines[0].replace(f"{char_string} ", "")
        lines = " ".join(lines)
        text_nodes = text_to_textnode(lines)
        childs = help_txt_node_to_html_node(text_nodes)
        return ParentNode(f"h{i}", childs)

    elif type_block == BlockType.quote:
        lines = block.split("\n")
        list_of_line = []
        for line in lines:
            if line[0:2] == "> ":
                line = line.replace("> ", "")
                list_of_line.append(line)
            else:
                line = line.replace(">", "")
                list_of_line.append(line)

        lines = " ".join(list_of_line)
        text_nodes = text_to_textnode(lines)
        childs = help_txt_node_to_html_node(text_nodes)
        return ParentNode("blockquote", childs)

    elif type_block == BlockType.ordered_list:
        lines = block.split("\n")
        childs = []
        for index, line in enumerate(lines, start=1):
            line = line.replace(f"{index}. ", "")
            text_nodes = text_to_textnode(line)
            childs.append(ParentNode("li", help_txt_node_to_html_node(text_nodes)))
        return ParentNode("ol", childs)

    elif type_block == BlockType.unordered_list:
        lines = block.split("\n")
        childs = []
        for line in lines:
            line = line.replace("- ", "")
            text_nodes = text_to_textnode(line)
            childs.append(ParentNode("li", help_txt_node_to_html_node(text_nodes)))
        return ParentNode("ul", childs)


def help_txt_node_to_html_node(nodes):
    html_nodes = []
    for node in nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes
