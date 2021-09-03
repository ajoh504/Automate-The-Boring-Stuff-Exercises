# This is an expanded version of the Character Picture Grid
# problem from Al Sweigart's book, Automate the Boring Stuff With Python.
# This function takes in user input to determine what direction to print
# the arrow.

rightArrow = [['.', '.', '.', '.', '.', '.'], 
              ['.', 'O', 'O', '.', '.', '.'],
              ['O', 'O', 'O', 'O', '.', '.'], 
              ['O', 'O', 'O', 'O', 'O', '.'],
              ['.', 'O', 'O', 'O', 'O', 'O'], 
              ['O', 'O', 'O', 'O', 'O', '.'],
              ['O', 'O', 'O', 'O', '.', '.'], 
              ['.', 'O', 'O', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.']]


def printArrow(list):
    rowLength = len(list[0])  # length of x plane coordinates
    columnLength = len(list)  # length of y plane coordinates
    print('Welcome to Arrow Pointer v1.0!')
    while True:
        #main program loop
        print('\n\nType in one of the following:\n\nup, down, left, right, or end to exit the program.')
        #user determines direction of arrow to be printed
        userInput = input()
        if userInput.lower() == 'right':
            for i in range(columnLength):
                for j in range(rowLength):
                    #first loop iterates through main list
                    #nested loop iterates through inner list elements
                    print(list[i][j] + '     ', end='')
                print('\n')

        if userInput.lower() == 'left':
            for i in range(columnLength):
                for j in range(rowLength - 1, -1, -1):
                    #iterate backwards to print arrow in opposite direction
                    print(list[i][j] + '     ', end='')
                print('\n')

        if userInput.lower() == 'down':
            for i in range(rowLength):
                for j in range(columnLength):
                    print(list[j][i] + '     ', end='')
                print('\n')

        if userInput.lower() == 'up':
            for i in range(rowLength-1, -1, -1):
                for j in range(columnLength-1, -1, -1):
                    print(list[j][i] + '     ', end='')
                print('\n')

        if userInput.lower() == 'end':
            quit()

printArrow(rightArrow)
