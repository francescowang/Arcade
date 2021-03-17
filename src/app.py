import sys # exit the programme cleanly
import core # unresolved import -> select the correct Python interpreter
import os

# functions
core.clear_terminal()
# core.welcome_message()
# core.press_enter()

# inputs
username = input("What is your username? ")

while True:
    core.clear_terminal()
    core.main_menu()
    user = input(f"\nWelcome to Tic Tac Toe, {username}. Please select the following options: ")
    if user == "0":
        core.thank_you()
        sys.exit(0)

    elif user == "1":
        core.clear_terminal()
        print("\n")
        import play_vs_friend # impporting py file - is there a better way of importing the file?
    elif user == "2":
        core.clear_terminal()
        print("\n")
        import play_vs_computer
