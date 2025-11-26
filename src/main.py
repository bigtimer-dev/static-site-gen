from generate_page import generate_page_recursive
from recursive_copy import recursive_copy
from empty_dir import empty_directory
import os
import sys

if len(sys.argv) == 2:
    basepath = sys.argv[1]
else:
    basepath = "/"


def sync_folders():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    docs = os.path.join(root, "docs")
    static = os.path.join(root, "static")
    if not os.path.exists(static):
        raise FileNotFoundError(f"Static folder not found: {static}")
    if not os.path.exists(docs):
        os.mkdir(docs)
    empty_directory(docs)
    recursive_copy(static, docs)
    print("Sync complete!")


def creating_pages():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    content = os.path.join(root, "content")
    template = os.path.join(root, "template.html")
    docs = os.path.join(root, "docs")
    generate_page_recursive(content, template, docs, basepath)


def main():
    try:
        sync_folders()
        creating_pages()
    except Exception as e:
        print(f"Error Generating: {e}")


if __name__ == "__main__":
    main()
