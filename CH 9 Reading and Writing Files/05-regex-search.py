#! python3
# 05-regex-search.py -- open all .txt files in a directory to search using a user supplied regex

import os, re
from pathlib import Path

def main() -> None:
    # prompt user to change directories
    print('This script allows you to input a regex to search all .txt files in a directory')
    while True:
        dir = Path(input('Please enter a valid directory path:\n'))
        if dir.is_dir():
            os.chdir(dir)
            break
        else:
            continue

    # ask user for regex and search for .txt files in directory
    user_regex = input('Please enter a regex to search all .txt files:\n')
    regex = re.compile(user_regex)
    cwd = Path.cwd()
    for windows_path in os.listdir(cwd):
        if windows_path[-4:] == '.txt':
            file_object = open(windows_path, encoding='utf8')
            read_file = file_object.read()
            print(regex.findall(read_file))
            file_object.close()

if __name__ == '__main__':
    main()
