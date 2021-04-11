import random 
# Create strings with all possible characters that we can use for the passwords. 
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower() # Use uppercase function with the string function here. 
digits = "0123456789"
symbols = "()[]{},:;=+-/\\!£$%&*? "
# Select Boolean for things we want to select in the password. 
upper, lower, nums, syms = True, True, True, True # Change your preferences in password content. (Change to false to remove either one)
# Create string for final password. 
all = ""
# Create string with the things we're going to use. 
if upper:
    all += uppercase_letters # if we choose to use uppercase_letters we're going to include it into the final string. 
if lower:
    all += lowercase_letters # if we choose to use lowercase letters. 
if nums:
    all += digits # If we choose digits 
if syms:
    all += symbols # If we choose symbols. 
length = 10 #Set length to whatever we wanted in password. 
amount = 5 # set the amount of passwords that one generates 
# Now we can get into the actual generation, after we've chosen what characters we want to use, the length of the password, and the amount that one generates. 
for x in range(amount):
    password = "".join(random.sample(all, length))  
    print(password)
# join on empty string. (random.sample) takes anything out of full string that we have.
# We're using 'all' string to complete string with all the characters that we're using . 
# And we define this string length to be 10.