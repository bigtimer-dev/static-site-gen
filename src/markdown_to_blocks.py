from enum import Enum


def markdown_to_blocks(md_text):
    raw_blocks = md_text.strip().split("\n\n")

    blocks = []
    for block in raw_blocks:
        lines = block.split("\n")
        clean_lines = [line.strip() for line in lines if line.strip()]
        if clean_lines:
            blocks.append("\n".join(clean_lines))

    return blocks


class BlockType(Enum):
    paragraph = "paragraph"
    heading = "heading"
    code = "code"
    quote = "quote"
    unordered_list = "unordered_list"
    ordered_list = "ordered_list"


def block_to_block_type(block):
    lines = block.split("\n")
    if lines[0].startswith("#"):
        i = 0
        while i < len(lines[0]) and lines[0][i] == "#":
            i += 1

        if 1 <= i <= 6 and len(lines[0]) > i and lines[0][i] == " ":
            return BlockType.heading

    if lines[0].startswith("```") and lines[-1].endswith("```"):
        return BlockType.code

    if all(line.startswith(">") for line in lines):
        return BlockType.quote

    if all(line.startswith("- ") for line in lines):
        return BlockType.unordered_list

    order = True
    for index, line in enumerate(lines, start=1):
        is_this = f"{index}. "
        if not line.startswith(is_this):
            order = False
            break
    if order:
        return BlockType.ordered_list

    return BlockType.paragraph
