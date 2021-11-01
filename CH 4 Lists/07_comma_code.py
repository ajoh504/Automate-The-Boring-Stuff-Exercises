# This function takes a list with string values, and
# returns the list as a single string, separated by 
# commas, with 'and' before the last item. The 
# function can receive a list with any number of 
# values. Function returns a message if the list 
# contains no items. 

def list_to_string(list):
    if list == []:
        print('List must contain items.')
    new_string = ''
    for i in list:
        if list.index(i) == len(list)-1:
            new_string += 'and ' + i
        else:
            new_string += i + ', '
        print(new_string)
    return new_string
    
spam = ['apples','bananas','tofu','cats']
spam2 = []
list_to_string(spam)
list_to_string(spam2)
