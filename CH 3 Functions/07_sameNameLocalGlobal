# This program shows how to rewrite the value of a
# global-scoped variable from within a function. To
# do this, you must use the 'global' command before
# the variable. This prevents Python from creating a
# local version of that variable within the function.

def spam():
    global eggs
    eggs = 'spam' # this is global scoped
def bacon():
    eggs = 'bacon' # this is local scoped
def ham():
    print(eggs) # this is global scoped
eggs = 42 #this is global scoped
spam()
print(eggs)
