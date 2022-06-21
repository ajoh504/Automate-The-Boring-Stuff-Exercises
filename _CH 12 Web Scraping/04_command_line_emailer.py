#!python3
'''
04_command_line_emailer.py -- send emails from the command line
usage: input four command line arguments:
1. sys.argv[1] = email to log into
2. sys.argv[2] = password
3. sys.argv[3] = email body
4. sys.argv[4] = recipient email adddres
'''

from selenium import webdriver
import sys
import re
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

    # todo: open browser session and navigate to email client
    def go_to_email_client(self) -> None:
        EMAIL_CLIENTS = {
            'outlook': 'https://www.outlook.com/',
            'gmail': 'https://www.gmail.com/',
            'yahoo': 'https://yahoomail.com/'
        }
        browser = webdriver.Firefox()
        browser.get(EMAIL_CLIENTS[self.return_email_client()])

    # todo: find username attribute

    # todo: find password attribute

    # todo: log into email client

    # todo: find new message attribute

    # todo: find "to:" attribute and submit sending address

    # todo: find message attribute and submit email body

    # todo: send email


def main():
    command_line_emailer = commandLineEmailer()
    command_line_emailer.go_to_email_client()
    logging.info(command_line_emailer.return_email_client())
    logging.info(str(type(command_line_emailer.return_email_client())))

if __name__ == "__main__":
    main()
