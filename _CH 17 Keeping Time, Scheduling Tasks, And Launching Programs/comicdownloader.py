#!python3
# comicdownloader.py - Download all webcomics from https://xkcd.com/ and schedule
#                      a daily task to check for the latest comic. If the latest
#                      comic is not in the download directory, then download it.

# todo: write main() logic flow


import os
import lxml
import threading
import bs4
import requests
import subprocess
import logging

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s -  %(levelname)s -  %(message)s"
)
logging.info("Program start")


class XkcdDownloader:
    def __init__(self, comic_num: int):
        self.comic_num = self.get_recent_comic_num

    def get_soup_object(self) -> bs4.BeautifulSoup:
        """
        The urls for XKCD comics contain numbers. Append the comic number to the end of the
        following url: https://xkcd.com/. Then, download and parse the html contents from
        the image webpage at xkcd.com.

        :return: A beautiful soup object containing the html contents of the image webpage.
        """
        print(f"Downloading page https://xkcd.com/{self.comic_num}...")
        res = requests.get(f"https://xkcd.com/{self.comic_num}")
        logging.info("res.text = " + res.text)
        res.raise_for_status()
        return bs4.BeautifulSoup(res.text, "lxml")

    def download_image(self) -> tuple:
        """
        Call get_soup_object() to get the Bs4 object. Use the select() method on the Bs4
        object to retrieve the html image contents and pass it to the variable image_elem.
        Retrieve the image url from image_elem, then download the image into a requests
        object.

        :return tuple: Index 0 of the tuple contains the reqests object. Index 1 contains the
            image url.
        """
        image_elem = self.get_soup_object().select("#comic img")
        # < a
        # rel = "prev"
        # href = "/2649/"
        # accesskey = "p" > & lt;
        # Prev < / a >
        if image_elem == []:
            pass
        else:
            image_url = image_elem[0].get("src")
            print(f"Downloading image from {image_url}")
            res = requests.get(f"https:{image_url}")
            res.raise_for_status()
            return res, image_url

    def save_image(self) -> None:
        """
        Get the requests object and the image_url from self.download_images(). Open a file
        with the image_url basename. Add the comic number to the beginning of the file name,
        save the file, then close it.
        """
        res = self.download_image()[0]  # requests object
        image_url = self.download_image()[1]  # image url
        image_file = open(
            os.path.join("xkcd", f"{self.comic_num}_{os.path.basename(image_url)}"),
            "wb",
        )
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()

    @staticmethod
    def make_bat_file():
        """
        Scheduled task runs from the following file: download_xkcd.bat. Check if download_xkcd.bat
        exists in the current working directory. If it does not exist, create it.
        """
        if not os.path.isfile(f"{os.getcwd()}\\download_xkcd.bat"):
            with open("download_xkcd.bat", "w") as bat_file:
                bat_file.write(f"py.exe {os.getcwd()}\\comicdownloader.py")

    @staticmethod
    def schedule_task():
        """
        Try subprocess.check_output() to see if the scheduled task exists. If it does not exist,
        the CalledProcessError exception will be thrown. In which case, create the scheduled task
        inside the except clause.
        """
        try:
            subprocess.check_output('SCHTASKS /Query /TN "Download XKCD"')
        except subprocess.CalledProcessError:
            subprocess.run(
                f'SCHTASKS /Create /SC DAILY /ST 20:00 /TN "Download XKCD" /TR "{os.getcwd()}\\download_xkcd.bat"'
            )


def main():
    os.makedirs("xkcd", exist_ok=True)  # store comics in ./xkcd
    XkcdDownloader.make_bat_file()  # First checks if .bat file exists
    XkcdDownloader.schedule_task()  # First checks if task exists
    XkcdDownloader(46).save_image()


if __name__ == "__main__":
    main()
