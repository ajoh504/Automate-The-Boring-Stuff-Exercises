#! python3
# 04-madlibs.py -- a Mad Libs game program
# usage: prompt user to enter an adjevtice, noun, adverb, and verb

from pathlib import Path

def madlibs():
    print('-- Welcome to Mad Libs! ---')
    adjective = input('Please enter an adjective:')
    noun1 = input('Please enter a noun:')
    print('Please enter a verb:')
    verb = input()
    noun2 = input('Please enter another noun:')
    madlibs_text = f'''
    The {adjective} panda walked to the
    {noun1} and then {verb}. A nearby {noun2}
    was unaffected by these events.
    '''
    p = open('madlibs.txt', 'w')
    p.write(madlibs_text)
    p.close()
    print(madlibs_text)
    
madlibs()
