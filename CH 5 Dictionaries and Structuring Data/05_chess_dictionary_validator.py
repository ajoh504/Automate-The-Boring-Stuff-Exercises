"""
This program takes a dictionary and runs it through a function
to determine if the dictionary is a valid chessboard. The program
assumes a board format of 'a1' as a sample key and 'wrook' as a 
sample value.

Function searches for five criteria: 
1 Board contains 64 squares
2 Board squares are a1 through h8
3 Sum of pawn, rook, queen, bishop, and knight <= 15
4 No more than 8 pawns per color
5 No more than 1 king per color

"""
chess_board = {
    "a1": "wrook",
    "b1": "wknight",
    "c1": "wbishop",
    "d1": "wqueen",
    "e1": "wking",
    "f1": "wbishop",
    "g1": "wknight",
    "h1": "wrook",
    "a2": "wpawn",
    "b2": "wpawn",
    "c2": "wpawn",
    "d2": "wpawn",
    "e2": "wpawn",
    "f2": "wpawn",
    "g2": "wpawn",
    "h2": "wpawn",
    "a3": "",
    "b3": "",
    "c3": "",
    "d3": "",
    "e3": "",
    "f3": "",
    "g3": "",
    "h3": "",
    "a4": "",
    "b4": "",
    "c4": "",
    "d4": "",
    "e4": "",
    "f4": "",
    "g4": "",
    "h4": "",
    "a5": "",
    "b5": "",
    "c5": "",
    "d5": "",
    "e5": "",
    "f5": "",
    "g5": "",
    "h5": "",
    "a6": "",
    "b6": "",
    "c6": "",
    "d6": "",
    "e6": "",
    "f6": "",
    "g6": "",
    "h6": "",
    "a7": "bpawn",
    "b7": "bpawn",
    "c7": "bpawn",
    "d7": "bpawn",
    "e7": "bpawn",
    "f7": "bpawn",
    "g7": "bpawn",
    "h7": "bpawn",
    "a8": "brook",
    "b8": "bknight",
    "c8": "bbishop",
    "d8": "bqueen",
    "e8": "bking",
    "f8": "bbishop",
    "g8": "bknight",
    "h8": "brook",
}

# main program
def is_valid_chess_board(board: dict) -> bool:
    is_valid = True  # final return value, change to False if board not valid
    board_squares = list(board.keys())  # store board squares in list
    temp_list = list(board.values())  # temporary list for storing chess pieces, will remove empty strings from this list
    board_pieces = []  # new list after removing empty strings
    bpawn = 0
    brook = 0
    bknight = 0
    bbishop = 0
    bqueen = 0
    bking = 0
    wpawn = 0
    wrook = 0
    wknight = 0
    wbishop = 0
    wqueen = 0
    wking = 0

    # place non-empty strings in new list: board_pieces
    for i in temp_list:
        if bool(i) != False:
            board_pieces.append(i)

    # check number of board squares
    if len(board_squares) != 64:
        is_valid = False
        print("Invalid number of board squares.")

    # check format of board squares
    for i in board_squares:
        letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
        nums = ["1", "2", "3", "4", "5", "6", "7", "8"]
        if i[0] not in letters or i[1] not in nums:
            is_valid = False
            print("Format error. Check format of board squares. Board must have 64 squares, a1 through h8.")

    # count pieces
    for i in board_pieces:
        if i == "bpawn":
            bpawn += 1
        elif i == "brook":
            brook += 1
        elif i == "bknight":
            bknight += 1
        elif i == "bbishop":
            bbishop += 1
        elif i == "bqueen":
            bqueen += 1
        elif i == "bking":
            bking += 1
        elif i == "wpawn":
            wpawn += 1
        elif i == "wrook":
            wrook += 1
        elif i == "wknight":
            wknight += 1
        elif i == "wbishop":
            wbishop += 1
        elif i == "wqueen":
            wqueen += 1
        elif i == "wking":
            wking += 1
        else:
            is_valid = False
            print("Invalid piece format.")

    # sum of pawns, rooks, knights, queens, bishops must be <= 15
    if (bpawn + bbishop + brook + bknight + bqueen) > 15:
        is_valid = False
        print("Invalid piece count.")
    if (wpawn + wbishop + wrook + wknight + wqueen) > 15:
        is_valid = False
        print("Invalid piece count.")

    # check for no more than 8 pawns per color
    if (bpawn > 8) or (wpawn > 8):
        is_valid = False
        print("Invalid pawn count.")      

    # check for no more than 1 king per color
    white_king = 0
    black_king = 0
    for i in board_pieces:
        if i == "wking":
            white_king += 1
        if i == "bking":
            black_king += 1
    if (white_king > 1) or (black_king > 1):
        is_valid = False
        print("Invalid king count.")

    print(is_valid)
    return is_valid


is_valid_chess_board(chess_board)
