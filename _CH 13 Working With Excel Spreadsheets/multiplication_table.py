#!python3
# multiplication_table.py -- take a number N from the command line and create a
# multiplication table in Excel with the contents N x N. Make the first row and
# column bold. sys.argv[1] = N

import openpyxl
import sys

def create_multiplication_table():
    wb = openpyxl.Workbook() # create Workbook object
    sheet = wb.active # create Workbook sheet object
    # todo: create bold font type

    #todo: loop through rows and columns, and append N to cells
    for i in range(1, sys.argv[1]):
        print(sheet[i])

if __name__ == '__main__':
    create_multiplication_table()
