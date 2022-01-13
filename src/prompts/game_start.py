import sys
from prompts.clear_console import *
import time
from character.player import *
from gameplay.game_loop import *

##### New Game Start #####
def start_game():
    clearConsole()
    question = "What is your name?\n"
    for character in question:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    myPlayer.name = input("> ")

    # Introduction
    intro1 = "Welcome to the land of Requiem {}!\n".format(myPlayer.name)
    intro2 = ("Here you will fight monsters, level up skills, and complete quests.\n"
              "But it is up to you on how you do it!\n"
              "Have fun and be careful!\n")
    for character in intro1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in intro2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(2)

    clearConsole()
    print("\n#################")
    print("# Let us Begin! #")
    print("#################")
    time.sleep(1)
    intro3 = "\nYou arrive in the bustling city of Myrefall"
    for character in intro3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    periods = "....."
    for character in periods:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.6)
    main_game_loop()
