import sys
import os
import time
from player import *
from game_loop import *

##### New Game Start #####
def start_game():
    os.system('clear')
    question = "What is your name?\n"
    for character in question:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    myPlayer.name = input("> ")

    # Introduction
    intro1 = "Welcome to the land of Requiem {}!\n".format(myPlayer.name)
    intro2 = "Here you will fight monsters, level up skills, and complete quests.\n"
    intro3 = "But it is up to you on how you do it!\n"
    intro4 = "Have fun and be careful!\n"

    for character in intro1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in intro2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in intro3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in intro4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(2)

    os.system("clear")
    print("#################")
    print("# Let us Begin! #")
    print("#################")
    time.sleep(1)
    intro5 = "\nYou arrive in the bustling city of Myrefall\n"
    for character in intro5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1)
    main_game_loop()