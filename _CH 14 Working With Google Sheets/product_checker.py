#!python3
# sum_checker.py - Open the given spreadsheet, and check the product of the first two columns
#                  for any mistakes.


import ezsheets


def product_checker():
    ss = ezsheets.Spreadsheet("1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg")
    try:
        for row_num in range(1, len(ss[0].getRows())):
            if int(ss[0].getRow(row_num + 1)[0]) * int(
                ss[0].getRow(row_num + 1)[1]
            ) == int(ss[0].getRow(row_num + 1)[2]):
                continue
            elif not int(ss[0].getRow(row_num + 1)[0]) * int(
                ss[0].getRow(row_num + 1)[1]
            ) == int(ss[0].getRow(row_num + 1)[2]):
                print(
                    "Row number "
                    + str(row_num + 1)
                    + " returned an error. Check your math!"
                )
    except ValueError:
        pass


if __name__ == "__main__":
    product_checker()
