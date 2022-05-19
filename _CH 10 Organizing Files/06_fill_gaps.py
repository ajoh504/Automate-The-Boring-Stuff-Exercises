#! python3
# 06_fill_gaps.py -- search a single folder, find gaps in numbered files (ex. spam001.txt, spam003.txt)
# and rename later files to fill in the gaps.

import re, os, shutil
from pathlib import Path

class rename_gap_files:

    def __init__(self, directory, prefix) -> None:
        self.directory = directory
        self.prefix = prefix

        
    def return_match_object(prefix: str) -> re.Match:
        # Remove numbers from prefix using a regex, then separate letters and numbers into groups
        return re.compile("(\D*)(\d*)").search(prefix)


    def check_user_input(directory: str, regex_mo: re.Match) -> str | bool:
        if regex_mo is None:
            return "Invalid prefix. Prefix contains no letters or numbers."
        elif os.path.isdir(directory) == False:
            return "Invalid directory. Argument must be a valid directory path."
        else:
            return False


    def create_file_list(regex_mo: re.Match) -> list:
        # Search directory for letters and add matches to a list
        letters = regex_mo.group(1)
        file_list = [i for i in os.listdir(".") if letters in i]
        return file_list


    def create_number_list(file_list: list, regex_mo: re.Match) -> list:
        # search match_list for numbers and add them to a list
        number_list = []
        for file_name in file_list:
            mo = return_match_object(file_name)
            number_list.append(int(mo.group(2)))
        return number_list


    def fill_gaps(
        file_list: list,
        number_list: list,
        directory: str,
        number_prefix_length: int,
        letters: str,
    ) -> list:
        # Rename later files to fill in gaps
        return_list = []
        for index, number in enumerate(number_list, 1):
            if index not in number_list:
                zeroes_to_add = "0" * (number_prefix_length - len(str(index)))
                suffix = Path(directory + "\\" + file_list[0]).suffix
                shutil.move(
                    directory + "\\" + file_list[-1],
                    directory + "\\" + letters + zeroes_to_add + str(index) + suffix,
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


def main() -> None:
    while True:
        directory = input("Please enter a directory to search for files\n")
        prefix = input("Please enter a prefix to search for, such as spam000\n")
        fill_gaps = rename_gap_files(directory, prefix)
        match_object = fill_gaps.return_match_object(prefix)
        letters = match_object.group(1)
        number_prefix_length = len(match_object.group(2))
        # check for valid user input
        if type(fill_gaps.check_user_input(directory, match_object)) == str:
            continue
        else:
            # main program execution
            os.chdir(directory)
            file_list = fill_gaps.create_file_list(match_object)
            number_list = fill_gaps.create_number_list(file_list, match_object)
            print(
                fill_gaps.fill_gaps(file_list, number_list, directory, number_prefix_length, letters)
            )
            break


if __name__ == "__main__":
    main()
