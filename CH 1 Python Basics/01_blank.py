#example of a while Loop
#the loop repeats infinitely until the user
#types the exact phrase 'your name'

while True:
    print ('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you')
