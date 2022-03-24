import re

# required argument is user's password
def pw_strength_check(user_pw: str) -> bool:
    
          
    # check for any length number, any lenght lowercase letters
    #pw_regex = re.compile(r'(\d*)([a-z]*)')
    pw_regex = re.compile(r'(.)')
    regex_groups = pw_regex.findall(password)
    #store match object and groups in variables
    #match_object = pw_regex.search(user_pw)
    #regex_groups = match_object.groups()
    print(regex_groups)


while True:
    print('Please enter your password:')
    password = input()
    pw_strength_check(password)
