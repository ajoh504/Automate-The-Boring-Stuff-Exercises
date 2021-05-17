# This program is an improved version of the allMyCats1
# program. The code here uses a while loop to receive any
# number of cat names.

catNames = []
while True:
    print('Enter the name of the cat '
    + str(len(catNames) + 1) +
    ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] #list concatenation
print('The cat names are:')
for name in catNames:
    print(' ' + name)
