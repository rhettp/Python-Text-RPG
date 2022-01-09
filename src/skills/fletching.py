import cmd
import textwrap
import sys
import os
import time
from character.player import *
from gameplay.inventory import *

##### Fletching #####

# Fletching prompt
def fletching_prompt():
    print("What bow would you like to make?")
    print("1) Oak Bow")
    print("2) Willow Bow")
    print("3) Maple Bow")
    print("4) Yew Bow")
    print("5) Magic Bow")
    print("6) View Inventory")
    print("7) Back")
    while True:
        action = input('> ')
        if action == '1':       # Oak Bow
            if inventory.count("Oak Log") >= 2:   # 2 Oak Logs needed
                os.system('clear')
                print("\n#############")
                print("# Fletching #")
                print("#############\n")
                fletch("Oak Log")
                myPlayer.display_stats()
                fletching_prompt()
                break
            else:
                print("You need 2 Oak Logs to make an Oak Bow.")
        elif action == '2':     # Willow Bow
            if inventory.count("Willow Log") >= 2 and myPlayer.ft_lvl >= 5:        # 2 Willow logs and at least lvl 5
                os.system('clear')
                print("\n#############")
                print("# Fletching #")
                print("#############\n")
                fletch("Willow Log")
                myPlayer.display_stats()
                fletching_prompt()
                break
            elif myPlayer.ft_lvl < 5:
                print("You need a Fletching level of at least 5 to make Willow Bows.")
            else:
                print("You need 2 Willow Logs to make a Willow Bow.")
        elif action == '3':     # Maple Bow
            if inventory.count("Maple Log") >= 2 and myPlayer.ft_lvl >= 10:        # 2 Maple logs and at least lvl 10
                os.system('clear')
                print("\n#############")
                print("# Fletching #")
                print("#############\n")
                fletch("Maple Log")
                myPlayer.display_stats()
                fletching_prompt()
                break
            elif myPlayer.ft_lvl < 10:
                print("You need a Fletching level of at least 10 to make Maple Bows.")
            else:
                print("You need 2 Maple Logs to make a Maple Bow.")
        elif action == '4':     # Yew Bow
            if inventory.count("Yew Log") >= 2 and myPlayer.ft_lvl >= 15:        # 2 Yew logs and at least lvl 15
                os.system('clear')
                print("\n#############")
                print("# Fletching #")
                print("#############\n")
                fletch("Yew Log")
                myPlayer.display_stats()
                fletching_prompt()
                break
            elif myPlayer.ft_lvl < 15:
                print("You need a Fletching level of at least 15 to make Yew Bows.")
            else:
                print("You need 2 Yew Logs to make a Yew Bow.")
        elif action == '5':     # Magic Bow
            if inventory.count("Magic Log") >= 2 and myPlayer.ft_lvl >= 20:        # 2 Magic logs and at least lvl 20
                os.system('clear')
                print("\n#############")
                print("# Fletching #")
                print("#############\n")
                fletch("Magic Log")
                myPlayer.display_stats()
                fletching_prompt()
                break
            elif myPlayer.ft_lvl < 20:
                print("You need a Fletching level of at least 20 to make Magic Bows.")
            else:
                print("You need 2 Magic Logs to make a Magic Bow.")
        elif action == '6':     # Inventory
            os.system('clear')
            print("\n#############")
            print("# Fletching #")
            print("#############\n")
            inventory_prompt()
            fletching_prompt()
            break
        elif action == '7':     # Back
            os.system('clear')
            break
        else:                   # Input Validation
            print("Please enter a valid bow.")
            continue

# Fletch function
def fletch(logs):
    if logs == "Oak Log":
        print("You start cutting the logs into an Oak Bow...")
        for i in range(2):      # -2 Oak logs
            removeItem(logs)
        addToInventory("Oak Bow")
        print("You receive an Oak Bow!")
        myPlayer.ft_xp += items["Oak Bow"]["EXPERIENCE"]        # 15 XP
        if myPlayer.ft_xp >= myPlayer.ft_lvlUp:
            myPlayer.fletching_level_up()
        else:
            print("{} XP left to next level.\n".format(myPlayer.ft_lvlUp - myPlayer.ft_xp))
    elif logs == "Willow Log":
        print("You start cutting the logs into a Willow Bow...")
        for i in range(2):      # -2 Willow logs
            removeItem(logs)
        addToInventory("Willow Bow")
        print("You receive a Willow Bow!")
        myPlayer.ft_xp += items["Willow Bow"]["EXPERIENCE"]      # 30 XP
        if myPlayer.ft_xp >= myPlayer.ft_lvlUp:
            myPlayer.fletching_level_up()
        else:
            print("{} XP left to next level.\n".format(myPlayer.ft_lvlUp - myPlayer.ft_xp))
    elif logs == "Maple Log":
        print("You start cutting the logs into a Maple Bow...")
        for i in range(2):      # -2 Maple logs
            removeItem(logs)
        addToInventory("Maple Bow")
        print("You receive a Maple Bow!")
        myPlayer.ft_xp += items["Maple Bow"]["EXPERIENCE"]      # 60 XP
        if myPlayer.ft_xp >= myPlayer.ft_lvlUp:
            myPlayer.fletching_level_up()
        else:
            print("{} XP left to next level.\n".format(myPlayer.ft_lvlUp - myPlayer.ft_xp))
    elif logs == "Yew Log":
        print("You start cutting the logs into a Yew Bow...")
        for i in range(2):      # -2 Yew logs
            removeItem(logs)
        addToInventory("Yew Bow")
        print("You receive a Yew Bow!")
        myPlayer.ft_xp += items["Yew Bow"]["EXPERIENCE"]        # 120 XP
        if myPlayer.ft_xp >= myPlayer.ft_lvlUp:
            myPlayer.fletching_level_up()
        else:
            print("{} XP left to next level.\n".format(myPlayer.ft_lvlUp - myPlayer.ft_xp))
    elif logs == "Magic Log":
        print("You start cutting the logs into a Magic Bow...")
        for i in range(2):      # -2 Magic logs
            removeItem(logs)
        addToInventory("Magic Bow")
        print("You receive a Magic Bow!")
        myPlayer.ft_xp += items["Magic Bow"]["EXPERIENCE"]      # 240 XP
        if myPlayer.ft_xp >= myPlayer.ft_lvlUp:
            myPlayer.fletching_level_up()
        else:
            print("{} XP left to next level.\n".format(myPlayer.ft_lvlUp - myPlayer.ft_xp))

