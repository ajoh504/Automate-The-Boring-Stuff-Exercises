#! python3
# 06_fill_gaps.py -- search a single folder, find gaps in numbered files (spam001.txt, spam003.txt)
# and rename later files to fill in the gaps.
# INCOMPLETE -- see TODO

import re, os, shutil

def fill_gaps(folder: str, prefix: str) -> str:

    # Remove numbers from prefix using a regex
    remove_num_regex = re.compile('(\D*)')
    mo = remove_num_regex.search(prefix)
    if mo is None:
        return 'Invalid prefix. Prefix contains no letters.'
    elif os.path.isdir(folder) == False:
        return 'Invalid folder. Argument must be a valid folder path.'
    else:
        os.chdir(folder)
        # Add letter-only prefix to new regex
        letters_only = mo.group(1)
        # Search folder for letter prefix and add all matches to a list
        match_list = [i for i in os.listdir('.') if letters_only in i]
        
    # TODO: Rename later files to fill in gaps
    for index, file_name in enumerate(match_list):
        if str(index) not in ''.join(match_list):
            print(folder + '\\' + match_list[-1], folder + '\\' + match_list[index])
            #shutil.move(folder + '\\' + match_list[-1], folder + '\\' + match_list[index])

fill_gaps('C:\\Users\\Buzzkill\\test_source', 'spam000')
