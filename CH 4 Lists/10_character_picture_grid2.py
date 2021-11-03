# This is an expanded version of the Character Picture Grid
# problem from Al Sweigart's book, Automate the Boring Stuff With Python.
# This function takes in user input to determine what direction to print
# the arrow. Changes were made based on Code Review at: https://codereview.stackexchange.com/questions/267666/expanding-on-a-problem-from-automate-the-boring-stuff

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
SEPARATOR = (
    "     "  # empty space to keep arrow's shape when it's printed to the console.
)

# function to print arrow either left or right
def _print_arrow_left_right(
    x_start: int, x_end: int, x_step: int, y_start: int, y_end: int, y_step: int
) -> None:
    for i in range(y_start, y_end, y_step):  # loop through columns
        for j in range(x_start, x_end, x_step):  # loop through rows
            print(RIGHT_ARROW[i][j] + SEPARATOR, end="")
        print("\n")


# function to print arrow either up or down
def _print_arrow_up_down(
    x_start: int, x_end: int, x_step: int, y_start: int, y_end: int, y_step: int
) -> None:
    for i in range(x_start, x_end, x_step):  # loop through rows
        for j in range(y_start, y_end, y_step):  # loop through columns
            print(RIGHT_ARROW[j][i] + SEPARATOR, end="")
        print("\n")


def main() -> None:  # main program prints instructions and accepts user input
    print("Welcome to Arrow Pointer v1.0!")
    while True:
        print(
            "\n\nType in one of the following:\n\nup, down, left, right, or end to exit the program."
        )
        user_input = input()
        # user determines direction of arrow to be printed
        if user_input.lower() == "right":
            _print_arrow_left_right(
                0, ROW_LENGTH, 1, 0, COLUMN_LENGTH, 1
            )  # print pointing right

        if user_input.lower() == "left":
            _print_arrow_left_right(
                ROW_LENGTH - 1, -1, -1, 0, COLUMN_LENGTH, 1
            )  # print pointing left

        if user_input.lower() == "down":
            _print_arrow_up_down(
                0, ROW_LENGTH, 1, 0, COLUMN_LENGTH, 1
            )  # print pointing down

        if user_input.lower() == "up":
            _print_arrow_up_down(ROW_LENGTH - 1, -1, -1, 0, COLUMN_LENGTH, 1)  # up

        if user_input.lower() == "end":
            return


if __name__ == "__main__":
    main()
