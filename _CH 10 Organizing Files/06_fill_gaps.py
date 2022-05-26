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


class rename_gapped_files:
    def __init__(self, directory: str, prefix: str) -> None:
        self.directory = directory
        self.prefix = prefix
        self.number_prefix_length = len(
            Path(self.create_file_list()[0]).stem.strip(self.prefix)
        )

    # TODO: rewrite as generator function
    def create_file_list(self) -> list:
        return [str(file) for file in self.directory.glob(f"{self.prefix}*")]

    def create_number_list(self) -> list:
        # find numbers in matched file names and store numbers in list
        number_list = []
        for file_name in self.create_file_list():
            number_list.append(int(str(Path(file_name).stem).strip(self.prefix)))
        return number_list

    def zeroes_to_add(self, number):
        return "0" * (self.number_prefix_length - len(str(number)))

    def return_suffix(self):
        return Path(str(self.directory) + "\\" + self.create_file_list()[0]).suffix

    # TODO: separate gap renaming code from gap identification code
    def fill_gaps(self) -> None:
        # Rename later files to fill in gaps
        for index, number in enumerate(self.create_number_list(), 1):
            if index not in self.create_number_list():
                # TODO: rewrite using Path instead of shutil
                shutil.move(
                    str(self.create_file_list()[-1]),
                    str(self.directory)
                    + "\\"
                    + self.prefix
                    + self.zeroes_to_add(index)
                    + str(index)
                    + self.return_suffix(),
                )

    # TODO: write added challenge (insert gaps)
    def insert_gaps(self):
        gaps_to_insert = random.randint(1, len(self.create_number_list()))
        for number in range(gaps_to_insert):
            number_to_change = random.choice(self.create_number_list())
            new_number = number_to_change + len(self.create_number_list())
            changed_number_list = []
            if number_to_change not in changed_number_list:
                print(
                    str(self.directory)
                    + "\\"
                    + self.prefix
                    + str(self.zeroes_to_add(number))
                    + str(number_to_change)
                    + self.return_suffix(),
                    str(self.directory)
                    + "\\"
                    + self.prefix
                    + str(self.zeroes_to_add(new_number))
                    + str(new_number)
                    + self.return_suffix(),
                )

                shutil.move(
                    str(self.directory)
                    + "\\"
                    + self.prefix
                    + str(self.zeroes_to_add(number))
                    + str(number_to_change)
                    + self.return_suffix(),
                    str(self.directory)
                    + "\\"
                    + self.prefix
                    + str(self.zeroes_to_add(new_number))
                    + str(new_number)
                    + self.return_suffix(),
                )
                changed_number_list.append(number_to_change)



def main() -> None:
    while True:
        directory = Path(r'C:\Users\Buzzkill\test_source')# Path(input("Please enter a directory to search for files\n"))
        prefix = 'spam' # input("Please enter a prefix to search for, such as spam\n")
        choice = input("Type '1' to rename gapped files, or '2' to to insert gaps")
        rename = rename_gapped_files(directory, prefix)
        match choice:
            case '1':
                rename.fill_gaps()
                break
            case '2':
                rename.insert_gaps()
                break



if __name__ == "__main__":
    main()
