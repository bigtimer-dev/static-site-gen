import re


def extract_markdown_images(text):
    we_got_this = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return we_got_this


def extract_markdown_link(text):
    we_got_this = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return we_got_this
