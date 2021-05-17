# This code demonstrates how to check a list
# to see if an item is stored in it using the
# 'not in' operator

myPets = ['Zombie','Pooka','Fat-tail']
print('Enter a pet name')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')
