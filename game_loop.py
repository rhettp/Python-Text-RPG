import os
import time
from prompts import *
from player_movement import *

def main_game_loop():
    while True:
        os.system('clear')
        print_location()
        if myPlayer.location == "Town":
            town_prompt()
        elif myPlayer.location in ["Blacksmith", "Magic Shop", "General Store"]:
            shop_prompt()