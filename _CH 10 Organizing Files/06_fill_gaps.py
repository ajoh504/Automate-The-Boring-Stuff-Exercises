#! python3
# 06_fill_gaps.py -- search a single folder, find gaps in numbered files (ex. spam001.txt, spam003.txt)
# and rename later files to fill in the gaps.
#
# (From the book) as an added challenge, insert gaps into numbered files so that
# new files can be added. See 'class insert_gaps' for solution
#
# INCOMPLETE -- see all TODO:

import shutil, random
from pathlib import Path

# TODO: remove unnecessary variables -- invoke functions directly instead of in variables?
class rename_gapped_files:
    def __init__(self, directory: str, prefix: str) -> None:
        self.directory = directory
        self.prefix = prefix
        self.file_list = self.create_file_list()
        self.number_list = self.create_number_list()
        self.number_prefix_length = len(Path(self.file_list[0]).stem.strip(self.prefix))

    # TODO: rewrite as generator function
    def create_file_list(self) -> list:
        return [str(file) for file in self.directory.glob(f"{self.prefix}*")]

    def create_number_list(self) -> list:
        # find numbers in matched file names and store numbers in list
        number_list = []
        for file_name in self.file_list:
            number_list.append(int(str(Path(file_name).stem).strip(self.prefix)))
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
                    str(self.file_list[-1]),
                    str(self.directory)
                    + "\\"
                    + self.prefix
                    + zeroes_to_add
                    + str(index)
                    + suffix,
                )
                return_list.append(
                    "renamed "
                    + self.file_list[-1]
                    + " to "
                    + self.prefix
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
    directory = Path(input("Please enter a directory to search for files\n"))
    prefix = input("Please enter a prefix to search for, such as spam\n")
    rename = rename_gapped_files(directory, prefix)
    #insert = insert_gaps(directory, prefix, rename)
    print(rename.fill_gaps())
    #insert.insert_gaps()



if __name__ == "__main__":
    main()
