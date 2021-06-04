from random import randrange

# The lists will be understood when you go further into the code
Player_Options = ["1", "2", "3"]
Choices = ["rock.", "paper.", "scissors."]
AI_Loses = ["scissors.", "rock.", "paper."]
AI_Wins = ["paper.", "scissors.", "rock."]
Difficulties = Player_Options

# AI will not choose, each difficulty has a different probability of outcome
# AI's roll will result in a win, lose or draw


def Play(x, y):
    if AI in range(1, x):
        Win()
    elif AI in range(x, y):
        Draw()
    else:
        Lose()


# AI's roll will result in the outcome, we manipulate AI's choice using indexing
# Hence why the lists were arranged in that manner
def Win():
    Message(Choices, AI_Loses, "You win!")


def Draw():
    Message(Choices, Choices, "It's a draw!")


def Lose():
    Message(Choices, AI_Wins, "You lost!")


def Message(PlayerChoice, AIChoice, OutcomeMessage):
    print("You chose", PlayerChoice[P1ayer], "AI chose", AIChoice[P1ayer])
    print(OutcomeMessage)


# Here is where the game starts
while True:

    # AI rolls, Player chooses Difficulty
    while True:
        AI = randrange(1, 11)
        print("1 Easy, 2 Medium, 3 Hard")
        Difficulty = input("Select Difficulty")
        if Difficulty in Difficulties:
            Diff = int(Difficulty)

            # Easy
            if Diff == 1:
                print("Easy difficulty!")
                while True:
                    Player = input("1:Rock, 2:Paper, 3:Scissors")
                    if Player in Player_Options:
                        P1ayer = int(Player) - 1
                        Play(6, 9)
                        break
                    else:
                        continue

            elif Diff == 2:
                print("Medium difficulty!")
                while True:
                    Player = input("1:Rock, 2:Paper, 3:Scissors")
                    if Player in Player_Options:
                        P1ayer = int(Player) - 1
                        Play(5, 7)
                        break
                    else:
                        continue

            else:
                print("Hard difficulty!")
                while True:
                    Player = input("1:Rock, 2:Paper, 3:Scissors")
                    if Player in Player_Options:
                        P1ayer = int(Player) - 1
                        Play(4, 7)
                        break
                    else:
                        continue
            break

        else:
            continue  # Player didn't choose valid difficulty

    Replay = input("Enter X to quit, Enter any key to play again.")
    if Replay == "x" or Replay == "X":
        break
