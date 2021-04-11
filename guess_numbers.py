import random

def guess(x):
    random_number = random.randint(1, x) # begins at 1
    guess = 0 # guess won't be 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("\nSorry, guess again. The number is too low.\n")
        elif guess > random_number:
            print("\nSorry, guess again. The number is too high.\n")
    print(f"\nCongratulations. You have guessed the correct number {random_number}.\n")


def computer_guess(x):
    low = 1
    high = x
    feedback = '' # nothing is too low or high for the time being
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high b/c low = high
        feedback = input(f'\nIs {guess} too high (H), too low (L), or correct (C)? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"\nCongratulations. The computer guessed your number, {guess}, correctly.\n")
    
guess(1000)
computer_guess(10000)
