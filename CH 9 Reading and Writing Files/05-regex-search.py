#! python3
# 05-regex-search.py -- open all .txt files in a directory to search using a user supplied regex

import os, re
from pathlib import Path

# prompt user to change directories
print('This script allows you to input a regex to search all .txt files in a directory')
while True:
    dir = Path(input('Please enter a valid directory path:\n'))
    if dir.exists() and dir.is_dir():
        os.chdir(dir)
        break
    else:
        continue

# TODO: ask for user supplied regex

# TODO: search for .txt files in directory
