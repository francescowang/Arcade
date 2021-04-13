import random

print('\nSelect the following options:', 'rock - ', 'paper - ', 'scissors')

while True: 
	choice = str(input("\nIt is show time, what\'s your choice?: "))
	choice = choice.lower().strip()

	print("\nMy choice is", choice + ".")

	choices = ['rock', 'paper', 'scissors']

	pythonbot_choice = random.choice(choices)

	print("\nPython Bot's choice is", pythonbot_choice + ".")
	if choice in choices:
		if choice == pythonbot_choice:
			print('\nIt seems like a tie.')
		if choice == 'rock':
			if pythonbot_choice == 'paper':
				print('\nYou lose! I\'m invicible haha.')
			elif pythonbot_choice == 'scissors':
				print('\nAlright. You win! Congratulations. Want another go?')
		if choice == 'paper':
			if pythonbot_choice == 'scissors':
				print('\nYou lose! I\'m invicible haha.')
			elif pythonbot_choice == 'rock':
				print('\nAlright. You win! Congratulations. Want another go?')
		if choice == 'scissors':
			if pythonbot_choice == 'rock':
				print('\nYou lose! I\'m invicible haha.' )
			elif pythonbot_choice == 'paper':
				print('\nAlright. You win! Congratulations. Want another go?')
	else:
		print('\nInvalid input. Try again.')

	print()