#!python3
# 07_link_verification.py -- input url to find all broken links on the page
# final function prints a list of broken links
# sys.argv[1] = url to check

import sys
import requests
import bs4
import lxml


class linkVerification:
    def __init__(self):
        self.url = sys.argv[1]
        self.download_webpage = lambda: requests.get(self.url)

    def get_soup_object(self) -> bs4.BeautifulSoup:
        res = self.download_webpage()
        res.raise_for_status() # crash program if url not valid
        return bs4.BeautifulSoup(res.text, 'lxml')

    def get_url_list(self) -> list:
        '''
        create beautiful soup object from self.get_soup_object() function call.
        :return: use list comprehension to search the beautiful soup result set for
        any items with the html anchor element. Then return a list of items with the
        href attribute.
        '''
        soup = self.get_soup_object()
        return [url.get('href') for url in soup.find_all('a')]


    def print_broken_links(self) -> None:
        '''
        call self.get_url_list() to loop through items with the href attribute. 
        try to download the items. Except MissingSchema if link is invalid. If 
        link is valid and status_code returns an error, print the link and the
        status code. 
        '''
        for string in self.get_url_list():
            try:
                res = requests.get(string)
                if res.status_code != requests.codes.ok:
                    print(res, string)
            except requests.exceptions.MissingSchema: # skip non-link strings
                continue

def main():
    link_verification = linkVerification()
    link_verification.print_broken_links()

if __name__ == "__main__":
    main()
