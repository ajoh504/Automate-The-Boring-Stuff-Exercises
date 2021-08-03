# This program finds out how often a streak of
# six heads or six tails comes up in a randomly
# generated list of heads and tails. The program
# makes a list of 100 random coin streaks. Then,
# the program repeats 10000 times.

import random
for experimentNumber in range(10000):
    numberOfStreaks = 0
    # Code that creates a list of 100 'heads' or 'tails' values.
    hundredFlips = []
    for i in range(0, 100):
        if random.randint(0,1) == 0:
            hundredFlips.append('h')
        else:
            hundredFlips.append('t')
    # Code that checks if there is a streak of 6 heads or tails in a row.
    # sixStreak will count the number of streaks in a row.
    # If sixStreak == 6 at the end of the streak, add 1 to numberOfStreaks.
    # If not, then reset sixStreak to 0.
    sixStreak = 0
    for i in range (len(hundredFlips)):
        if i == 0:
            pass
        if hundredFlips[i] == hundredFlips[i-1]:
            sixStreak += 1
        else:
            if sixStreak == 6:
                numberOfStreaks += 1
            else:
                sixStreak = 0
    print('Chance of streak: %s%%' % (numberOfStreaks / 100))

