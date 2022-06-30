#!python3
# 04_image_downloader.py -- input a keyword and automatically download images from https://unsplash.com/
# sys.argv[1] = keyword to search for

import requests
import os
import sys
import bs4
import lxml
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.info('Program start')

def make_photo_dir():
    os.makedirs(f'{sys.argv[1]}', exist_ok=True)

def get_site_html_contents() -> list:
    res = requests.get('https://unsplash.com/s/photos/' + sys.argv[1])
    res.raise_for_status() # crash program if url not valid
    soup = bs4.BeautifulSoup(res.text, "lxml")
    return soup.select('.YVj9w')

def download_images(list_of_image_elements):
    pass


def main():
    make_photo_dir()
    get_site_html_contents()

if __name__ == "__main__":
    main()
