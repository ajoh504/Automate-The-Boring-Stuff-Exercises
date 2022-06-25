#!python3
# 04_command_line_emailer.py -- send emails from the command line
# usage: input four command line arguments:
# sys.argv[1] = email to log into
# sys.argv[2] = password
# sys.argv[3] = email body
# sys.argv[4] = recipient email address


from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import re
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.info('Program start')


class commandLineEmailer:
    def __init__(self):
        self.browser = webdriver.Firefox()

    def return_email_info(self) -> tuple:
        '''
        Input sys.argv[1] into regex. sys.argv[1] contains the sending email
        address. return the username and the email client name.

        :return: tuple, username at index 0, email client name at index 1
        '''
        return re.compile("(.*)(\@)(.*)(\.)").match(sys.argv[1]).group(1), \
               re.compile("(.*)(\@)(.*)(\.)").match(sys.argv[1]).group(3)

    # open browser session and navigate to email client
    def go_to_email_client(self) -> None:
        EMAIL_CLIENTS = {
            'outlook': 'https://www.outlook.com/',
            'gmail': 'https://www.gmail.com/',
            'yahoo': 'https://yahoomail.com/'
        }
        self.browser.get(EMAIL_CLIENTS[self.return_email_info()[1]])

    def sign_into_gmail(self) -> None:
        pass

    def sign_into_outlook(self) -> None:
        pass

    def sign_into_yahoo(self) -> None: # yahoomail signin method
        self.browser.find_element(By.CLASS_NAME, 'signin').click()
        self.browser.find_element(By.NAME, 'username').send_keys(self.return_email_info()[0])
        self.browser.find_element(By.NAME, 'signin').click()
        self.browser.find_element(By.NAME, 'password').send_keys(sys.argv[2])
        self.browser.find_element(By.NAME, 'verifyPassword').click()

    # sign into email client and input username / password
    def sign_in(self) -> None:
        if self.return_email_info()[1] == 'gmail':
            self.sign_into_gmail()
        elif self.return_email_info()[1] == 'outlook':
            self.sign_into_outlook()
        elif self.return_email_info()[1] == 'yahoo':
            self.sign_into_yahoo()

    def send_from_gmail(self) -> None:
        pass

    def send_from_outlook(self) -> None:
        pass

    # todo: find new message attribute
    def send_from_yahoo(self) -> None:
        self.browser.find_element(By.CSS_SELECTOR, '/d/compose/').click()

    # todo: find "to:" attribute and submit sending address

    # todo: find message attribute and submit email body

    # todo: send email
    def send_email(self) -> None:
        if self.return_email_info()[1] == 'gmail':
            self.send_from_gmail()
        elif self.return_email_info()[1] == 'outlook':
            self.send_from_outlook()
        elif self.return_email_info()[1] == 'yahoo':
            self.send_from_yahoo()

def main() -> None:
    command_line_emailer = commandLineEmailer()
    command_line_emailer.go_to_email_client()
    command_line_emailer.sign_in()
    command_line_emailer.send_email()

if __name__ == "__main__":
    main()
