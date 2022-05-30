# use debugging tools to fix the bugs 

import random
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('Start of the program')

guess = ''
while guess not in ('heads', 'tails'):
    guess = input('Guess the coin toss! Enter heads or tails:\n')

toss = random.randint(0, 1) # 0 is tails, 1 is heads
logging.debug('toss is ' + str(toss) + ' and guess is ' + guess)

if (toss == 0 and guess == 'tails') or (toss == 1 and guess == 'heads'):
    print('You got it!')
else:
    guess = input('Nope! Guess again!\n')
    if (toss == 0 and guess == 'tails') or (toss == 1 and guess == 'heads'):
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

logging.debug('End of the program')
