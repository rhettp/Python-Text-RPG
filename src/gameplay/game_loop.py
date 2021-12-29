import os
import time
from prompts.prompts import *
from gameplay.movement import *

def main_game_loop():
    while True:
        os.system('clear')
        print_location()
        prompt_choice()