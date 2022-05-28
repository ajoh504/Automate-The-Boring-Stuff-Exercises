#! python3
# 06_fill_gaps.py -- search a single folder, find gaps in numbered files (ex. spam001.txt, spam003.txt)
# and rename later files to fill in the gaps.
#
# (From text) as an added challenge, insert gaps into numbered files so that
# new files can be added. See 'class insert_gaps' for solution
#
# usage -- user will be prompted for 1. filepath 2. file prefix, such as 'spam'
#          if user selects insert gaps, must supply start and end point for gaps


from pathlib import Path


class renameFiles:
    def __init__(self, directory: Path, prefix: str) -> None:
        self.directory = directory
        self.prefix = prefix
        self.number_prefix_length = len(  # will help determine leading zeroes for numbered files
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

    def zeroes_to_add(self, number) -> str:  # return leading zeroes for file name, such as 'spam004'
        return "0" * (self.number_prefix_length - len(str(number)))

    def return_suffix(self) -> str:  # suffix example: '.txt' or '.pdf'
        return Path(str(self.directory) + "/" + self.return_file_list()[0]).suffix

    def return_gap_list(self) -> list:  # return numbered gaps in filenames
        number_list = self.return_number_list()
        gap_list = []
        for gap in range(len(number_list)):
            if gap not in number_list:
                gap_list.append(gap)
        return gap_list

    def fill_gaps(self):  # fill any numbered gaps matching the user supplied prefix
        gap_list = self.return_gap_list()
        for gap in gap_list:
            Path.rename(
                Path(self.return_file_list()[-1]),
                Path(
                    str(self.directory)
                    + "/"
                    + self.prefix
                    + self.zeroes_to_add(gap)
                    + str(gap) 
                    + self.return_suffix()
                )
            )

    # insert gaps into numbered files
    def insert_gaps(self, gap_range_start: int, gap_range_end: int):
        for number in range(gap_range_start, gap_range_end):
            number_list = self.return_number_list()
            new_number = len(number_list)  # new number == end of number_list
            Path.rename(
                Path(
                    str(self.directory)
                    + "/"
                    + self.prefix
                    + str(self.zeroes_to_add(number))
                    + str(number)
                    + self.return_suffix(),
                ),
                Path(
                    str(self.directory)
                    + "/"
                    + self.prefix
                    + str(self.zeroes_to_add(new_number))
                    + str(new_number)
                    + self.return_suffix(),
                )
            )


def main() -> None:
    directory = Path(input("Please enter a directory to search for files\n"))
    prefix = input("Please enter a prefix to search for, such as spam\n")
    while True:
        choice = input("Type '1' to rename files, or '2' to to insert gaps\n")
        rename = renameFiles(directory, prefix)
        match choice:
            case '1':
                rename.fill_gaps()
                break
            case '2':
                rename.insert_gaps(
                    int(input('Insert starting gap range:\n')),
                    int(input('Insert ending gap range:\n'))
                )
                break


if __name__ == "__main__":
    main()
