from re import findall

# str1 is string to strip
# str2 is optional string to remove from str1
def regex_strip_method(str1, str2=''): 
    stripped_str = '' # final return value

    # if str2 is not given, remove whitespace from beginning and end
    if str2 == '':
        regex_list = findall(r'\S*', str1)
        while '' in regex_list:
            regex_list.remove('')
        stripped_str = ' '.join(regex_list)

    # remove empty strings from regex_list
    if str2 != '':
        regex_list = findall(r'\S*', str1)
        while '' in regex_list:
            regex_list.remove('')

        # remove str2 from beginning and end of str1    
        if str2 in regex_list[0]:
            regex_list[0] = regex_list[0].replace(str2, '')
        if str2 == regex_list[-1]:
            regex_list[-1] = regex_list[-1].replace(str2, '')
        stripped_str = ' '.join(regex_list)
    
    return stripped_str
