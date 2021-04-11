import sys # exit the programme cleanly
import core # unresolved import -> select the correct Python interpreter
import os
import guess_numbers

# functions
core.clear_terminal()
# core.welcome_message()
# core.press_enter()

# inputs
username = input("What is your username? ")

while True:
    core.clear_terminal()
    core.main_menu()
    user = input(f"\nWelcome to the Arcade {username}. Please select the following options: ")
    if user == "0":
        core.thank_you()
        sys.exit(0)

    elif user == "1":
        guess_menu = True
        while guess_menu == True:
            core.clear_terminal()
            guess_numbers.guess_menu()
            user_value = input(f"Hi {username.strip()}. Please select the following options: ")
            core.clear_terminal()
            if user_value == "0":
                core.thank_you()
                sys.exit(0)
            elif user_value == "1":
                core.clear_terminal()
                guess_numbers.player_guess(10) # x is now 10
            elif user_value == "2":
                core.clear_terminal()
                guess_numbers.computer_guess(10000) # x is now 10000
            elif user_value == "3":
                core.clear_terminal()
                guess_menu = False # returns back to the guess_menu
            else:
                print(f"\nSorry {username}. Invalid input. Enter one of the available inputs.")