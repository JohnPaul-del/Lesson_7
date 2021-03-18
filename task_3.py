import shutil
import os

for main_dir, dirs, files in os.walk("my_project"):
    for s_file in files:
        if s_file.endswith(".html"):
            print(os.path.abspath(s_file))
#          shutil.copytree(main_dir, os.path.join(os.path.dirname(main_dir), r"templates"))
