import random


def winner(board):
    """This function accepts the Connect Four board as a parameter.
    If there is no winner, the function will return the empty string "".
    If the user has won, it will return 'X', and if the computer has
    won it will return 'O'."""




    # No winner: return the empty string
    return ""


def display_board(board):
    """This function accepts the Connect Four board as a parameter.
    It will print the Connect Four board grid (using ASCII characters)
    and show the positions of any X's and O's.  It also displays
    the column numbers on top of the board to help
    the user figure out the coordinates of their next move.
    This function does not return anything."""

    print("   0   1   2   3   4   5   6")
    print()
    print("   " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " | " + board[0][3] + " | " + board[0][
        4] + " | " + board[0][5] + " | " + board[0][6])
    print("  ---+---+---+---+---+---+---")
    print("   " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " | " + board[1][3] + " | " + board[1][
        4] + " | " + board[1][5] + " | " + board[1][6])
    print("  ---+---+---+---+---+---+---")
    print("   " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " | " + board[2][3] + " | " + board[2][
        4] + " | " + board[2][5] + " | " + board[2][6])
    print("  ---+---+---+---+---+---+---")
    print("   " + board[3][0] + " | " + board[3][1] + " | " + board[3][2] + " | " + board[3][3] + " | " + board[3][
        4] + " | " + board[3][5] + " | " + board[3][6])
    print("  ---+---+---+---+---+---+---")
    print("   " + board[4][0] + " | " + board[4][1] + " | " + board[4][2] + " | " + board[4][3] + " | " + board[4][
        4] + " | " + board[4][5] + " | " + board[4][6])
    print("  ---+---+---+---+---+---+---")
    print("   " + board[5][0] + " | " + board[5][1] + " | " + board[5][2] + " | " + board[5][3] + " | " + board[5][
        4] + " | " + board[5][5] + " | " + board[5][6])
    print("  ---+---+---+---+---+---+---")
    print("   " + board[6][0] + " | " + board[6][1] + " | " + board[6][2] + " | " + board[6][3] + " | " + board[6][
        4] + " | " + board[6][5] + " | " + board[6][6])
    print()


def make_user_move(board):
    """This function accepts the Connect Four board as a parameter.
    It will ask the user for a row and column.  If the row and
    column are each within the range of 0 and 6, and that square
    is not already occupied, then it will place an 'X' in that square."""
 
    valid_move = False
    while not valid_move:
        col = int(input("What column would you like to move to (0-6):"))
        if board[0][col] != ' ':
            print("Sorry, that column is full. Please try again!\n")
        else:
            for row in range(6, -1, -1):
                if board[row][col] == ' ' and not valid_move:
                    board[row][col] = 'X'
                    valid_move = True
    return board


def make_computer_move(board):
    """This function accepts the Connect Four board as a parameter.
    It will randomly pick row and column values between 0 and 6.
    If that square is not already occupied it will place an 'O'
    in that square.  Otherwise, another random row and column
    will be generated."""
    computer_valid_move = False
    while not computer_valid_move:
        col = random.randint(0, 6)
        if board[0][col] != ' ':
            print("Sorry, that column is full. Please try again!\n")
        else:
            for row in range(6, -1, -1):
                if board[row][col] == ' ' and not computer_valid_move:
                    board[row][col] = 'O'
                    computer_valid_move = True
    return board


def main():
    """The Main Game Loop:"""

    free_cells = 42
    users_turn = True
    ttt_board = [[" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "]]

    while not winner(ttt_board) and (free_cells > 0):
        display_board(ttt_board)
        if users_turn:
            ttt_board = make_user_move(ttt_board)
            users_turn = not users_turn
        else:
            ttt_board = make_computer_move(ttt_board)
            users_turn = not users_turn
        free_cells -= 1

    display_board(ttt_board)
    if (winner(ttt_board) == 'X'):
        print("Y O U   W O N !")
    elif (winner(ttt_board) == 'O'):
        print("I   W O N !")
    else:
        print("S T A L E M A T E !")
    print("\n*** GAME OVER ***\n")


# Start the game!
main()

# if __name__ == "__main__":
#     main()