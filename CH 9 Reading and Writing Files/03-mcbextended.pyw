#! python3
# mcb.pyw -- Saves and loads pieces of text to the clipboard
# Usage: py.exe 03-mcbextended.pyw save <keyword> - Saves clipboard to keyword
#        py.exe 03-mcbextended.pyw <keyword> - Loads keyword to clipboard
#        py.exe 03-mcbextended.pyw list - Loads all keywords to clipboard
#        py.exe 03-mcbextended.pyw delete <keyword> - deletes keyword
#        py.exe 03-mcbextended.pyw reset - deletes all keywords

import shelve, pyperclip, sys

mcb_shelf = shelve.open('mcb')

# save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
# delete specified keyword
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcb_shelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # list keywords in clipboard
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    # load content to clipboard
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])
    # delete all keywords
    elif sys.argv[1].lower() == 'reset':
        mcb_shelf.clear()

mcb_shelf.close()
