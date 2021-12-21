import os
import time
from prompts import *
from player_movement import *

def main_game_loop():
    while True:
        os.system('clear')
        print_location()
        time.sleep(1)
        prompt()