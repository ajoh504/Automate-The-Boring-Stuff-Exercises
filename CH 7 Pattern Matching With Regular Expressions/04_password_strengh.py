# function to test the strength of a password

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

    # def a function to iterate over the regex lists
    # pass list and type into function
    # return number of items of that type
    def count_matches(match_list, match_type):
        count = 0
        try:
            if match_type == str and match_list[0].islower() == True:
                count = len(match_list)
            elif match_type == str and match_list[0].isupper() == True:
                count = len(match_list)
            elif match_type == int:
                count = len(match_list)
        # if no items in list, IndexError will be thrown
        except IndexError:
            print('IndexError thrown. One or more match lists are empty.')

        return count

    # store count into variables
    lower_count = count_matches(lower_groups, str)
    upper_count = count_matches(upper_groups, str)
    num_count = count_matches(num_groups, int)
    
    # if any list contains 0 items, pw test fails
    if lower_count == 0 or upper_count == 0 or num_count == 0:
        is_strong = False
        print("Error: password strength test failed.")
    # if less than 8 characters,
    elif (lower_count + upper_count + num_count) < 8:
        is_strong = False
        print("Error: password strength test failed.")
    else:
        print("Password strength test passed.")

    return is_strong

print('Please enter your password.')
pw_strength_test(str(input()))
