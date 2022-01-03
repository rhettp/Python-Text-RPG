import cmd
import textwrap
import sys
import os
import time
from character.player import *
from gameplay.inventory import *

##### Woodcutting #####

# Woodcutting prompt
def woodcutting_prompt():
    print("What type of tree do you want to cut down?")
    print("1) Oak Tree")
    print("2) Willow Tree")
    print("3) Maple Tree")
    print("4) Yew Tree")
    print("5) Magic Tree")
    print("6) Display Inventory")
    print("7) Back")
    while True:
        action = input('> ')
        if action == '1':       # Oak tree
            os.system('clear')
            print("\n###########")
            print("Woodcutting")
            print("###########\n")
            woodcut("Oak Log")
            myPlayer.display_stats()
            woodcutting_prompt()
            break
        elif action == '2':     # Willow tree
            os.system('clear')
            print("\n###########")
            print("Woodcutting")
            print("###########\n")
            woodcut("Willow Log")
            myPlayer.display_stats()
            woodcutting_prompt()
            break
        elif action == '3':     # Maple tree
            os.system('clear')
            print("\n###########")
            print("Woodcutting")
            print("###########\n")
            woodcut("Maple Log")
            myPlayer.display_stats()
            woodcutting_prompt()
            break
        elif action == '4':     # Yew tree
            os.system('clear')
            print("\n###########")
            print("Woodcutting")
            print("###########\n")
            woodcut("Yew Log")
            myPlayer.display_stats()
            woodcutting_prompt()
            break
        elif action == '5':     # Magic tree
            os.system('clear')
            print("\n###########")
            print("Woodcutting")
            print("###########\n")
            woodcut("Magic Log")
            myPlayer.display_stats()
            woodcutting_prompt()
            break
        elif action == '6':     # Inventory
            os.system('clear')
            print("\n###########")
            print("Woodcutting")
            print("###########\n")
            showIventory()
            print("\n")
            myPlayer.display_stats()
            woodcutting_prompt()
            break
        elif action == '7':     # Back
            print("back")
        else:                   # Input Validation
            print("Please enter a valid tree.")
            continue

# Woodcutting function
def woodcut(log):
    if log == "Oak Log":
        print("You swing your axe at the Oak Tree...")
        addToInventory("Oak Log")
        print("You reveive an Oak Log!\n")
    elif log == "Willow Log":
        print("You swing your axe at the Willow Tree...")
        addToInventory("Willow Log")
        print("You reveive a Willow Log!\n")
    elif log == "Maple Log":
        print("You swing your axe at the Maple Tree...")
        addToInventory("Maple Log")
        print("You reveive a Maple Log!\n")
    elif log == "Yew Log":
        print("You swing your axe at the Yew Tree...")
        addToInventory("Yew Log")
        print("You reveive a Yew Log!\n")
    elif log == "Magic Log":
        print("You swing your axe at the Magic Tree...")
        addToInventory("Magic Log")
        print("You reveive a Magic Log!\n")