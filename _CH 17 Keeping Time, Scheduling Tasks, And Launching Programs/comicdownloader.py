#!python3
# comicdownloader.py - Download all webcomics from https://xkcd.com/ and schedule
#                      a daily task to check for the latest comic. If the latest
#                      comic is not in the download directory, then download it.

# todo: write ScriptConfig class functions
# todo: write main() logic flow
# todo: check if comics have been downloaded previously?
# todo: edit docstrings for clarity


import os
import lxml
import threading
import bs4
import requests
import logging

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s -  %(levelname)s -  %(message)s"
)
logging.info("Program start")


class ScriptConfig:
    def __init__(self):
        pass

    def make_bat_file(self):
        """
        Scheduled task runs from the file download_xkcd.bat. Check if .bat file exists
        in the current working directory. If not, create it.
        """
        if not os.path.isfile(f"{os.getcwd()}\\download_xkcd.bat"):
            with open("download_xkcd.bat", "w") as bat_file:
                bat_file.write(f"py.exe {os.getcwd()}\\comicdownloader.py")

    def schedule_task(self):
        """Check to see if scheduled task exists. If not, create it."""
        os.system(
            f'SCHTASKS /Create /SC DAILY /ST 20:00 /TN "Download XKCD" /TR "{os.getcwd()}\\download_xkcd.bat"'
        )
        # SCHTASKS /Create /SC DAILY /ST 20:00 /TN "Download XKCD" /TR "CWD\download_xkcd.bat"


class XkcdDownloader:
    def __init__(self, comic_num: int):
        self.comic_num = comic_num

    def get_soup_object(self) -> bs4.BeautifulSoup:
        """Given a comic number, download and parse its html contents from xkcd.com."""
        print(f"Downloading page https://xkcd.com/{self.comic_num}...")
        res = requests.get(f"https://xkcd.com/{self.comic_num}")
        res.raise_for_status()
        return bs4.BeautifulSoup(res.text, "lxml")

    def download_image(self) -> tuple:
        """
        Get the image url from the comic element tag, then download the image.

        :return tuple: Index 0 contains the reqests object. Index 1 contains the
            image url.
        """
        comic_elem = self.get_soup_object().select("#comic img")
        if comic_elem == []:
            pass
        else:
            image_url = comic_elem[0].get("src")
            print(f"Downloading image from {image_url}")
            res = requests.get(f"https:{image_url}")
            res.raise_for_status()
            return res, image_url

    def save_image(self) -> None:
        """
        Get the requests object and the image_url from self.download_images(). Open
        a file with the image_url basename, save the file, then close it.
        """
        res = self.download_image()[0]
        image_url = self.download_image()[1]
        image_file = open(os.path.join("xkcd", os.path.basename(image_url)), "wb")
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()


def main():
    os.makedirs("xkcd", exist_ok=True)  # store comics in ./xkcd
    ScriptConfig().make_bat_file()  # First checks if .bat file exists
    ScriptConfig().schedule_task()  # First checks if task exists
    # XkcdDownloader(46).download_image()


if __name__ == "__main__":
    main()
