#!python3
# 04_command_line_emailer.py -- send emails from the command line
# usage: input four command line arguments:
# sys.argv[1] = email to log into
# sys.argv[2] = password
# sys.argv[3] = email body
# sys.argv[4] = recipient email address


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import sys
import re

class commandLineEmailer:
    def __init__(self):
        self.browser = webdriver.Firefox()
        self.outlook_method_calls = (
            lambda: self.browser.find_element(By.XPATH, '//*[text()="Sign in"]').click(),
            lambda: self.browser.find_element(By.NAME, 'loginfmt').send_keys(sys.argv[1]),
            lambda: self.browser.find_element(By.ID, "idSIButton9").click(),
            lambda: self.browser.find_element(By.NAME, 'passwd').send_keys(sys.argv[2]),
            lambda: self.browser.find_element(By.ID, "idSIButton9").click(),
            lambda: self.browser.find_element(By.ID, "idBtn_Back").click(),
            lambda: self.browser.find_element(By.XPATH, '//span[text()="New message"]').click(),
            lambda: self.browser.find_element(By.CSS_SELECTOR, "[aria-label='To']").send_keys(sys.argv[4]),
            lambda: self.browser.find_element(By.CSS_SELECTOR, "[aria-label='Message body']").send_keys(sys.argv[3]),
            lambda: self.browser.find_element(By.XPATH, '//*[text()="Send"]').click(),
            lambda: self.browser.find_element(By.ID, "id__183").click()
        )
        self.yahoo_method_calls = (
            lambda: self.browser.find_element(By.CLASS_NAME, 'signin').click(),
            lambda: self.browser.find_element(By.NAME, 'username').send_keys(self.return_email_info()[0]),
            lambda: self.browser.find_element(By.NAME, 'signin').click(),
            lambda: self.browser.find_element(By.NAME, 'password').send_keys(sys.argv[2]),
            lambda: self.browser.find_element(By.NAME, 'verifyPassword').click(),
            lambda: self.browser.find_element(By.CSS_SELECTOR, "[aria-label=Compose]").click(),
            lambda: self.browser.find_element(By.ID, "message-to-field").send_keys(sys.argv[4]),
            lambda: self.browser.find_element(By.CSS_SELECTOR, "[aria-label='Message body']").send_keys(sys.argv[3]),
            lambda: WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[text()="Send"]'))).click()
        )

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
            'yahoo': 'https://yahoomail.com/'
        }
        self.browser.get(EMAIL_CLIENTS[self.return_email_info()[1]])

    def selenium_exception_loop(self, selenium_method_collection) -> None:
        '''
        :param selenium_method_collection: input collection containing selenium
         method calls to search for html elements. Wait two seconds between each
         method call. Except the NoSuchElementException error.
        :return: None
        '''
        for selenium_method_call in selenium_method_collection:
            while True:
                try:
                    self.browser.implicitly_wait(2) # wait two seconds
                    selenium_method_call()
                    break
                except NoSuchElementException:
                    continue

    def sign_in_and_send(self) -> None:
        '''
        Retrieve the email client to log into. Call the selenium_exception_loop()
        function and pass it the email client tuple containing the selenium
        method calls
        :return None:
        '''
        if self.return_email_info()[1] == 'outlook':
            self.selenium_exception_loop(self.outlook_method_calls)
        elif self.return_email_info()[1] == 'yahoo':
            self.selenium_exception_loop(self.yahoo_method_calls)

def main() -> None:
    command_line_emailer = commandLineEmailer()
    command_line_emailer.go_to_email_client()
    command_line_emailer.sign_in_and_send()

if __name__ == "__main__":
    main()
