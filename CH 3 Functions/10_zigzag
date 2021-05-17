#This program creates a zigzag pattern in the console.
#The time module prevents the programming from running
#too fast. A while loop prints an empty string 
#multiplied by the value of the 'indent' variable.
#This value increases by 1 each iteration of the loop
#Once the indent equals 20, it reverses in the opposite
#direction by subtracting 1 from 'indent' 

import time, sys
indent = 0 # How many spaces to indent
indentIncreasing = True # Whether the indentation is increasing or not
try:
    while True: # The main program loop.
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10 of a second
        if indentIncreasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == 20:
                # Change direction:
                indentIncreasing = False
        else:
            # Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # Change direction
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
