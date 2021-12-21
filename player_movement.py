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
    print('#' * (4 + len(myPlayer.location)))

def player_move():
    print("Where would you like to travel to?")
    print("1) Town")
    print("2) Blacksmith")
    print("3) General Store")
    print("4) Castle")
    print("5) Forest")
    print("6) Mine")
    print("7) Dragon's Lair")
    print("8) Back")

    while True:
        destination = input('> ')
        if destination == "1":
            myPlayer.location = "Town"
            break
        elif destination == "2":
            myPlayer.location = "Blacksmith"
            break
        elif destination == "3":
            myPlayer.location = "General Store"
            break
        elif destination == "4":
            myPlayer.location = "Castle"
            break
        elif destination == "5":
            myPlayer.location = "Forest"
            break
        elif destination == "6":
            myPlayer.location = "Mine"
            break
        elif destination == "7":
            myPlayer.location = "Dragon's Lair"
            break
        elif destination == "8":
            break
        else:
            print("Please enter a valid location.")
            continue