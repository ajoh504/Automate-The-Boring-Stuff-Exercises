#!python3
# multiplication_table.py -- take a number (num) from the command line and create a
# multiplication table in Excel with the contents num x num. Make the first row and
# column bold.

import sys
import openpyxl
from openpyxl.styles import Font

def create_multiplication_table():
    num = int(sys.argv[1])
    wb = openpyxl.Workbook() # create Workbook object
    sheet = wb.active # create Workbook sheet object
    bold = Font(bold=True)

    #todo: loop through rows and columns, and append N to cells
    for row_num in range(2, num + 2):
        sheet.cell(row=row_num, column=1).value = row_num - 1
    wb.save('mult_table_' + str(num) + 'x' + str(num) + '.xlsx')

if __name__ == '__main__':
    create_multiplication_table()
