# this is a guess the number game
# this game uses the random module to generate a 
# random number for the user to attempt to guess
# the for loop only repeats six times, so the user
# only has six tries to guess the number

import random
secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')
# Ask the player to guess 6 times
for guessesTaken in range (1,7):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # the condition is the correct guess!
if guess == secretNumber:
    print('Good job! You guessed me number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope, the number I was thinking of was ' + str(secretNumber))
