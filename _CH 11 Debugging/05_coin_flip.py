# use to test breakpoints. Set a breakpoint at the first print function to see the value of 
# heads at the halfway point

import random
heads = 0
for i in range(1, 1001):
    if random.randint(0, 1) == 1:
        heads = heads + 1
    if i == 500:
        print('Halfway done!')
print('Heads came up ' + str(heads) + ' times.')