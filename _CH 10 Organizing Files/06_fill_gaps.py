#! python3
# 06_fill_gaps.py -- search a single folder, find gaps in numbered files (ex. spam001.txt, spam003.txt)
# and rename later files to fill in the gaps.
#
# (From the book) as an added challenge, insert gaps into numbered files so that
# new files can be added. See 'class insert_gaps' for solution
#
# INCOMPLETE -- see all TODO:


import random
from pathlib import Path


class renameFiles:
    def __init__(self, directory: Path, prefix: str) -> None:
        self.directory = directory
        self.prefix = prefix
        self.number_prefix_length = len(
            Path(self.return_file_list()[0]).stem.strip(self.prefix)
        )

    def return_file_list(self) -> list:
        return [str(file) for file in self.directory.glob(f"{self.prefix}*")]

    def return_number_list(self) -> list:
        # find numbers in matched file names and store numbers in list
        file_list = self.return_file_list()
        number_list = []
        for file_name in file_list:
            number_list.append(int(str(Path(file_name).stem).strip(self.prefix)))
        return number_list

    def zeroes_to_add(self, number) -> str:
        return "0" * (self.number_prefix_length - len(str(number)))

    def return_suffix(self) -> str:
        return Path(str(self.directory) + "\\" + self.return_file_list()[0]).suffix

    def return_gap_list(self) -> list:
        number_list = self.return_number_list()
        gap_list = []
        for gap in range(len(number_list)):
            if gap not in number_list:
                gap_list.append(gap)
        return gap_list

    def fill_gaps(self):
        gap_list = self.return_gap_list()
        for gap in gap_list:
            Path.rename(
                Path(self.return_file_list()[-1]),
                Path(
                    str(self.directory)
                    + "\\"
                    + self.prefix
                    + self.zeroes_to_add(gap)
                    + str(gap) + self.return_suffix()
                )
            )

# TODO: write added challenge (insert gaps)
#     def insert_gaps(self):
#         gaps_to_insert = random.randint(1, len(self.return_number_list()))
#         for number in range(gaps_to_insert):
#             number_to_change = random.choice(self.return_number_list())
#             new_number = number_to_change + len(self.return_number_list())
#             changed_number_list = []
#             if number_to_change not in changed_number_list:
#                 shutil.move(
#                     str(self.directory)
#                     + "\\"
#                     + self.prefix
#                     + str(self.zeroes_to_add(number))
#                     + str(number_to_change)
#                     + self.return_suffix,
#                     str(self.directory)
#                     + "\\"
#                     + self.prefix
#                     + str(self.zeroes_to_add(new_number))
#                     + str(new_number)
#                     + self.return_suffix,
#                 )
#                 changed_number_list.append(number_to_change)


def main() -> None:
    directory = Path(input("Please enter a directory to search for files\n"))
    prefix = input("Please enter a prefix to search for, such as spam\n")
    while True:
        choice = input("Type '1' to rename files, or '2' to to insert gaps")
        rename = renameFiles(directory, prefix)
        match choice:
            case '1':
                rename.fill_gaps()
                break
            case '2':
                #rename.insert_gaps()
                break


if __name__ == "__main__":
    main()
