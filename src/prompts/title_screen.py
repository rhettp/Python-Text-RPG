import cmd
import textwrap
import sys
import os
import time
import random
from prompts.game_start import *

##### Title Screen #####
def title_screen():
    os.system('clear')
    print('###################################')
    print('# Welcome to the Python Text RPG! #')
    print('###################################')
    print('1) Play')
    print('2) Help')
    print('3) Quit')
    title_screen_selections()

##### Title Selections #####
def title_screen_selections():
    while True:
        option = input('> ')
        if option == '1':
            start_game()
            break
        elif option == '2':
            help_menu()
            break
        elif option == '3':
            sys.exit()
        else:
            print("Please enter a valid command.")
            continue

##### Help Menu #####
def help_menu():
    print("#############")
    print("# Help Menu #")
    print("#############")
    print("Type left, right, up, or down to move.")
    print("Type examine to investigate the room.")
    print("Type quit to exit the game.")
    print("Have fun!")
    title_screen_selections()
    