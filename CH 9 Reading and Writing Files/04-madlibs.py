#! python3
# 04-madlibs.py -- a Mad Libs game program
# usage: prompt user to enter an adjevtice, noun, adverb, and verb

from pathlib import Path

def madlibs(adj: str, noun1: str, verb: str, noun2: str) -> str:

    MADLIBS_TEMPLATE = f'''
    The {adjective} panda walked to the
    {noun1} and then {verb}. A nearby {noun2}
    was unaffected by these events.
    '''
    p = Path.open('madlibs.txt', 'w')
