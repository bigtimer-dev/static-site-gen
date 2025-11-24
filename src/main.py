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


if __name__ == "__main__":
    sync_folders()
