__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


import os
import shutil


def clean_cache():
    if os.path.isdir('./files/cache'):
        shutil.rmtree('./files/cache')
        os.mkdir('./files/cache')
    else:
        os.mkdir('./files/cache')


def cache_zip(zip_file, cache_dir):
    if os.path.isdir('./files/cache'):
        shutil.rmtree('./files/cache')
        os.mkdir('./files/cache')
    else:
        os.mkdir('./files/cache')
    shutil.unpack_archive(zip_file, cache_dir)


def cached_files():
    file_list = []
    file_list_absolute = []
    for root, _, files in os.walk('./files/cache'):
        for name in files:
            file_list.append(os.path.join(root, name))
    lenght = len(file_list)
    for i in range(lenght):
        file_list_absolute.append(os.path.abspath(file_list[i]))
    return file_list_absolute


def find_password(cached_files):
    for file in cached_files:
        with open(file) as f:
            for line in f:
                if "password" in line:
                    split_line = line.split()
                    return split_line[1]


file_list = cached_files()
find_password(file_list)
