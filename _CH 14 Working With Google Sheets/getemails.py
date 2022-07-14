#!python3
# getemails.py -- get a list of emails from a Google Sheet that was converted
#                 from a Google Form. Function receives one param: a string
#                 containing a link to the Google Sheet (or the sheet id number)

import ezsheets
import re

def get_emails(google_sheet: str) -> list:
    ss = ezsheets.Spreadsheet(google_sheet)
    sheet = ss[0]
    return [email for email in sheet.getColumn(2) if re.compile(r"(?=.*@)").search(email)]
