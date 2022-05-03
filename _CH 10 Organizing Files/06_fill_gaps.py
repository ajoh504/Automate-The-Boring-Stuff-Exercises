#! python3
# 06_fill_gaps.py -- search a single folder, find gaps in numbered files (spam001.txt, spam003.txt)
# and rename later files to fill in the gaps.
# INCOMPLETE -- see TODO

import re, os, shutil

def fill_gaps(folder: str, prefix: str) -> str:
    # Remove numbers from prefix using a regex, then separate letters and numbers into groups
    regex = re.compile('(\D*)(\d*)') 
    mo = regex.search(prefix)
    if mo is None:
        return 'Invalid prefix. Prefix contains no letters or numbers.'
    elif os.path.isdir(folder) == False:
        return 'Invalid folder. Argument must be a valid folder path.'
    else:
        # main program execution
        os.chdir(folder)
        letters = mo.group(1)
        
        # Search folder for letters and add matches to a list
        file_list = [i for i in os.listdir('.') if letters in i]
        
        # search match_list for numbers and add them to a list
        numbers_list = []
        for file_name in match_list:
            mo = regex.search(file_name)
            numbers_list.append(int(mo.group(2)))

        # loop through file_list to search for missings numbers
        for index, file_name in enumerate(file_list, 1):
            if str(index) not in ''.join(str(numbers_list)):
                print(index)
                #print(index, file_list[-1], file_list[index], match_list)
                print(folder + '\\' + file_list[-1], folder + '\\' + file_list[index])
                
                # TODO: Rename later files to fill in gaps
                #shutil.move(folder + '\\' + file_list[-1], folder + '\\' + file_list[index])

fill_gaps('C:\\test_source', 'spam000')
