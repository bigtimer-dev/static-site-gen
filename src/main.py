from generate_page import generate_page_recursive
from recursive_copy import recursive_copy
from empty_dir import empty_directory
import os


def sync_folders():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    public = os.path.join(root, "public")
    static = os.path.join(root, "static")
    if not os.path.exists(static):
        raise FileNotFoundError(f"Static folder not found: {static}")
    if not os.path.exists(public):
        os.mkdir(public)
    empty_directory(public)
    recursive_copy(static, public)
    print("Sync complete!")


def creating_pages():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    content = os.path.join(root, "content")
    template = os.path.join(root, "template.html")
    public = os.path.join(root, "public")
    generate_page_recursive(content, template, public)


def main():
    try:
        sync_folders()
        creating_pages()
    except Exception as e:
        print(f"Error Generating: {e}")


if __name__ == "__main__":
    main()
