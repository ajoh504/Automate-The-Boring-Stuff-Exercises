#! python3
# 04_selective_copy.py -- Walk through a directory tree and copy all .bat or .cmd files to the specified destination. 

import os, shutil

def selective_copy(source_dir: str, destination_dir: str) -> str:
    # Walk through source_dir
    for folder_name, sub_folders, file_names in os.walk(source_dir):
        # Search for .bat or .cmd
        for file_name in file_names:
            if file_name[-4:] == '.bat' or file_name[-4:] == '.cmd':
                print(folder_name + '\\' + file_name)
                # Copy .bat or .cmd to destination_dir
                shutil.copy(folder_name + '\\' + file_name, destination_dir)
    return f'Batch files copied to {destination_dir}'
