#!python3
# invitation.py - Open a blank Word document that contains pre-set styles,
#                 and create a list of invitations for different guests. The
#                 guest names are stored in a .txt file.
#
#          USAGE: sys.argv[1] = .txt file containing guest names
#                 sys.argv[2] = blank .docx file with pre-set styles
#                 using Python version 3.8.10 and python-docx version 0.8.10
# INCOMPLETE -- SEE TODO

import sys
import docx

guest_names = sys.argv[1]
blank_docx = sys.argv[2]


# todo: write function to create paragraphs w/ custom styles
# todo: debug make_invitation() 
def make_invitation(text_file: str, docx_file: str) -> None:
    message = (
        'It would be a pleasure to have the company of',
        '',
        'at 11010 Memory Lane on the Evening of',
        "April 1st",
        'at 7 o\'clock'
    )
    guests_list = open(text_file).readlines()
    doc = docx.Document(docx_file)
    total_paragraphs = len(message) * len(guests_list)
    accumulator = 0
    for i in range(total_paragraphs):
        for guest in guests_list:
            for j, line in enumerate(message):
                if j == 1:
                    doc.paragraphs[i + accumulator].runs[0].text = guest
                else:
                    doc.paragraphs[i + accumulator].runs[0].text = line
            doc.paragraphs[4].runs[0].add_break(docx.enum.text.WD_BREAK.PAGE)
            accumulator += j
    doc.save('invitations.docx')


if __name__ == "__main__":
    make_invitation(guest_names, blank_docx)


