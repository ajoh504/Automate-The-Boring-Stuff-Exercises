#!python3
# 07_link_verification.py -- input url to find all broken links on the page
# final function prints a list of broken links
# sys.argv[1] = url to check

import sys
import requests
import bs4
import lxml
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.info('Program start')

class linkVerification:
    def __init__(self):
        self.url = sys.argv[1]
        self.css_selector = ''
        self.download_webpage = lambda: requests.get(self.url)

    def get_soup_object(self) -> bs4.BeautifulSoup:
        res = self.download_webpage()
        res.raise_for_status() # crash program if url not valid
        return bs4.BeautifulSoup(res.text, 'lxml')

    # todo: finish func
    def get_html_status_code(self) -> str:
        soup = self.get_soup_object()
        logging.info(soup.findall('a'))

def main():
    link_verification = linkVerification()
    link_verification.get_html_status_code()

if __name__ == "__main__":
    main()
