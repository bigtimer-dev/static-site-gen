from markdown_to_html import markdown_to_html_node
from extract_title import extract_title
import os


def generate_page(from_path, template_path, dest_path):
    if not os.path.exists(from_path):
        raise FileNotFoundError(f"{from_path} does not exists")
    elif not os.path.exists(template_path):
        raise FileNotFoundError(f"{template_path} does not exists")
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as md:
        md_content = md.read()
    with open(template_path, "r") as template:
        template_content = template.read()
    html_node = markdown_to_html_node(md_content)
    html_string = html_node.to_html()
    title = extract_title(md_content)
    template_content = template_content.replace("{{ Title }}", f"{title}")
    template_content = template_content.replace("{{ Content }}", f"{html_string}")
    parent_dir = os.path.dirname(dest_path)
    if parent_dir and not os.path.exists(parent_dir):
        os.makedirs(parent_dir, exist_ok=True)
    with open(dest_path, "w") as file:
        file.write(template_content)
