#an example of a for loop
#The loop prints the phrase "Jimmy Fives times"
#and prints 'i' each time
#

print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')


#the same code re-written using a for loop

print('My name is')
i = 0
while i < 5:
    print('Jimmy Five Times (' + str(i) + ')')
    i = i + 1