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
    print("What would you like to do?")
    print("1) Make unstrung bows")
    print("2) String bows")
    print("3) View Inventory")
    print("4) Back")
    while True:
        action = input('> ')
        if action == '1':       # Unstrung bows 
            os.system('clear')
            print("\n#############")
            print("# Fletching #")
            print("#############\n")
            myPlayer.display_stats()
            unstrung_prompt()
            break
        elif action == '2':     # String bows
            os.system('clear')
            print("\n#############")
            print("# Fletching #")
            print("#############\n")
            myPlayer.display_stats()
            string_bow_prompt()
            break
        elif action == '3':     # Inventory
            os.system('clear')
            print("\n#############")
            print("# Fletching #")
            print("#############\n")
            inventory_prompt()
            os.system('clear')
            print("\n#############")
            print("# Fletching #")
            print("#############\n")
            myPlayer.display_stats()
            fletching_prompt()
            break
        elif action == '4':     # Back
            os.system('clear')
            break
        else:                   # Input Validation
            print("Please enter a valid action.")
            continue
        
# Unstrung prompt
def unstrung_prompt():
    print("What bow would you like to make?")
    print("1) Oak Bow (u)")
    print("2) Willow Bow (u)")
    print("3) Maple Bow (u)")
    print("4) Yew Bow (u)")
    print("5) Magic Bow (u)")
    print("6) View Inventory")
    print("7) Back")
    while True:
        action = input('> ')
        if action == '1':       # Oak Bow (u)
            if inventory.count("Oak Log") >= 2:   # 2 Oak Logs needed
                os.system('clear')
                print("\n#############")
                print("# Fletching #")
                print("#############\n")
                fletch("Oak Log")
                myPlayer.display_stats()
                unstrung_prompt()
                break
            else:
                print("You need 2 Oak Logs to make an Oak Bow (u).")
        elif action == '2':     # Willow Bow (u)
            if inventory.count("Willow Log") >= 2 and myPlayer.ft_lvl >= 5:        # 2 Willow logs and at least lvl 5
                os.system('clear')
                print("\n#############")
                print("# Fletching #")
                print("#############\n")
                fletch("Willow Log")
                myPlayer.display_stats()
                unstrung_prompt()
                break
            elif myPlayer.ft_lvl < 5:
                print("You need a Fletching level of at least 5 to make Willow Bows (u).")
            else:
                print("You need 2 Willow Logs to make a Willow Bow (u).")
        elif action == '3':     # Maple Bow (u)
            if inventory.count("Maple Log") >= 2 and myPlayer.ft_lvl >= 10:        # 2 Maple logs and at least lvl 10
                os.system('clear')
                print("\n#############")
                print("# Fletching #")
                print("#############\n")
                fletch("Maple Log")
                myPlayer.display_stats()
                unstrung_prompt()
                break
            elif myPlayer.ft_lvl < 10:
                print("You need a Fletching level of at least 10 to make Maple Bows (u).")
            else:
                print("You need 2 Maple Logs to make a Maple Bow (u).")
        elif action == '4':     # Yew Bow (u)
            if inventory.count("Yew Log") >= 2 and myPlayer.ft_lvl >= 15:        # 2 Yew logs and at least lvl 15
                os.system('clear')
                print("\n#############")
                print("# Fletching #")
                print("#############\n")
                fletch("Yew Log")
                myPlayer.display_stats()
                unstrung_prompt()
                break
            elif myPlayer.ft_lvl < 15:
                print("You need a Fletching level of at least 15 to make Yew Bows (u).")
            else:
                print("You need 2 Yew Logs to make a Yew Bow (u).")
        elif action == '5':     # Magic Bow (u)
            if inventory.count("Magic Log") >= 2 and myPlayer.ft_lvl >= 20:        # 2 Magic logs and at least lvl 20
                os.system('clear')
                print("\n#############")
                print("# Fletching #")
                print("#############\n")
                fletch("Magic Log")
                myPlayer.display_stats()
                unstrung_prompt()
                break
            elif myPlayer.ft_lvl < 20:
                print("You need a Fletching level of at least 20 to make Magic Bows (u).")
            else:
                print("You need 2 Magic Logs to make a Magic Bow (u).")
        elif action == '6':     # Inventory
            os.system('clear')
            print("\n#############")
            print("# Fletching #")
            print("#############\n")
            inventory_prompt()
            os.system('clear')
            print("\n#############")
            print("# Fletching #")
            print("#############\n")
            myPlayer.display_stats()
            unstrung_prompt()
            break
        elif action == '7':     # Back
            os.system('clear')
            print("\n#############")
            print("# Fletching #")
            print("#############\n")
            myPlayer.display_stats()
            fletching_prompt()
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
        addToInventory("Oak Bow (u)")
        print("You receive an Oak Bow (u)!")
        myPlayer.ft_xp += items["Oak Bow (u)"]["EXPERIENCE"]        # 10 XP
        if myPlayer.ft_xp >= myPlayer.ft_lvlUp:
            myPlayer.fletching_level_up()
        else:
            print("{} XP left to next level.\n".format(myPlayer.ft_lvlUp - myPlayer.ft_xp))
    elif logs == "Willow Log":
        print("You start cutting the logs into a Willow Bow...")
        for i in range(2):      # -2 Willow logs
            removeItem(logs)
        addToInventory("Willow Bow (u)")
        print("You receive a Willow Bow (u)!")
        myPlayer.ft_xp += items["Willow Bow (u)"]["EXPERIENCE"]      # 20 XP
        if myPlayer.ft_xp >= myPlayer.ft_lvlUp:
            myPlayer.fletching_level_up()
        else:
            print("{} XP left to next level.\n".format(myPlayer.ft_lvlUp - myPlayer.ft_xp))
    elif logs == "Maple Log":
        print("You start cutting the logs into a Maple Bow...")
        for i in range(2):      # -2 Maple logs
            removeItem(logs)
        addToInventory("Maple Bow (u)")
        print("You receive a Maple Bow (u)!")
        myPlayer.ft_xp += items["Maple Bow (u)"]["EXPERIENCE"]      # 45 XP
        if myPlayer.ft_xp >= myPlayer.ft_lvlUp:
            myPlayer.fletching_level_up()
        else:
            print("{} XP left to next level.\n".format(myPlayer.ft_lvlUp - myPlayer.ft_xp))
    elif logs == "Yew Log":
        print("You start cutting the logs into a Yew Bow...")
        for i in range(2):      # -2 Yew logs
            removeItem(logs)
        addToInventory("Yew Bow (u)")
        print("You receive a Yew Bow (u)!")
        myPlayer.ft_xp += items["Yew Bow (u)"]["EXPERIENCE"]        # 90 XP
        if myPlayer.ft_xp >= myPlayer.ft_lvlUp:
            myPlayer.fletching_level_up()
        else:
            print("{} XP left to next level.\n".format(myPlayer.ft_lvlUp - myPlayer.ft_xp))
    elif logs == "Magic Log":
        print("You start cutting the logs into a Magic Bow...")
        for i in range(2):      # -2 Magic logs
            removeItem(logs)
        addToInventory("Magic Bow (u)")
        print("You receive a Magic Bow (u)!")
        myPlayer.ft_xp += items["Magic Bow (u)"]["EXPERIENCE"]      # 170 XP
        if myPlayer.ft_xp >= myPlayer.ft_lvlUp:
            myPlayer.fletching_level_up()
        else:
            print("{} XP left to next level.\n".format(myPlayer.ft_lvlUp - myPlayer.ft_xp))

