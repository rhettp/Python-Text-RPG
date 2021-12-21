import os
import time
from prompts import *
from player_movement import *

def main_game_loop():
    while True:
        os.system('clear')
        print_location()
        town_prompt()