# This code demonstrates how to check a list
# to see if an item is stored in it using the
# 'not in' operator

my_pets = ['Zombie','Pooka','Fat-tail']
print('Enter a pet name')
name = input()
if name not in my_pets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')
