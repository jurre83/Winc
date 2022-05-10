__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


import os
import shutil
DIR = './cache'


def clean_cache():
    if os.path.isdir(DIR):
        shutil.rmtree(DIR)
        os.mkdir(DIR)
    else:
        os.mkdir(DIR)


def cache_zip(zip_file, cache_dir):
    shutil.unpack_archive(zip_file, cache_dir)


def cached_files():
    file_list_absolute = []
    for root, _, files in os.walk(DIR):
        for name in files:
            file = os.path.join(root, name)
            file_absolute = os.path.abspath(file)
            file_list_absolute.append(file_absolute)
    return file_list_absolute


def find_password(cached_files):
    for file in cached_files:
        with open(file) as f:
            for line in f:
                if "password" in line:
                    password_list = line.split()
                    return password_list[1]


def main():
    clean_cache()
    file_list = cached_files()
    find_password(file_list)


if __name__ == "__main__":
    main()
