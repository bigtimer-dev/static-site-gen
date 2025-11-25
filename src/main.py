from generate_page import generate_page
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


def creating_page():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    content_index = os.path.join(root, "content/index.md")
    template = os.path.join(root, "template.html")
    public_index = os.path.join(root, "public/index.html")
    generate_page(content_index, template, public_index)


def main():
    try:
        sync_folders()
        creating_page()
    except Exception as e:
        print(f"Error Generating: {e}")


if __name__ == "__main__":
    main()
