import os
import time


# cleaning the terminal
def clear_terminal(): # os module is needed to run this function
    clear = lambda: os.system('cls' if os.name == 'nt' else 'clear') # a lambda function can take any number of arguments, but can only have one expression
    clear() # calling clear


# time module works with file handling
def welcome_message():
    clear_terminal()
    file = open("./data/welcome.txt", "r")
    contents = file.read()
    print(contents)
    file.close()
    time.sleep(2)
    clear_terminal()


# the user presses enter to display a txt file (file handling)
def press_enter():
    clear_terminal()
    file = open("./data/enter.txt", "r")
    contents = file.read()
    print(contents)
    file.close()
    input() # "stops" the app and ask the user for an input
    clear_terminal()


# congratulations message
def congrats():
    file = open("./data/congratulations.txt", "r")
    contents = file.read()
    print(contents)
    file.close()
    input()
    clear_terminal()


# main menu of the app
def main_menu():
    file = open("./data/main_menu.txt", "r")
    contents = file.read()
    print(contents)
    file.close()


# thank you message
def thank_you():
    clear_terminal()
    file = open("./data/thank_you.txt", "r")
    contents = file.read()
    print(contents)
    file.close()
    


###########

# snake_menu for app.py
def snake_menu():
    # clear_terminal()
    print('''
    Select [0] to exit the arcade.

    Select [1] to play snake on CLI.

    Select [2] to play snake on PYGAME.

    Select [3] to return to the arcade menu.
    ''')


# tic tac toe menu for app.py
def tictactoe_menu():
    print('''
    Select [0] to exit the arcade.

    Select [1] to play tic tac toe vs friend.

    Select [2] to play tic tac toe vs computer.
    
    Select [3] to play tic tac toe vs AI.

    Select [4] to return to the arcade menu.
    ''')
    

def rockpaperscissors_menu():
    print('''
    Select [0] to exit the arcade.

    Select [1] to play rock paper scissors vs friend.

    Select [2] to play rock paper scissors vs computer.
    
    Select [3] to play rock paper scissors vs AI.
    
    Select [4] to return to the arcade menu.
    ''')
    
    
def various_games():
    print('''
    Select [0] to exit the arcade.

    Select [1] to play hangman.

    Select [2] to play rock paper scissors vs computer.
    
    Select [3] to return to the arcade menu.
    ''')