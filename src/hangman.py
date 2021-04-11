import random  # import random
from words import words # word list that we just made in words.py, imports word file we made.
import string
# Get's entire list of words that we copy and pasted.
def get_valid_word(words): # Define function called get valid word, and pass in a list of words. 
    word = random.choice(words)  # Assign the word to random.choice(words) random.choice randomly chooses something from the list = random word from list. 
    while '-' in word or ' ' in word: # Make a while loop: while dash or space is in this word, keep choosing the word.
        # Above ^ as long as statement is true, it keeps iterating back and forth until it's not true anymore. Which means when it stops iterating, we'll get a word that doesn't have a space or a dash in it. 
        word = random.choice(words)
    return word.upper()  # Then finally we're just going to return that word. Plus we're going to uppercase all our letters
def hangman():  # Keep track of words we've guessed and letters in the word we've correctly guessed. We also need to keep track of what is a valid letter and what isn't. 
    word = get_valid_word(words) # variable that saves all the letters in a word, as a set. This is used, as a way to keep track of what has already been set in the word. 
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)  # import pre-determined list of upper.case characters in the English dictionary. 
    used_letters = set()  # Have an empty set called used_letters, in order to keep track of what the user has guessed
    lives = 6 # introduce the concept of lives. 6 lives in game 
    # getting user input - ask the user directly. 
    # the condition that we have to satisfy when the user gets all the letters in the word, is when the length of word letters is actually = to 0
    while len(word_letters) > 0 and lives > 0: # While the length of the word letter is greater than 0, and lives greater than 0, then we want them to be able to guess. - This means that as soon as they either win, when they've guessed all the letters, then they exit this while loop.  
        # letters used - We need to tell the user what letters they've already used. 
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', # print statement - You have x lives left. - What this .join does is turn this list into a string separated by whatever the string is before the .join 
            ' '.join(used_letters)) # So, each of these letters above ('a b cd' ) will be in a string separated by a space. 
        # tell the user what current word is (i.e W - R D) - Tell the user what the current word is, but with dashes where the characters that they haven't guessed are.
        word_list = [ # Create list where every single letter they've guessed, is shown. and where all the letters they haven't guessed are just dashes.
            letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list)) # Then take that list and join it with a space so we can create a string using that list.
        # we want the user to keep guessing until they get the word. 
        # so, in this case we're going to be using a loop. Loops are used to loop around your code and iterate.
        # for this part of the code, we use while loop so, user can keep guessing until they get the word. 
        user_letter = input('Guess a letter: ').upper()  # user inputs a letter
        if user_letter in alphabet - used_letters: # # if this is already a valid character in the alphabet that I haven't used yet, then, I'm going to add this to my used letters set
            used_letters.add(user_letter)  
            if user_letter in word_letters:  # if the letter that I just guessed is in the word
                word_letters.remove(user_letter) # Then I'm going to remove that letter from word_letters. 
                print('') # Every time I guess correctly, this word_letters that is keeping in contact with all the letters in a word decreases in size.  
            else: # However, if they don't guess the word correctly.
                lives = lives - 1  # then that's when you want to take away a life. Use lives variable to subtract -1
                print('\nYour letter,', user_letter, 'is not in the word.') # Tell the user, the letter they just inputted is is not in the word. Everything else should stay the same. 
        elif user_letter in used_letters:  # if the users letter that they just entered is in used_letters list. That means they've already used it before. 
            print('\nYou have already used that letter. Guess another letter.') # So, we message to user informing them they've already used this letter and suggest an alternative.
        else:  # The user types a non-valid letter not in the alphabet e.g a number.
            print('\nThat is not a valid letter.') # We tell the user that the letter they typed and was not valid in the alphabet. 
    # gets here when len(word_letters) == 0 OR when lives == 0 
    # they exit this while loop. 
    # my while condition is going to be, while the length of word letters is greater than zero, iterate.  
    # they exit this while loop.
    if lives == 0: # If lives equal 0, They died   
        print('You died, sorry. The word was', word)
    else: # They won. 
        print('YAY! You guessed the word', word, '!!')
if __name__ == '__main__':
    hangman()