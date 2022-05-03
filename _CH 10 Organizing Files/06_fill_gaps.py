#! python3
# 06_fill_gaps.py -- search a single folder, find gaps in numbered files (spam001.txt, spam003.txt)
# and rename later files to fill in the gaps.

import re, os, shutil
from pathlib import Path


def fill_gaps(folder: str, prefix: str) -> list | str:
    # Remove numbers from prefix using a regex, then separate letters and numbers into groups
    regex = re.compile("(\D*)(\d*)")
    mo = regex.search(prefix)
    if mo is None:
        return "Invalid prefix. Prefix contains no letters or numbers."
    elif os.path.isdir(folder) == False:
        return "Invalid folder. Argument must be a valid folder path."
    else:
        # main program execution
        os.chdir(folder)
        letters = mo.group(1)
        # Search folder for letters and add matches to a list
        file_list = [i for i in os.listdir(".") if letters in i]

        # search match_list for numbers and add them to a list
        numbers_list = []
        for file_name in file_list:
            mo = regex.search(file_name)
            numbers_list.append(int(mo.group(2)))
            number_prefix_length = len(mo.group(2))

        # loop through file_list to search for missings numbers
        # Rename later files to fill in gaps
        return_list = []
        for index, number in enumerate(numbers_list, 1):
            if index not in numbers_list:
                zeroes_to_add = "0" * (number_prefix_length - len(str(index)))
                suffix = Path(folder + "\\" + file_list[0]).suffix
                shutil.move(
                    folder + "\\" + file_list[-1],
                    folder + "\\" + letters + zeroes_to_add + str(index) + suffix,
                )
                return_list.append(
                    "renamed "
                    + file_list[-1]
                    + " to "
                    + letters
                    + zeroes_to_add
                    + str(index)
                    + suffix
                )

        return return_list


if __name__ == "__main__":
    print(
        "This program finds numbered text files, such as spam001 and spam003, \nand renames later files to fill in the numbered gaps"
    )
    print(
        fill_gaps(
            input("Please enter a folder to search for files\n"),
            input("Please enter a prefix to search for, such as spam000\n"),
        )
    )
