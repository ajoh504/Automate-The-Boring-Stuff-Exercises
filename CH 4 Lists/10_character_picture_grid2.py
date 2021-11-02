# This is an expanded version of the Character Picture Grid
# problem from Al Sweigart's book, Automate the Boring Stuff With Python.
# This function takes in user input to determine what direction to print
# the arrow.

RIGHT_ARROW = [
    [".", ".", ".", ".", ".", "."],
    [".", "O", "O", ".", ".", "."],
    ["O", "O", "O", "O", ".", "."],
    ["O", "O", "O", "O", "O", "."],
    [".", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "."],
    ["O", "O", "O", "O", ".", "."],
    [".", "O", "O", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
]

ROW_LENGTH = len(RIGHT_ARROW[0])  # length of x plane coordinates
COLUMN_LENGTH = len(RIGHT_ARROW)  # length of y plane coordinates
SEPARATOR = "     " # empty space keeps arrow's shape when it's printed to the console. 

def main():  # main program
    print("Welcome to Arrow Pointer v1.0!")
    while True:
        print(
            "\n\nType in one of the following:\n\nup, down, left, right, or end to exit the program."
        )
        # user determines direction of arrow to be printed
        user_input = input()
        if user_input.lower() == "right":
            for i in range(COLUMN_LENGTH):
                for j in range(ROW_LENGTH):
                    # first loop iterates through RIGHT_ARROW elements
                    # nested loop iterates through inner list elements
                    print(RIGHT_ARROW[i][j] + SEPARATOR, end="")
                    # empty space to keep the arrow's shape when it's printed to the console
                print("\n")

        if user_input.lower() == "left":
            for i in range(COLUMN_LENGTH):
                for j in range(ROW_LENGTH - 1, -1, -1):
                    # iterate backwards to print arrow in opposite direction
                    print(RIGHT_ARROW[i][j] + SEPARATOR, end="")
                print("\n")

        if user_input.lower() == "down":
            for i in range(ROW_LENGTH):
                for j in range(COLUMN_LENGTH):
                    print(RIGHT_ARROW[j][i] + SEPARATOR, end="")
                print("\n")

        if user_input.lower() == "up":
            for i in range(ROW_LENGTH - 1, -1, -1):
                for j in range(COLUMN_LENGTH - 1, -1, -1):
                    print(RIGHT_ARROW[j][i] + SEPARATOR, end="")
                print("\n")

        if user_input.lower() == "end":
            return


if __name__ == "__main__":
    main()
