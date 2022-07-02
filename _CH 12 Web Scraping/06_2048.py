#!python3
# 06_2048.py -- game bot to automatically play the game 2048
# game url: https://play2048.co/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.info('Program start')

class gameBot2048:
    def __init__(game):
        game.grid_state = {
            '1x1': '', '1x2': '', '1x3': '', '1x4': '',
            '2x1': '', '2x2': '', '2x3': '', '2x4': '',
            '3x1': '', '3x2': '', '3x3': '', '3x4': '',
            '4x1': '', '4x2': '', '4x3': '', '4x4': ''
        }

    def get_current_grid(game):
        pass
    
    def take_next_move(game):
        pass

def main():
    current_game = gameBot2048()

if __name__ == "__main__":
    main()
