import cmd
import textwrap
import sys
import os
import time
import random

##### Title Screen #####
def title_screen():
    os.system('clear')
    print('###################################')
    print('# Welcome to the Python Text RPG! #')
    print('###################################')
    print('-Play-')
    print('-Help-')
    print('-Quit-')
    title_screen_selections()

##### Title Selections #####
def title_screen_selections():
    while True:
        option = input('> ').lower()
        if option == 'play':
            #TODO
            print("Play")
            #start_game()
            break
        elif option == 'help':
            help_menu()
            break
        elif option == 'quit':
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