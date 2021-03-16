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




