#!python3
# 06_2048.py -- game bot to automatically play the game 2048
# game url: https://play2048.co/

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import random
import time
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.info('Program start')

class gameBot2048:
    def __init__(game):
        game.browser = webdriver.Firefox()
        game.moves = (
            Keys.ARROW_UP,
            Keys.ARROW_DOWN,
            Keys.ARROW_LEFT,
            Keys.ARROW_RIGHT
        )


    def play_game(game):
        game.browser.get('https://play2048.co/')
        while True:
            time.sleep(1)
            x = random.randint(0, 3)
            game.browser.find_element(By.CSS_SELECTOR, 'html').send_keys(game.moves[x])


def main():
    current_game = gameBot2048()
    current_game.play_game()

if __name__ == "__main__":
    main()

'''
<div class="game-message game-over"><p>Game over!</p><div class="lower"><a class="keep-playing-button">Keep going</a>
<a class="retry-button">Try again</a></div></div>

'''


