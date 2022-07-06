#!python3
# multiplication_table.py -- take a number N from the command line and create a
# multiplication table in Excel with the contents N x N. Make the first row and
# column bold. sys.argv[1] = N

import sys
import openpyxl
from openpyxl.styles import Font

def create_multiplication_table():
    wb = openpyxl.Workbook() # create Workbook object
    sheet = wb.active # create Workbook sheet object
    bold = Font(bold=True)

    #todo: loop through rows and columns, and append N to cells
    for row_num in range(1, int(sys.argv[1])):
        for column_num in range(0, int(sys.argv[1])):
            print(sheet[row_num][column_num])

if __name__ == '__main__':
    create_multiplication_table()
