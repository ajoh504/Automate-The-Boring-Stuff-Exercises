# the sys.exit() function can be used to terminate a program
# early. All programs terminate when they reach the last line
# of code, but some may require you to end it sooner. The while
# loop will repeat the user input if they do not type 'exit'

import sys
while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
