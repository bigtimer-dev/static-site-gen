import shutil
import os


def empty_directory(path):
    if not os.path.exists(path):
        return "Directory not found"
    else:
        items_inside = os.listdir(path)
        for item in items_inside:
            full_path_to_item = os.path.join(path, item)
            if os.path.isfile(full_path_to_item):
                os.remove(full_path_to_item)
                print(f"Removing file: {full_path_to_item}")
            else:
                shutil.rmtree(full_path_to_item)
                print(f"Removing directory: {full_path_to_item}")