# String bow prompt
def string_bow_prompt():
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
            if inventory.count("Bow String") >= 1:   # 1 Bow string needed
                os.system('clear')
                print("\n#############")
                print("# Fletching #")
                print("#############\n")
                string("Oak Bow")
                myPlayer.display_stats()
                string_bow_prompt()
                break
            else:
                print("You need a Bow String to make an Oak Bow.")
        elif action == '2':     # Willow Bow
            if inventory.count("Bow String") >= 1 and myPlayer.ft_lvl >= 6:        # 1 Bow string and at least lvl 6
                os.system('clear')
                print("\n#############")
                print("# Fletching #")
                print("#############\n")
                string("Willow Bow")
                myPlayer.display_stats()
                string_bow_prompt()
                break
            elif myPlayer.ft_lvl < 6:
                print("You need a Fletching level of at least 6 to make Willow Bows.")
            else:
                print("You need a Bow String to make a Willow Bow.")
        elif action == '3':     # Maple Bow
            if inventory.count("Bow String") >= 1 and myPlayer.ft_lvl >= 11:        # 1 Bow string and at least lvl 11
                os.system('clear')
                print("\n#############")
                print("# Fletching #")
                print("#############\n")
                string("Maple Bow")
                myPlayer.display_stats()
                string_bow_prompt()
                break
            elif myPlayer.ft_lvl < 11:
                print("You need a Fletching level of at least 11 to make Maple Bows.")
            else:
                print("You need a Bow String to make a Maple Bow.")
        elif action == '4':     # Yew Bow
            if inventory.count("Bow String") >= 1 and myPlayer.ft_lvl >= 16:        # 1 Bow string and at least lvl 16
                os.system('clear')
                print("\n#############")
                print("# Fletching #")
                print("#############\n")
                string("Yew Bow")
                myPlayer.display_stats()
                string_bow_prompt()
                break
            elif myPlayer.ft_lvl < 16:
                print("You need a Fletching level of at least 16 to make Yew Bows.")
            else:
                print("You need a Bow String to make a Yew Bow.")
        elif action == '5':     # Magic Bow
            if inventory.count("Bow String") >= 1 and myPlayer.ft_lvl >= 21:        # 1 Bow string and at least lvl 21
                os.system('clear')
                print("\n#############")
                print("# Fletching #")
                print("#############\n")
                string("Magic Bow")
                myPlayer.display_stats()
                string_bow_prompt()
                break
            elif myPlayer.ft_lvl < 21:
                print("You need a Fletching level of at least 21 to make Magic Bows.")
            else:
                print("You need a Bow String to make a Magic Bow.")
        elif action == '6':     # Inventory
            os.system('clear')
            print("\n#############")
            print("# Fletching #")
            print("#############\n")
            inventory_prompt()
            os.system('clear')
            print("\n#############")
            print("# Fletching #")
            print("#############\n")
            myPlayer.display_stats()
            string_bow_prompt()
            break
        elif action == '7':     # Back
            os.system('clear')
            print("\n#############")
            print("# Fletching #")
            print("#############\n")
            myPlayer.display_stats()
            fletching_prompt()
            break
        else:                   # Input Validation
            print("Please enter a valid bow.")
            continue

