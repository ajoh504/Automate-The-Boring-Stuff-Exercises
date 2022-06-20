#!python3
''' 
04_command_line_emailer.py -- send emails from the command line
usage: input four command line arguments:
1. email to log into = sys.argv[1]
2. password = sys.argv[2]
3. email body = sys.argv[3]
4. recipient email adddress = sys.argv[4]
'''

import sys
import re
import selenium
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.info('Program start')

class commandLineEmailer:
    def __init__(self):
        pass

    # todo: return the name of the email client for the sending address
    def return_email_client(self) -> str:
        '''
        pass sending email into regex (sys.argv[1])
        regex pattern creates three groups:
        group 1 stops at "@"
        group 2 finds the email client name
        group 3 begins at "."
        :return: name of email client from regex group 2
        '''
        return re.compile("(.*\@)(.*)(\.)").match(sys.argv[1]).group(2)

    # todo: open Firefox session

    # todo: log into email client

    # todo:
    
def main():
    command_line_emailer = commandLineEmailer()
    logging.info(command_line_emailer.return_email_client())
    logging.info(str(type(command_line_emailer.return_email_client())))
    
if __name__ == "__main__":
    main()
