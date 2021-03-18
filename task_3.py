import shutil
import os

root_dir = 'my_project'
find_dir = 'templates'
for main_dir, dirs, files in os.walk(root_dir):
    if main_dir.find(find_dir) > 0 and len(files) == 0:
        shutil.copytree(os.path.join(main_dir), find_dir, dirs_exist_ok=True)
