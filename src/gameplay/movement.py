import cmd
import textwrap
import sys
import os
import time
import random
from character.player import *
from world.world_map import*

##### Player Movement #####

# Print current player location
def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('# {} #'.format(myPlayer.location))
    print('#' * (4 + len(myPlayer.location)))
    print('\n')

# Player move location
def player_move():
    print("Where would you like to travel to?")
    print("1) Town")
    print("2) Forest")
    print("3) Mine")
    print("4) Swamp")
    print("5) Graveyard")
    print("6) Dragon's Lair")
    print("7) Back")    # Go back a menu

    while True:
        destination = input('> ')
        if destination == "1":
            if myPlayer.location == "Town":
                print("You are already here.")
                continue
            else:
                myPlayer.location = "Town"
                break
        elif destination == "2":
            if myPlayer.location == "Forest":
                print("You are already here.")
                continue
            else:
                myPlayer.location = "Forest"
                break
        elif destination == "3":
            if myPlayer.location == "Mine":
                print("You are already here.")
                continue
            else:
                myPlayer.location = "Mine"
                break
        elif destination == "4":
            if myPlayer.location == "Swamp":
                print("You are already here.")
                continue
            else:
                myPlayer.location = "Swamp"
                break
        elif destination == "5":
            if myPlayer.location == "Graveyard":
                print("You are already here.")
                continue
            else:
                myPlayer.location = "Graveyard"
                break
        elif destination == "6":
            if myPlayer.location == "Dragon's Lair":
                print("You are already here.")
                continue
            else:
                myPlayer.location = "Dragon's Lair"
                break
        elif destination == "7":    # Go back a menu
            break
        else:
            print("Please enter a valid location.")
            continue