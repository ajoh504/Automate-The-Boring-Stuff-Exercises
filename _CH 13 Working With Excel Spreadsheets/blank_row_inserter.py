#!python3
# blank_row_inserter.py - take two numbers and an Excel filename as command line
# arguments. The first number denotes a row number. The second number denotes
# how many blank rows to place starting at the given row number.

import sys
import openpyxl
from openpyxl.utils import get_column_letter, column_index_from_string

def blank_row_inserter(blank_row_starting_point: int, blank_row_quantity: int, excel_file: str) -> None:
    wb = openpyxl.load_workbook(excel_file)
    sheet = wb.active
    new_cells = {}

    # todo: store contents to copy into dict
    for row_num in range(1, sheet.max_row):
        for column_num in range(1, sheet.max_column):
            pass
            # if row_num == blank_row_starting_point:
            #     new_cells[get_column_letter(column_num) + str(row_num)] = sheet.cell(row=row_num, column=column_num)

    # todo: overwrite cells using dictionary contents
    wb.save(excel_file[0:-5] + 'RowsInserted' + '.xlsx') # save as new file

if __name__ == "__main__":
    blank_row_inserter(sys.argv[1], sys.argv[2], sys.argv[3])
