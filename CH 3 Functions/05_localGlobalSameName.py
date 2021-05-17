# This example shows how using the same variable name
# in different scopes creates entirely different variables.
# This is not considered a good practice,
# because it makes it difficult to keep track of
# of the different variables.
# The first 'eggs' variable is local-scoped to the spam()
# function. The second 'eggs' variable is local-scoped
# to the bacon() function. And the final 'eggs' variable
# is global-scoped.

def spam():
    eggs = 'spam local'
    print(eggs) #prints 'spam local'
def bacon():
    eggs = 'bacon local'
    print(eggs) #prints 'bacon local'
    spam()
    print(eggs) #prints 'bacon local'
eggs = 'global'
bacon()
print(eggs) # prints 'global'
