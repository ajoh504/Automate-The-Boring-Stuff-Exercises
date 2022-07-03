#!python3
# 06_2048.py -- game bot to automatically play the game 2048
# game url: https://play2048.co/

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import random


class gameBot2048:
    def __init__(game):
        game.browser = webdriver.Firefox()
        game.moves = (
            Keys.ARROW_UP,
            Keys.ARROW_DOWN,
            Keys.ARROW_LEFT,
            Keys.ARROW_RIGHT
        )

    def game_not_over(game) -> bool:
        '''
        :return bool: if "Game over!" text is displayed on screen, return False. Otherwise,
        return True.
        '''
        try:
            game_over_text = game.browser.find_element(By.XPATH, '//*[text()="Game over!"]')
            if game_over_text.is_displayed():
                return False
        except NoSuchElementException:
            return True


    def play_game(game):
        game.browser.get('https://play2048.co/')
        while game.game_not_over():
            game.browser.implicitly_wait(1) # wait 1 second between each turn
            x = random.randint(0, 3)
            game.browser.find_element(By.CSS_SELECTOR, 'html').send_keys(game.moves[x])


def main():
    current_game = gameBot2048()
    current_game.play_game()

if __name__ == "__main__":
    main()
