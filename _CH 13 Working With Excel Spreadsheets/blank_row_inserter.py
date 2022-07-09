#!python3
# blank_row_inserter.py - take two numbers and an Excel filename as command line
#                         arguments. The first number denotes a row number. The second
#                         number denotes how many blank rows to place starting at the
#                         given row number.

import sys
import openpyxl
from openpyxl.utils import get_column_letter, column_index_from_string


def blank_row_inserter(start: int, qty: int, excel_file: str) -> None:
    """
    :param start: blank row starting point (sys.argv[1])
    :param qty: quantity of blank rows to add (sys.argv[2])

    Use nested loops to append Excel cell coordinates to dictionary keys. Use the same coordinates
    to append the cell values to the dictionary values. If the iterator == the blank row starting
    point (or) if the iterator < (blank row starting point + blank row qty), then add None as
    values to create blank lines. Loop continues after blank lines, and appends all the rest of the
    Excel values.
    """
    wb = openpyxl.load_workbook(excel_file)
    sheet = wb.active
    new_cells = {}
    for row in range(
        1, sheet.max_row + qty + 1
    ):  # add 1 to account for non-zero starting index
        for column in range(1, sheet.max_column + 1):
            if row < start:
                new_cells[get_column_letter(column) + str(row)] = sheet[
                    get_column_letter(column) + str(row)
                ].value
            elif row == start or row < (start + qty):
                new_cells[get_column_letter(column) + str(row)] = None
            elif row >= start + qty:
                new_cells[get_column_letter(column) + str(row)] = sheet[
                    get_column_letter(column) + str(row - qty)
                ].value

    # append dictionary values to Excel cells, then save the new file
    for row in range(1, sheet.max_row + qty + 1):
        for column in range(1, sheet.max_column + 1):
            sheet[get_column_letter(column) + str(row)].value = new_cells[
                get_column_letter(column) + str(row)
            ]

    wb.save(excel_file[0:-5] + "_edited" + ".xlsx")


if __name__ == "__main__":
    blank_row_inserter(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3])
