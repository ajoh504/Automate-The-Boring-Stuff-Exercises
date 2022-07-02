#!python3
# 04_image_downloader.py -- input a keyword and automatically download images from https://unsplash.com/
# sys.argv[1] = keyword to search for

import requests
import os
import sys
import bs4
import lxml


class imageDownloader:
    def __init__(self):
        self.keyword = sys.argv[1] # keyword to search for photos
        self.photo_site_url = 'https://unsplash.com/s/photos/' # link is invalid if keyword is not appended
        self.image_css_class = 'YVj9w'

    def parse_site_html_contents(self) -> bs4.element.ResultSet:
        res = requests.get(self.photo_site_url + self.keyword)
        res.raise_for_status() # crash program if url not valid
        return bs4.BeautifulSoup(res.text, "lxml").select('.' + self.image_css_class)

    def download_images(self) -> None:
        '''
        create dir to store photos using search keyword as the name. iterate over
        beautiful soup result set. use 'src' to pass url into image_url
        variable. use raise_for_status() to crash the program if url is not valid.
        except the MissingSchema exception. download photos into dir with the keyword +
        the index as the filename, + '.jpeg' as the file type.
        '''
        os.makedirs(self.keyword, exist_ok=True)  # make dir to store photos
        for index, url in enumerate(self.parse_site_html_contents()):
            image_url = url.get('src')
            try:
                res = requests.get(image_url)
                res.raise_for_status()
            except requests.exceptions.MissingSchema:
                continue
            image_file = open(os.path.join(self.keyword + '\\' + self.keyword + str(index) + '.jpeg'),'wb')
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()


def main():
    image_downloader = imageDownloader()
    image_downloader.download_images()

if __name__ == "__main__":
    main()
