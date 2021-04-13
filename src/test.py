import sys # exit the programme cleanly
import core # unresolved import -> select the correct Python interpreter
import os
import guess_numbers
import play_vs_friend
# import connect_4

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
            guess_numbers.guess_menu() # guess_menu is an imported function
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
    elif user == "2":
        snake_menu = True
        while snake_menu == True:
            core.clear_terminal() # maybe I can put this function in the snake_menu function to save space
            core.snake_menu()
            user_value = input(f"Hi {username.strip()}. Please select the following options: ")
            core.clear_terminal()
            if user_value == "0":
                core.thank_you()
                sys.exit(0)
            elif user_value == "1":
                core.clear_terminal()
                import snake_cli
            elif user_value == "2":
                core.clear_terminal()
                import snake_pygame
            elif user_value == "3":
                core.clear_terminal()
                snake_menu = False
            else:
                print(f"\nSorry {username}. Invalid input. Enter one of the available inputs.")
    elif user == "3":
        tictactoe_menu = True
        while tictactoe_menu == True:
            core.clear_terminal()
            core.tictactoe_menu()
            user_value = input(f"Hi {username.strip()}. Please select the following options: ")
            core.clear_terminal()
            if user_value == "0":
                core.thank_you()
                sys.exit(0)
            elif user_value == "1":
                core.clear_terminal()
                play_vs_friend.commence_game()
            elif user_value == "2":
                core.clear_terminal()
                import play_vs_computer
            elif user_value == "3":
                core.clear_terminal()
                import play_vs_ai
            elif user_value == "4":
                core.clear_terminal()
                tictactoe_menu = False
            else:
                print(f"\nSorry {username}. Invalid input. Enter one of the available inputs.")
    elif user == "4":
        rockpaperscissors_menu = True
        while rockpaperscissors_menu == True:
            core.clear_terminal()
            core.rockpaperscissors_menu()
            user_value = input(f"Hi {username.strip()}. Please select the following options: ")
            core.clear_terminal()
            if user_value == "0":
                core.thank_you()
                sys.exit(0)
            if user_value == "1":
                core.clear_terminal()
                import rps_vs_friend
            if user_value == "2":
                core.clear_terminal()
                import rps_vs_computer
            if user_value == "3":
                core.clear_terminal()
                import rps_vs_ai
            if user_value == "4":
                core.clear_terminal()
                rockpaperscissors_menu = False
            else:
                print(f"\nSorry {username}. Invalid input. Enter one of the available inputs.")
    elif user == "5":
        hangman_menu = True
        while hangman_menu == True:
            core.clear_terminal()
            core.hangman_menu()
            user_value = input(f"Hi {username.strip()}. Please select the following options: ")
            core.clear_terminal()
            if user_value == "0":
                core.thank_you()
                sys.exit(0)
            elif user_value == "1":
                core.clear_terminal()
                import hangman_vs_computer
            elif user_value == "2":
                core.clear_terminal()
                import hangman_vs_ai
            elif user_value == "3":
                core.clear_terminal()
                hangman_menu = False
            else:
                print(f"\nSorry {username}. Invalid input. Enter one of the available inputs.")
                
# connect_4.main()