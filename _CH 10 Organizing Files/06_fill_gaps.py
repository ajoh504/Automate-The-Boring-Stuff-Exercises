#! python3
# 06_fill_gaps.py -- search a single folder, find gaps in numbered files (ex. spam001.txt, spam003.txt)
# and rename later files to fill in the gaps.
#
# (From the book) as an added challenge, insert gaps into numbered files so that
# new files can be added. See 'class insert_gaps' for solution
#
# INCOMPLETE -- see all TODO:

import re, os, shutil, random
from pathlib import Path

# TODO: remove unnecessary variables -- invoke functions directly instead of in variables?
class rename_gapped_files:
    def __init__(self, directory: str, prefix: str) -> None:
        self.directory = directory
        # TODO: rewrite to accept prefix as 'spam' instead of 'spam000'
        self.prefix = prefix
        self.file_list = self.create_file_list(self.return_match_object(self.prefix))
        self.number_list = self.create_number_list()
        self.number_prefix_length = len(self.return_match_object(self.prefix).group(2))
        self.letters = self.return_match_object(self.prefix).group(1)

    # TODO: rewrite code to use glob instead of regex
    def return_match_object(self, prefix) -> re.Match:
        return re.compile("(\D*)(\d*)").search(prefix)
    # TODO: rewrite to include exceptions
    def check_user_input(self, regex_mo: re.Match) -> str | bool:
        if regex_mo is None:
            return "Invalid prefix. Prefix contains no letters or numbers."
        elif os.path.isdir(self.directory) == False:
            return "Invalid directory. Argument must be a valid directory path."
        else:
            return False
    # TODO: rewrite to use glob instead of os.listdir
    # TODO: rewrite as generator function
    def create_file_list(self, regex_mo: re.Match) -> list:
        # search current working directory for file names that match regex
        letters = regex_mo.group(1)
        #test_list = [str(file) for file in self.directory.glob(f"{letters}*")]
        #print(test_list, self.directory, self.prefix)
        return [i for i in os.listdir(".") if letters in i]
        #return [str(file) for file in self.directory.glob(f"{letters}*")]
    # TODO: make functional without mo (match_object)
    def create_number_list(self) -> list:
        # find numbers in matched file names and store numbers in list
        # number_list will be used to find numbered gaps
        number_list = []
        for file_name in self.file_list:
            mo = self.return_match_object(file_name)
            number_list.append(int(mo.group(2)))
        return number_list
    # TODO: separate gap renaming code from gap identification code
    def fill_gaps(self) -> list:
        # Rename later files to fill in gaps
        return_list = []
        for index, number in enumerate(self.number_list, 1):
            if index not in self.number_list:
                zeroes_to_add = "0" * (self.number_prefix_length - len(str(index)))
                suffix = Path(str(self.directory) + "\\" + self.file_list[0]).suffix
                # TODO: rewrite using Path instead of shutil
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
# TODO: write added challenge (insert gaps)
'''
class insert_gaps:
    def __init__(self, directory, prefix, rename_gap_class):
        self.directory = directory
        self.prefix = prefix
        self.file_list = rename_gap_class.create_file_list(rename_gap_class.return_match_object(self.prefix))
        self.letters = rename_gap_class.letters
        self.number_prefix_length = rename_gap_class.number_prefix_length
        self.number_list = rename_gap_class.number_list

    def insert_gaps(self):
        gaps_to_insert = random.randint(1, len(self.number_list))
        for number in range(gaps_to_insert):
            zeroes_to_add = "0" * (self.number_prefix_length - len(str(number)))
            number_to_change = random.choice(self.number_list)
            new_number = number_to_change + len(self.number_list)
            new_number_zeroes = "0" * (self.number_prefix_length - len(str(new_number)))
            suffix = Path(str(self.directory) + "\\" + self.file_list[0]).suffix
            changed_number_list = []
            if number_to_change not in changed_number_list:
                print(
                    str(self.directory) + '\\' + self.letters + str(zeroes_to_add) + str(number_to_change) + suffix,
                    str(self.directory) + '\\' + self.letters + str(new_number_zeroes) + str(new_number) + suffix
                )

                shutil.move(
                    str(self.directory) + '\\' + self.letters + str(zeroes_to_add) + str(number_to_change) + suffix,
                    str(self.directory) + '\\' + self.letters + str(new_number_zeroes) + str(new_number) + suffix
                )
                changed_number_list.append(number_to_change)
'''
'''                
            for file in self.directory.glob('*'):
                if self.letters in str(file):
                    shutil.move(
                        self.directory + '\\' +
                    )'''


def main() -> None:
    while True:
        directory = Path(input("Please enter a directory to search for files\n"))
        prefix = (input("Please enter a prefix to search for, such as spam000\n"))
        os.chdir(directory)
        rename = rename_gapped_files(directory, prefix)
        #insert = insert_gaps(directory, prefix, rename)
        match_object = rename.return_match_object(prefix)

        if type(rename.check_user_input(match_object)) == str:
            continue
        else:

            print(rename.fill_gaps())
            #insert.insert_gaps()
            break


if __name__ == "__main__":
    main()
