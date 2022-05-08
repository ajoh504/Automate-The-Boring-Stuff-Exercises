#! python3
# 04_password_strength.py -- function to test the strength of a password
# password must contain at least 1 upper case letter, 1 lower case letter,
# 1 number, and be greater than or equal to 8 characters

import re

# pw = password
# function receives user input (password) as argument
def pw_strength_test(pw: str) -> bool:
    is_strong = True # final return value, change to False if test fails
    
    # lowercase, uppercase, and number regexes
    lower_regex = re.compile(r"[a-z]")
    upper_regex = re.compile(r"[A-Z]")
    num_regex = re.compile(r"\d")

    # store matches into lists
    lower_groups = lower_regex.findall(pw)
    upper_groups = upper_regex.findall(pw)
    num_groups = num_regex.findall(pw)

    return lower_groups and upper_groups and num_groups and len(pw) >= 8

def main() -> bool:
        user_input = str(input('Please enter your password.\n'))
        password_test_result = pw_strength_test(user_input)
        return bool(password_test_result) 

if __name__ == "__main__":
    print(main())
