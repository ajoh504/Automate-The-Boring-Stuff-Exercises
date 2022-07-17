#!python3
# invitation.py - Open a blank Word document that contains pre-set styles,
#                 and create a list of invitations for different guests. The
#                 guest names are stored in a .txt file.
#
#          USAGE: sys.argv[1] = .txt file containing guest names
#                 sys.argv[2] = blank .docx file with pre-set styles
#                 using Python version 3.8.10 and python-docx version 0.8.10

import sys
import docx

guest_names = sys.argv[1]
blank_docx = sys.argv[2]


def make_invitation(text_file: str, docx_file: str) -> None:
    guests_list = open(text_file).readlines()
    invitation = docx.Document(docx_file)
    for guest in guests_list:
        # todo: write invitation w/ each guest name then save the file
        pass

    
if __name__ == "__main__":
    make_invitation(guest_names, blank_docx)
