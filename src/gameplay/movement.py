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
    time.sleep(1)

# Player move location
def player_move():
    print("Where would you like to travel to?")
    print("1) Town")
    print("2) Castle")
    print("3) Forest")
    print("4) Mine")
    print("5) Dragon's Lair")
    print("6) Back")    # Go back a menu

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
            if myPlayer.location == "Castle":
                print("You are already here.")
                continue
            else:
                myPlayer.location = "Castle"
                break
        elif destination == "3":
            if myPlayer.location == "Forest":
                print("You are already here.")
                continue
            else:
                myPlayer.location = "Forest"
                break
        elif destination == "4":
            if myPlayer.location == "Mine":
                print("You are already here.")
                continue
            else:
                myPlayer.location = "Mine"
                break
        elif destination == "5":
            if myPlayer.location == "Dragon's Lair":
                print("You are already here.")
                continue
            else:
                myPlayer.location = "Dragon's Lair"
                break
        elif destination == "6":    # Go back a menu
            break
        else:
            print("Please enter a valid location.")
            continue

# Player move to shop
def player_shop():
    print("Where would you like to shop?")
    print("1) Blacksmith")
    print("2) Magic Shop")
    print("3) General Store")
    print("4) Back")    # Go back a menu

    while True:
        destination = input('> ')
        if destination == '1':
            myPlayer.location = "Blacksmith"
            break
        elif destination == '2':
            myPlayer.location = "Magic Shop"
            break
        elif destination == '3':
            myPlayer.location = "General Store"
            break
        elif destination == '4':    # Go back a menu
            break
        else:
            print("Please enter a valid shop.")
            continue