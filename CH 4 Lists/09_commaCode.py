#receive a list and return a string value
#with all items separated by commas, and
#the word "and" before the last item. Must
#account for an empty list.

def addCommasToList(listToConvert):
    string = ''
    if len(listToConvert) == 0:
        string = 'List contains no items.'
    elif len(listToConvert) == 1:
        string = str(listToConvert[0])
    elif len(listToConvert) == 2:
        string = str(listToConvert[0]) + ' and ' + str(listToConvert[1])
    else: 
        for i in listToConvert :
            string += str(i) + ', '
            if i == listToConvert[-2]:
                string += 'and ' + str(listToConvert[-1])
                break
    print(string)
    return string
    
testList = ['salad', 'potato', 'soup']  
testList2 = []
testList3 = [1]
testList4 = [1,2]
addCommasToList(testList)
addCommasToList(testList2)
addCommasToList(testList3)
addCommasToList(testList4)
