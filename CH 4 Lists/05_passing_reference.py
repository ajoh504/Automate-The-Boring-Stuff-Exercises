# This function has no return statement because it
# modifies the list in place, rather than
# returning a new list. In this instance, the return
# value is None

def eggs(some_parameter):
    some_parameter.append('Hello')
spam = [1,2,3]
eggs(spam)
print(spam)
