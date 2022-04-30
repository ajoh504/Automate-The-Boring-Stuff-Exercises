#! python3
# 05_deleting_unneeded_files.py -- walk through a directory tree, search for all files larger than 100MB
# print the absolute path to the screen

import os

def find_large_files(source_dir: str) -> None:
    for folder_name, sub_folders, file_names in os.walk(source_dir):
        for file_name in file_names:
            abs_path = folder_name + '\\' + file_name
            if os.path.getsize(abs_path) > 100000000:
                print(abs_path)

find_large_files('C:\\test_source')
            
        

