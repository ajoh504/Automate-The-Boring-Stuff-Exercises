import re

def password_strength_test(password):
    
    lowercase_regex = re.compile(r'[a-z]')
    uppercase_regex = re.compile(r'[A-Z]')
    number_regex = re.compile(r'\d')
    
    lowercase_groups = lowercase_regex.findall(password)
    uppercase_groups = uppercase_regex.findall(password)
    number_groups = number_regex.findall(password)
    print(lowercase_groups, uppercase_groups, number_groups)
    #print(regex.findall(str_test))

while True:
    password_strength_test(str(input()))
