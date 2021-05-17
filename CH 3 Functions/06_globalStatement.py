# this is an example of the global statement, which tells
# a function to refer to the global variable 'eggs' rather
# than the local 'eggs'

def spam():
    global eggs
    eggs = 'spam'
eggs = 'global'
spam()
print(eggs)
