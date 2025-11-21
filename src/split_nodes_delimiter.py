from textnode import TextNode, TextType


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
                        new_nodes.append(TextNode(string_split[i], TextType.plain))
                    else:
                        new_nodes.append(TextNode(string_split[i], text_type))

        else:
            new_nodes.append(node)

    return new_nodes
