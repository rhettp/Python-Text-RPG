import sys
import os
from prompts.game_start import *
from gameplay.save_load_game import *
from prompts.clear_console import *

##### Title Screen #####
def title_screen():
    clearConsole()
    print('\n###################################')
    print('# Welcome to the Python Text RPG! #')
    print('###################################')
    print('1) Start Game')
    print('2) Load Game')
    print('3) Quit')
    title_screen_selections()

##### Title Selections #####
def title_screen_selections():
    while True:
        option = input('> ')
        # Start game
        if option == '1':       
            if os.path.exists('saved_game_file'):       # Saved game file exists
                print("This will overwrite your saved game.")
                print("Do you want to continue?")
                while True:
                    option = input('> ')
                    if option in ["yes","Yes", "YES", "accept","Accept","ACCEPT"]:  # Continue
                        start_game()
                        break
                    elif option in ["no","No","NO","back","Back","BACK"]:           # Go back
                        title_screen()
                        break
                    else:                                                           # Input Validation
                        print("Please enter a valid command.")
                        continue
            else:                                       # No saved game file
                start_game()
                break

        # Load Game
        elif option == '2':
            if os.path.exists('saved_game_file'):       # Load saved game file if it exists
                load_game()
                break
            else:                                       # No saved game file
                print("No saved game file exists.")
                continue
        elif option == '3':
            sys.exit()
        else:                                           # Input Validation
            print("Please enter a valid command.")
            continue
        break


