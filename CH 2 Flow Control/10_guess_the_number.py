# this is a guess the number game
# this game uses the random module to generate a 
# random number for the user to attempt to guess
# the for loop only repeats six times, so the user
# only has six tries to guess the number

import random
secret_number = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')
# Ask the player to guess 6 times
for guesses_taken in range (1,7):
    print('Take a guess.')
    guess = int(input())
    if guess < secret_number:
        print('Your guess is too low.')
    elif guess > secret_number:
        print('Your guess is too high.')
    else:
        break # the condition is the correct guess!
if guess == secret_number:
    print('Good job! You guessed me number in ' + str(guesses_taken) + ' guesses!')
else:
    print('Nope, the number I was thinking of was ' + str(secret_number))
