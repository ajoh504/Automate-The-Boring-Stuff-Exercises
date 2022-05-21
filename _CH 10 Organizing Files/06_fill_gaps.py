#! python3
# 06_fill_gaps.py -- search a single folder, find gaps in numbered files (ex. spam001.txt, spam003.txt)
# and rename later files to fill in the gaps.

import re, os, shutil
from pathlib import Path


class rename_gapped_files:
    def __init__(self, directory: str, prefix: str) -> None:
        self.directory = directory
        self.prefix = prefix
        self.file_list = self.create_file_list(self.return_match_object(self.prefix))
        self.number_list = self.create_number_list()
        self.number_prefix_length = len(self.return_match_object(self.prefix).group(2))
        self.letters = self.return_match_object(self.prefix).group(1)

    def return_match_object(self, prefix) -> re.Match:
        return re.compile("(\D*)(\d*)").search(prefix)

    def check_user_input(self, regex_mo: re.Match) -> str | bool:
        if regex_mo is None:
            return "Invalid prefix. Prefix contains no letters or numbers."
        elif os.path.isdir(self.directory) == False:
            return "Invalid directory. Argument must be a valid directory path."
        else:
            return False

    def create_file_list(self, regex_mo: re.Match) -> list:
        # search current working directory for file names that match regex
        letters = regex_mo.group(1)
        file_list = [i for i in os.listdir(".") if letters in i]
        return file_list

    def create_number_list(self) -> list:
        # find numbers in matched file names and store numbers in list
        # number_list will be used to find numbered gaps
        number_list = []
        for file_name in self.file_list:
            mo = self.return_match_object(file_name)
            number_list.append(int(mo.group(2)))
        return number_list

    def fill_gaps(self) -> list:
        # Rename later files to fill in gaps
        return_list = []
        for index, number in enumerate(self.number_list, 1):
            if index not in self.number_list:
                zeroes_to_add = "0" * (self.number_prefix_length - len(str(index)))
                suffix = Path(str(self.directory) + "\\" + self.file_list[0]).suffix
                shutil.move(
                    str(self.directory) + "\\" + self.file_list[-1],
                    str(self.directory)
                    + "\\"
                    + self.letters
                    + zeroes_to_add
                    + str(index)
                    + suffix,
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
        directory = Path(input("Please enter a directory to search for files\n"))
        prefix = (input("Please enter a prefix to search for, such as spam000\n"))
        os.chdir(directory)
        rename = rename_gapped_files(directory, prefix)
        match_object = rename.return_match_object(prefix)

        if type(rename.check_user_input(match_object)) == str:
            continue
        else:
            print(rename.fill_gaps())
            break


if __name__ == "__main__":
    main()
