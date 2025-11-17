from textnode import TextNode, TextType


def main():
    new_text_node = TextNode("This is some text", TextType.plain)
    print(new_text_node)


if __name__ == "__main__":
    main()
