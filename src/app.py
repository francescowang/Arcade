import sys  # exit the programme cleanly
import core  # unresolved import -> select the correct Python interpreter
from guess_numbers import guess_number_menu, player_guess, computer_guess
from snake_cli import snake_main
import tictactoe_friend
import tictactoe_computer
import tictactoe_ai
import hangman
import rps_computer

# import connect_4

# functions
core.clear_terminal()
core.welcome_message()
core.press_enter()


# inputs
username = input("What is your username? ")

while True:
    core.clear_terminal()
    core.main_menu()
    user = input(
        f"\nWelcome to the Arcade {username}. Please select the following options: "
    )
    if user == "0":
        core.thank_you()
        sys.exit(0)

    elif user == "1":
        guess_menu = True
        while guess_menu == True:
            core.clear_terminal()
            guess_number_menu()  # guess_menu is an imported function
            user_value = input(
                f"Hi {username.strip()}. Please select the following options: "
            )
            core.clear_terminal()
            if user_value == "0":
                core.thank_you()
                sys.exit(0)
            elif user_value == "1":
                core.clear_terminal()
                player_guess(10000)  # x is now 10
            elif user_value == "2":
                core.clear_terminal()
                computer_guess(10000)  # x is now 10000
            elif user_value == "3":
                core.clear_terminal()
                guess_menu = False  # returns back to the guess_menu
            else:
                print(
                    f"\nSorry {username}. Invalid input. Enter one of the available inputs."
                )
    elif user == "2":
        snake_menu = True
        while snake_menu == True:
            core.clear_terminal()  # maybe I can put this function in the snake_menu function to save space
            core.snake_menu()
            user_value = input(
                f"Hi {username.strip()}. Please select the following options: "
            )
            core.clear_terminal()
            if user_value == "0":
                core.thank_you()
                sys.exit(0)
            elif user_value == "1":
                core.clear_terminal()
                snake_main()
            elif user_value == "2":
                core.clear_terminal()
                import snake_pygame
            elif user_value == "3":
                core.clear_terminal()
                snake_menu = False
            else:
                print(
                    f"\nSorry {username}. Invalid input. Enter one of the available inputs."
                )
    elif user == "3":
        tictactoe_menu = True
        while tictactoe_menu == True:
            core.clear_terminal()
            core.tictactoe_menu()
            user_value = input(
                f"Hi {username.strip()}. Please select the following options: "
            )
            core.clear_terminal()
            if user_value == "0":
                core.thank_you()
                sys.exit(0)
            elif user_value == "1":
                core.clear_terminal()
                tictactoe_friend.commence_game()
            elif user_value == "2":
                core.clear_terminal()
                tictactoe_computer.commence_game()
            elif user_value == "3":
                core.clear_terminal()
                tictactoe_ai.commence_game()
            elif user_value == "4":
                core.clear_terminal()
                tictactoe_menu = False
            else:
                print(
                    f"\nSorry {username}. Invalid input. Enter one of the available inputs."
                )
    elif user == "4":
        connect4menu = True
        while connect4menu == True:
            core.clear_terminal()
            core.connect4_menu()
            user_value = input(
                f"Hi {username.strip()}. Please select the following options: "
            )
            core.clear_terminal()
            if user_value == "0":
                core.thank_you()
                sys.exit(0)
            if user_value == "1":
                core.clear_terminal()
                import connect4
            if user_value == "2":
                core.clear_terminal()
                import connect4ai
            if user_value == "3":
                core.clear_terminal()
                connect4menu = False
            else:
                print(
                    f"\nSorry {username}. Invalid input. Enter one of the available inputs."
                )
    elif user == "5":
        various_games_menu = True
        while various_games_menu == True:
            core.clear_terminal()
            core.various_games()
            user_value = input(
                f"Hi {username.strip()}. Please select the following options: "
            )
            core.clear_terminal()
            if user_value == "0":
                core.thank_you()
                sys.exit(0)
            elif user_value == "1":
                core.clear_terminal()
                hangman.hangman_main()
            elif user_value == "2":
                core.clear_terminal()
                rps_computer.rsp_computer()
            elif user_value == "3":
                core.clear_terminal()
                import space_invaders
            elif user_value == "4":
                core.clear_terminal()
                various_games_menu = False
            else:
                print(
                    f"\nSorry {username}. Invalid input. Enter one of the available inputs."
                )