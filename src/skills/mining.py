import cmd
import textwrap
import sys
import os
import time
from character.player import *
from gameplay.inventory import *

##### Mining #####

# Mining prompt
def mining_prompt():
    print("What type of ore do you want to mine?")
    print("1) Copper Ore")
    print("2) Iron Ore")
    print("3) Silver Ore")
    print("4) Gold Ore")
    print("5) Diamond Ore")
    print("6) View Inventory")
    print("7) Back")
    while True:
        action = input('> ')
        if action == '1':       # Copper ore
            os.system('clear')
            print("\n##########")
            print("# Mining #")
            print("##########\n")
            mine("Copper Ore")
            myPlayer.display_stats()
            mining_prompt()
            break
        elif action == '2' and myPlayer.mn_lvl < 5:     # Iron Ore lvl check
            print("You need a Mining level of at least 5 to mine Iron Ore.")
            continue 
        elif action == '2' and myPlayer.mn_lvl >= 5:    # Iron ore
            os.system('clear')
            print("\n##########")
            print("# Mining #")
            print("##########\n")
            mine("Iron Ore")
            myPlayer.display_stats()
            mining_prompt()
            break
        elif action == '3' and myPlayer.mn_lvl < 10:    # Silver ore lvl check
            print("You need a Mining level of at least 10 to mine Silver Ore.")
            continue 
        elif action == '3' and myPlayer.mn_lvl >= 10:   # Silver ore
            os.system('clear')
            print("\n##########")
            print("# Mining #")
            print("##########\n")
            mine("Silver Ore")
            myPlayer.display_stats()
            mining_prompt()
            break
        elif action == '4' and myPlayer.mn_lvl < 15:    # Gold ore lvl check
            print("You need a Mining level of at least 15 to mine Gold Ore.")
            continue 
        elif action == '4' and myPlayer.mn_lvl >= 15:   # Gold ore
            os.system('clear')
            print("\n##########")
            print("# Mining #")
            print("##########\n")
            mine("Gold Ore")
            myPlayer.display_stats()
            mining_prompt()
            break
        elif action == '5' and myPlayer.mn_lvl < 20:    # Diamond ore lvl check
            print("You need a Mining level of at least 20 to mine Diamond Ore.")
            continue 
        elif action == '5' and myPlayer.mn_lvl >= 20:   # Diamond ore
            os.system('clear')
            print("\n##########")
            print("# Mining #")
            print("##########\n")
            mine("Diamond Ore")
            myPlayer.display_stats()
            mining_prompt()
            break
        elif action == '6':     # Inventory
            os.system('clear')
            print("\n##########")
            print("# Mining #")
            print("##########\n")
            inventory_prompt()
            mining_prompt()
            break
        elif action == '7':     # Back
            os.system('clear')
            break
        else:                   # Input Validation
            print("Please enter a valid ore.")
            continue

# Woodcutting function
def mine(ore):
    if ore == "Copper Ore":
        print("You swing your pickaxe at the Copper node...")
        addToInventory("Copper Ore")
        print("You receive Copper Ore!")
        myPlayer.mn_xp += items["Copper Ore"]["EXPERIENCE"]      # 5 XP
        if myPlayer.mn_xp >= myPlayer.mn_lvlUp:
            myPlayer.mining_level_up()
        else:
            print("{} XP left to next level.\n".format(myPlayer.mn_lvlUp - myPlayer.mn_xp))
    elif ore == "Iron Ore":
        print("You swing your pickaxe at the Iron node...")
        addToInventory("Iron Ore")
        print("You receive Iron Ore!")
        myPlayer.mn_xp += items["Iron Ore"]["EXPERIENCE"]      # 10 XP
        if myPlayer.mn_xp >= myPlayer.mn_lvlUp:
            myPlayer.mining_level_up()
        else:
            print("{} XP left to next level.\n".format(myPlayer.mn_lvlUp - myPlayer.mn_xp))
    elif ore == "Silver Ore":
        print("You swing your pickaxe at the Silver node...")
        addToInventory("Silver Ore")
        print("You receive Silver Ore!")
        myPlayer.mn_xp += items["Silver Ore"]["EXPERIENCE"]      # 20 XP
        if myPlayer.mn_xp >= myPlayer.mn_lvlUp:
            myPlayer.mining_level_up()
        else:
            print("{} XP left to next level.\n".format(myPlayer.mn_lvlUp - myPlayer.mn_xp))
    elif ore == "Gold Ore":
        print("You swing your pickaxe at the Gold node...")
        addToInventory("Gold Ore")
        print("You receive Gold Ore!")
        myPlayer.mn_xp += items["Gold Ore"]["EXPERIENCE"]      # 40 XP
        if myPlayer.mn_xp >= myPlayer.mn_lvlUp:
            myPlayer.mining_level_up()
        else:
            print("{} XP left to next level.\n".format(myPlayer.mn_lvlUp - myPlayer.mn_xp))
    elif ore == "Diamond Ore":
        print("You swing your pickaxe at the Diamond node...")
        addToInventory("Diamond Ore")
        print("You receive Diamond Ore!")
        myPlayer.mn_xp += items["Diamond Ore"]["EXPERIENCE"]      # 5 XP
        if myPlayer.mn_xp >= myPlayer.mn_lvlUp:
            myPlayer.mining_level_up()
        else:
            print("{} XP left to next level.\n".format(myPlayer.mn_lvlUp - myPlayer.mn_xp))

  