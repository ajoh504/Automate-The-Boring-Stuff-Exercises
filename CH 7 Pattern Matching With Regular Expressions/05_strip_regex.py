'''Write a function that takes a string and does the same thing as the strip()
string method. If no other arguments are passed other than the string to strip,
then whitespace characters will be removed from the beginning and end of the
string.Otherwise, the characters specified in the second argument to the
function will be removed from the string.'''

def regex_strip(str1, str2):
    # receive string argument to edit, and string argument to remove.
    # If no string to remove is provided, remove whitespace characters. 
    str_to_edit = str1
    str_to_remove = str2

string = 'Hello, world!'

regex_strip(string)