# String bows prompt
def string(bow):
    if bow == "Oak Bow":
        print("You start stringing the Oak Bow...")
        removeItem("Bow String")
        addToInventory("Oak Bow")
        print("You receive an Oak Bow!")
        myPlayer.ft_xp += items["Oak Bow"]["EXPERIENCE"]            # 15 XP
        if myPlayer.ft_xp >= myPlayer.ft_lvlUp:
            myPlayer.fletching_level_up()
        else:
            print("{} XP left to next level.\n".format(myPlayer.ft_lvlUp - myPlayer.ft_xp))
    elif bow == "Willow Bow":
        print("You start stringing the Willow Bow...")
        removeItem("Bow String")
        addToInventory("Willow Bow")
        print("You receive a Willow Bow!")
        myPlayer.ft_xp += items["Willow Bow"]["EXPERIENCE"]          # 30 XP
        if myPlayer.ft_xp >= myPlayer.ft_lvlUp:
            myPlayer.fletching_level_up()
        else:
            print("{} XP left to next level.\n".format(myPlayer.ft_lvlUp - myPlayer.ft_xp))
    elif bow == "Maple Bow":
        print("You start stringing the Maple Bow...")
        removeItem("Bow String")
        addToInventory("Maple Bow")
        print("You receive a Maple Bow!")
        myPlayer.ft_xp += items["Maple Bow"]["EXPERIENCE"]          # 60 XP
        if myPlayer.ft_xp >= myPlayer.ft_lvlUp:
            myPlayer.fletching_level_up()
        else:
            print("{} XP left to next level.\n".format(myPlayer.ft_lvlUp - myPlayer.ft_xp))
    elif bow == "Yew Bow":
        print("You start stringing the Yew Bow...")
        removeItem("Bow String")
        addToInventory("Yew Bow")
        print("You receive a Yew Bow!")
        myPlayer.ft_xp += items["Yew Bow"]["EXPERIENCE"]            # 120 XP
        if myPlayer.ft_xp >= myPlayer.ft_lvlUp:
            myPlayer.fletching_level_up()
        else:
            print("{} XP left to next level.\n".format(myPlayer.ft_lvlUp - myPlayer.ft_xp))
    elif bow == "Magic Bow":
        print("You start stringing the Magic Bow...")
        removeItem("Bow String")
        addToInventory("Magic Bow")
        print("You receive a Magic Bow!")
        myPlayer.ft_xp += items["Magic Bow"]["EXPERIENCE"]          # 240 XP
        if myPlayer.ft_xp >= myPlayer.ft_lvlUp:
            myPlayer.fletching_level_up()
        else:
            print("{} XP left to next level.\n".format(myPlayer.ft_lvlUp - myPlayer.ft_xp))