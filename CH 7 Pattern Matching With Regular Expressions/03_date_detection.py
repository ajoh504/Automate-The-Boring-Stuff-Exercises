
# date regex: dd/mm/yyyy

import re

def regex_date_validator(date: str) -> bool:
    valid = True # final return value, change to False if date not valid
    is_leap_year = False # If leap year, change to True
    date_regex = re.compile(r'''
    (\d{2})     # day
    (/)         # separator
    (\d{2})     # month
    (/)         # separator 
    (\d{4})     # year
    ''', re.VERBOSE)
    regex_groups = date_regex.findall(date) # store regex groups

    # convert regex groups to int, store in variables
    day = int(regex_groups[0][0])
    month = int(regex_groups[0][2])
    year = int(regex_groups[0][4])

    # check month and date
    if month > 12 or day > 31:
        valid = False
        print('Error: invalid month/date range.')

    # check 30-day months: April, June, September, November
    if month in (4, 6, 9, 11) and day > 30:
        valid = False
        print('Error: invalid date. Apr, Jun, Sept, and Nov have 30 days.')

    # check leap-year. Must be divisible by 4. If leap year is
    # divisible by 100, must also be divisible by 400
    if year % 4 == 0:
        is_leap_year = True
        if year % 100 == 0 and year % 400 == 0:
            is_leap_year = True
        elif year % 100 == 0 and year % 400 != 0: # if divisible by 100 but not 400, is_leap_year == False
            is_leap_year = False

    # check February and compare to leap year
    if month == 2 and is_leap_year == True:
        if day > 29:
            valid = False
            print('Error: invalid date. Feb has 29 days during leap years.')

    # Check February and compare to non-leap year
    if month == 2 and is_leap_year == False:
        if day > 28:
            valid = False
            print('Error: invalid date. Feb has 28 days.')
    
    # if all previous conditionals are False, then Date is valid
    if valid == True:
        print('Date is valid')

    return valid

# loop indefinitely
while True:
    print('Please enter a date in the following format: dd/mm/yyyy')
    regex_date_validator(str(input()))
    

