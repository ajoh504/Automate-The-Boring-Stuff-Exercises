import re

# receive string argument to modify (str1), and string argument to
# remove (str2). If str2 is not provided, remove whitespace characters. 
def regex_strip(str1, str2=''):
    if str2 == '':
        regex = re.compile(r'\S*')
        regex_list = regex.findall(str1)
        while '' in regex_list:
            regex_list.remove('')
        return ' '.join(regex_list)
    else:
        regex = re.compile(r'[^'+str2+'].*[^'+str2+']')
        mo = regex.search(str1)
        return mo.group()

string1 = 'Hello, world!'
string2 = 'olleH'

print(regex_strip(string1, string2))

