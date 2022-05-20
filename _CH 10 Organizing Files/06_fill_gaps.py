#! python3
# 06_fill_gaps.py -- search a single folder, find gaps in numbered files (ex. spam001.txt, spam003.txt)
# and rename later files to fill in the gaps.
# INCOMPLETE

import re, os, shutil
from pathlib import Path

class rename_gapped_files:

    def __init__(
        self,
        directory: str,
        prefix: str,
        #regex_mo: re.Match,
        #file_list: list,
        #number_list: list,
        number_prefix_length: int,
        letters: str,
    ) -> None:
        self.directory = directory
        self.prefix = prefix
        #self.regex_mo = regex_mo
        #self.file_list = file_list
        #self.number_list = number_list
        self.number_prefix_length = number_prefix_length
        self.letters = letters

        
    def return_match_object(self) -> re.Match:
        # Remove numbers from prefix using a regex, then separate letters and numbers into groups
        return re.compile("(\D*)(\d*)").search(self.prefix)


    def check_user_input(self, regex_mo: re.Match) -> str | bool:
        if regex_mo is None:
            return "Invalid prefix. Prefix contains no letters or numbers."
        elif os.path.isdir(self.directory) == False:
            return "Invalid directory. Argument must be a valid directory path."
        else:
            return False


    def create_file_list(self, regex_mo: re.Match) -> list:
        # Search directory for letters and add matches to a list
        letters = regex_mo.group(1)
        file_list = [i for i in os.listdir(".") if letters in i]
        return file_list


    def create_number_list(self) -> list:
        # search match_list for numbers and add them to a list
        number_list = []
        for file_name in self.file_list:
            mo = return_match_object(file_name)
            number_list.append(int(mo.group(2)))
        return number_list


    def fill_gaps(self) -> list:
        # Rename later files to fill in gaps
        return_list = []
        for index, number in enumerate(self.number_list, 1):
            if index not in self.number_list:
                zeroes_to_add = "0" * (self.number_prefix_length - len(str(index)))
                suffix = Path(self.directory + "\\" + file_list[0]).suffix
                shutil.move(
                    self.directory + "\\" + self.file_list[-1],
                    self.directory + "\\" + self.letters + zeroes_to_add + str(index) + suffix,
                )
                return_list.append(
                    "renamed "
                    + self.file_list[-1]
                    + " to "
                    + self.letters
                    + zeroes_to_add
                    + str(index)
                    + suffix
                )

        return return_list


def main() -> None:
    while True:
        directory = input("Please enter a directory to search for files\n")
        prefix = input("Please enter a prefix to search for, such as spam000\n")
        rename = rename_gapped_files(directory, prefix)
        match_object = rename.return_match_object()
        letters = match_object.group(1)
        number_prefix_length = len(match_object.group(2))
        # check for valid user input
        if type(rename.check_user_input(rename.return_match_object())) == str:
            continue
        else:
            # main program execution
            os.chdir(directory)
            file_list = rename.create_file_list(rename.return_match_object())
            number_list = rename.create_number_list(
                rename.create_file_list(),
                rename.return_match_object()
            )
            print(
                rename.fill_gaps(
                    rename.create_file_list(),
                    rename.create_number_list(),
                    number_prefix_length,
                    letters
                )
            )
            break


if __name__ == "__main__":
    main()
