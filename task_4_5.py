import os
import django
import json

main_dir = django.__path__[0]
res_django_files = {}
for root_dir, sub_dirs, files in os.walk(main_dir):
    for s_file in files:
        f_size = 10 ** len(str(os.stat(os.path.join(root_dir, s_file)).st_size))
        file_ext = s_file.rsplit(".", maxsplit=1)[-1].lower()
        if f_size in res_django_files:
            res_django_files[f_size][0] += 1
            if file_ext not in res_django_files[f_size][1]:
                res_django_files[f_size][1].append(file_ext)
        else:
            res_django_files[f_size] = [1, [file_ext]]

res = {}
for size, nums in sorted(res_django_files.items()):
    res[size] = tuple(nums)
    print(size, tuple(nums))

dir_name = os.path.relpath(__file__).split("\\")[-1] + "_summary.json"
with open(dir_name, "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False, indent=4)
