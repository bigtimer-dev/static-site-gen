def markdown_to_blocks(md_text):
    raw_blocks = md_text.strip().split("\n\n")

    blocks = []
    for block in raw_blocks:
        lines = block.split("\n")
        clean_lines = [line.strip() for line in lines if line.strip()]
        if clean_lines:
            blocks.append("\n".join(clean_lines))

    return blocks
