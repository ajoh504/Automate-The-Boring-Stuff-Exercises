#!python3
# 04_command_line_emailer.py -- send emails from the command line
# usage: input four command line arguments:
# 1. sys.argv[1] = email to log into
# 2. sys.argv[2] = password
# 3. sys.argv[3] = email body
# 4. sys.argv[4] = recipient email address


from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import re
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.info('Program start')

class commandLineEmailer:
    def __init__(self):
        pass

    # return the name of the email client for the sending address
    # todo: only return necessary data
    def return_email_info(self) -> tuple:
        '''
        Input sys.argv[1] into regex. sys.argv[1] contains the sending email
        address. The regex pattern creates four groups: group at index 0 
        contains username, group at index 2 contains email client name
        
        :return: email address separated into tuple
        '''
        return re.compile("(.*)(\@)(.*)(\.)").match(sys.argv[1]).groups()

    # open browser session and navigate to email client
    def go_to_email_client(self) -> None:
        EMAIL_CLIENTS = {
            'outlook': 'https://www.outlook.com/',
            'gmail': 'https://www.gmail.com/',
            'yahoo': 'https://yahoomail.com/'
        }
        browser = webdriver.Firefox()
        browser.get(EMAIL_CLIENTS[self.return_email_client()[2]])

    # sign into email client and input username / password
    def sign_in(self):
        if self.return_email_client() == 'yahoo':
            browser.find_element(By.CLASS_NAME, 'signin').click()
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
