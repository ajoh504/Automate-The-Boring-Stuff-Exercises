# This program finds out how often a streak of
# six heads or six tails comes up in a randomly
# generated list of heads and tails. The program
# makes a list of 100 random coin streaks. Then,
# the program repeats 10000 times.

import random
for experiment_number in range(10000):
    number_of_streaks = 0
    # Code that creates a list of 100 'heads' or 'tails' values.
    hundred_flips = []
    for i in range(0, 100):
        if random.randint(0,1) == 0:
            hundred_flips.append('h')
        else:
            hundred_flips.append('t')
    # Code that checks if there is a streak of 6 heads or tails in a row.
    # six_streak will count the number of streaks in a row.
    # If six_streak == 6 at the end of the streak, add 1 to number_of_streaks.
    # If not, then reset six_streak to 0.
    six_streak = 0
    for i in range (len(hundred_flips)):
        if i == 0:
            pass
        if hundred_flips[i] == hundred_flips[i-1]:
            six_streak += 1
        else:
            if six_streak == 6:
                number_of_streaks += 1
            else:
                six_streak = 0
    print('Chance of streak: %s%%' % (number_of_streaks / 100))

