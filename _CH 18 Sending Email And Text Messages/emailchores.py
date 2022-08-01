#!python3
# emailchores.py - Scan a list of chores and a list of email addresses then
#                  randomly assign chores to people via email. Track recent
#                  chores so that the same chore is not assigned teh following
#                  week. Schedule the script to run once per week.
#
#           Usage: emails.txt = emails separated by newline characters
#                  chores.txt = chores separated by newline characters
#                  Store both .txt files in emailchores.py directory.


# todo: func to return .txt file contents
def get_text_contents(text_file) -> list:
    """
    :return: A list of the contents of a plain text file. File contents should be
        separated by newline characters.
    """
    with open(text_file, 'r') as f: 
        return f

# todo: func to choose random items

# todo: func to store last week's chore assignment

# todo: review how to schedule tasks properly


def main():
    emails = 'emails.txt'
    chores = 'chores.txt'
    get_text_contents(emails)


if __name__ == "__main__":
    main()
