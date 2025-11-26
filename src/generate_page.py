from markdown_to_html import markdown_to_html_node
from extract_title import extract_title
import os


def generate_page(from_path, template_path, dest_path, basepath):
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
    template_content = template_content.replace('href="/', f'href="{basepath}')
    template_content = template_content.replace('src="/', f'src="{basepath}')
    parent_dir = os.path.dirname(dest_path)
    if parent_dir and not os.path.exists(parent_dir):
        os.makedirs(parent_dir, exist_ok=True)
    with open(dest_path, "w") as file:
        file.write(template_content)


def generate_page_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    if os.path.exists(dir_path_content):
        contents_path = os.listdir(dir_path_content)
        for content in contents_path:
            full_path_content = os.path.join(dir_path_content, content)
            full_path_dest = os.path.join(dest_dir_path, content)
            if os.path.isfile(full_path_content) and full_path_content.endswith(".md"):
                full_with_html = full_path_dest[:-3] + ".html"
                generate_page(
                    full_path_content, template_path, full_with_html, basepath
                )

            elif os.path.isdir(full_path_content):
                generate_page_recursive(
                    full_path_content, template_path, full_path_dest, basepath
                )

            else:
                raise Exception(
                    f"Found invalid entry: {full_path_content}. Only .md files and directories are allowed."
                )
    else:
        raise FileNotFoundError(f"{dir_path_content} does not exist")
