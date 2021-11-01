eggs = 'global'
def spam():
    print(eggs) # error!
    eggs = 'spam local'

spam()

# this throws an error message because the variable 'eggs'
# is referenced before it is defined
