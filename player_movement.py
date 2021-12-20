import cmd
import textwrap
import sys
import os
import time
import random
from player import *
from world_map import*

def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('# {} #'.format(myPlayer.location))
    print('# {} #'.format(world_zone[myPlayer.location][DESCRIPTION]))
    print('#' * (4 + len(myPlayer.location)))

def player_move(action):
    print("Where would you like to travel to?")

    while True:
        destination = input('> ').lower()
        if destination == "blacksmith":
            myPlayer.location = "Blacksmith"
            break
        elif destination == "town":
            myPlayer.location = "Town"
            break
        elif destination == "general store":
            myPlayer.location = "General Store"
            break
        elif destination == "castle":
            myPlayer.location = "Castle"
            break
        elif destination == "forest":
            myPlayer.location = "Forest"
            break
        elif destination == "mine":
            myPlayer.location = "Mine"
            break
        elif destination == "dragon's lair":
            myPlayer.location = "Dragon's Lair"
            break
        else:
            print("Please enter a valid location.")
            continue