


board = ['#','#','#','#','#','#','#','#','#','#']

# This function takes the board list as a parameter and replaces the case number 
# inside the blankBoard with either the player’s choice or a blank space.
def display_board(board):
    blank_board = """
    
|-----------------|
|  1  |  2  |  3  |
|-----------------|
|  4  |  5  |  6  |
|-----------------|
|  7  |  8  |  9  |
|-----------------|
    
"""
    for num in range(1,10):
        if(board[num] == "O" or board[num] == "X"):
            blank_board = blank_board.replace(str(num), board[num])
        else:
            blank_board = blank_board.replace(str(num), ' ')
    print(blank_board)


# The second function will ask player one which marker they want. Choices can be X/x or O/o. 
# If another choice is made by the user, the program must re-ask for an input.
def player_input():
    player1 = input("Please pick a marker 'X' or 'O': ")
    while True:
        if player1.upper() == "X":
            player2 = "O"
            print("You have choosen " + player1 + ". Player 2 will be " + player2)
            return player1.upper(), player2
        elif player1.upper() == "O":
            player2 = "X"
            print("You have choosen " + player1 + ". Player 2 will be " + player2)
            return player1.upper(), player2
        else:
            player1 = input("Please pick a marker 'X' or 'O': ")

# Here, we simply use a while True statement, which will be exited by a return if the input matches the possibilities. 
# Note that we are applying the input if player1.upper() == ‘X’: to avoid double checks.


# The third function will be the place_marker.
def place_marker(board, marker, position):
    board[position] = marker
    return board

# We just pass the board list, the marker, and the position chosen. 
# The function will assign the marker to our list, replacing the # character at the given position.


# Hereafter, both our functions will ask the player for a position and check whether the chosen position is empty or not. 
# These two functions are linked, and that’s why I put these two behind together.
def space_check(board, position):
    return board[position] == "#"
def player_choice(board):
    choice = input("Please select an empty space between 1 and 9: ")
    while not space_check(board, int(choice)):
        choice = input("This space is not free. Please choose between 1 and 9: ")
    return choice


# Only three functions remain: Is the board full? Has someone won? Do you want to play again?
def full_board_check(board):
    return len([x for x in board if x == "#"]) == 1


def win_check(board, mark):
    if board[1] == board[2] == board[3] == mark:
        return True
    if board[4] == board[5] == board[6] == mark:
        return True
    if board[7] == board[8] == board[9] == mark:
        return True
    if board[1] == board[4] == board[7] == mark:
        return True
    if board[2] == board[5] == board[8] == mark:
        return True
    if board[3] == board[6] == board[9] == mark:
        return True
    if board[1] == board[5] == board[9] == mark:
        return True
    if board[3] == board[5] == board[7] == mark:
        return True
    return False


# We’re at our last function before our main program, 
# and that’s just asking the users if they want to play again.
def replay():
    play_again = input("Would you like to play again (y/n)? ").strip()
    if play_again.lower() == "y":
        return True
    if play_again.lower() == "n":
        return False
    

if __name__ == "__main__":
    print('Welcome to Tic Tac Toe!')
    i = 1
    # Choose your side
    players=player_input()
    # Empty board init
    board = ['#'] * 10
    while True:
        # Set the game up here
        game_on=full_board_check(board)
        while not game_on:
            # Player to choose where to put the mark
            position = player_choice(board)
            # Who's playin ? Choose the marker
            if i % 2 == 0:
                marker = players[1]
            else:
                marker = players[0]
            # Play !
            place_marker(board, marker, int(position))
            # # Check the board
            display_board(board)
            i += 1
            if win_check(board, marker):
                print("You won !")
                break
            game_on=full_board_check(board)
        if not replay():
            break
        else:
            i = 1
            # Choose your side
            players=player_input()
            # Empty board init
            board = ['#'] * 10
