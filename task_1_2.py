import os
import yaml


def create_path(values, prefix=""):
    for folder, paths in values.items():
        folder_path = os.path.join(prefix, folder)
        os.makedirs(folder_path, exist_ok=True)
        if isinstance(paths, dict):
            create_path(paths, folder_path)
        else:
            for sub_elem in paths:
                if isinstance(sub_elem, dict):
                    create_path(sub_elem, folder_path)
                else:
                    n_file = open(os.path.join(folder_path, sub_elem), "w")
                    n_file.close()


with open("config.yaml", "r", encoding="utf-8") as f_conf:
    temp_config = yaml.safe_load(f_conf)
    create_path(temp_config)