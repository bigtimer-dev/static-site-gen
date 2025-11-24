import os
import shutil


def recursive_copy(src, dest):
    if os.path.exists(src):
        items_in_source = os.listdir(src)
        for item in items_in_source:
            full_path_item_src = os.path.join(src, item)
            full_path_item_dest = os.path.join(dest, item)
            if os.path.isfile(full_path_item_src):
                shutil.copy(full_path_item_src, full_path_item_dest)
                print("Copying:", full_path_item_src, "to", full_path_item_dest)
            else:
                if not os.path.exists(full_path_item_dest):
                    os.mkdir(full_path_item_dest)
                recursive_copy(full_path_item_src, full_path_item_dest)
    else:
        return "Error: path does not exists"
