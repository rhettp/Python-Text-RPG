from prompts.prompts import *
from gameplay.movement import *
from prompts.clear_console import *

def main_game_loop():
    while True:
        clearConsole()
        print_location()
        prompt_choice()
