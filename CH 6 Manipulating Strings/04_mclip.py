#! python3
# 04_myclip.py - A multi-clipboard program.
# Use Win+R to run the mclip file with the associated keyphrase

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?""",}
import sys, pyperclip
# Ensure user does not forget to add command line arg:
if len(sys.argv) < 2: 
    print('Argument: keyphrase missing. Usage: python 04_mclip.py [keyphrase] - copy phrase text')
    sys.exit()
keyphrase = sys.argv[1] #first command line arg is the keyphrase
keyphrase

# if keyphrase is stored as key in TEXT, copy value using .copy() method
if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)
