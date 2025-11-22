from textnode import TextNode, TextType
from extract_markdown_links_images import extract_markdown_images, extract_markdown_link


def split_nodes_dilimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.plain:
            string_split = node.text.split(delimiter)
            if len(string_split) % 2 == 0:
                raise Exception("FIX YOUR SHT MARKDOWN")
            else:
                for i in range(0, len(string_split)):
                    if i % 2 == 0:
                        if string_split[i]:
                            new_nodes.append(TextNode(string_split[i], TextType.plain))
                    else:
                        if string_split[i]:
                            new_nodes.append(TextNode(string_split[i], text_type))

        else:
            new_nodes.append(node)

    return new_nodes


def split_nodes_images(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type == TextType.plain:
            current_text = old_node.text
            list_of_extracts = extract_markdown_images(current_text)
            if len(list_of_extracts) == 0:
                new_nodes.append(old_node)
            else:
                for alt, url in list_of_extracts:
                    split_text = current_text.split(f"![{alt}]({url})", maxsplit=1)
                    if split_text[0]:
                        new_nodes.append(TextNode(split_text[0], TextType.plain))
                    new_nodes.append(TextNode(alt, TextType.image, url))
                    current_text = split_text[1]
                if current_text:
                    new_nodes.append(TextNode(current_text, TextType.plain))
        else:
            new_nodes.append(old_node)

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type == TextType.plain:
            current_text = old_node.text
            list_of_extracts = extract_markdown_link(current_text)
            if len(list_of_extracts) == 0:
                new_nodes.append(old_node)
            else:
                for alt, url in list_of_extracts:
                    split_text = current_text.split(f"[{alt}]({url})", maxsplit=1)
                    if split_text[0]:
                        new_nodes.append(TextNode(split_text[0], TextType.plain))
                    new_nodes.append(TextNode(alt, TextType.link, url))
                    current_text = split_text[1]
                if current_text:
                    new_nodes.append(TextNode(current_text, TextType.plain))
        else:
            new_nodes.append(old_node)

    return new_nodes
