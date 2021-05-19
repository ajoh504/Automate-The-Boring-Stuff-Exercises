# This function takes a list with string values, and
# returns the list as a single string, separated by 
# commas, with 'and' before the last item. The 
# function can receive a list with any number of 
# values. Function returns a message if the list 
# contains no items. 

def listToString(list):
    if list == []:
        print('List must contain items.')
    newString = ''
    for i in list:
        if list.index(i) == len(list)-1:
            newString += 'and ' + i
        else:
            newString += i + ', '
        print(newString)
    return newString
    
spam = ['apples','bananas','tofu','cats']
spam2 = []
listToString(spam)
listToString(spam2)
