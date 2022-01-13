import cmd
import textwrap
import sys
import os
import time
from character.player import *
from gameplay.inventory import *
from skills.skill_wait_time import *

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

# Mining function
def mine(ore):
    # Copper Ore
    if ore == "Copper Ore":
        print("You swing your pickaxe at the Copper node", end='')
        # Determine Mining time
        if myPlayer.mn_lvl < 2:                                 # level 1-2
            skill_wait_time(0)
        elif myPlayer.mn_lvl >= 2 and myPlayer.mn_lvl < 5:      # level 2-5
            skill_wait_time(1)
        elif myPlayer.mn_lvl >= 5 and myPlayer.mn_lvl < 9:      # level 5-9
            skill_wait_time(2)                  
        else:                                                   # level 9+
            skill_wait_time(3)
        addToInventory("Copper Ore")
        print("You receive Copper Ore!")
        myPlayer.mn_xp += items["Copper Ore"]["EXPERIENCE"]  
        if myPlayer.mn_lvl < myPlayer.max_level:    
            if myPlayer.mn_xp >= myPlayer.mn_lvlUp:
                myPlayer.mining_level_up()
            else:
                print("{} XP left to next level.\n".format(myPlayer.mn_lvlUp - myPlayer.mn_xp))

    # Iron Ore
    elif ore == "Iron Ore":
        print("You swing your pickaxe at the Iron node", end='')
        # Determine Mining time
        if myPlayer.mn_lvl < 7:                                 # level 5-7
            skill_wait_time(0)
        elif myPlayer.mn_lvl >= 7 and myPlayer.mn_lvl < 10:     # level 7-10
            skill_wait_time(1)
        elif myPlayer.mn_lvl >= 10 and myPlayer.mn_lvl < 14:    # level 10-14
            skill_wait_time(2)
        else:                                                   # level 14+
            skill_wait_time(3)
        addToInventory("Iron Ore")
        print("You receive Iron Ore!")
        myPlayer.mn_xp += items["Iron Ore"]["EXPERIENCE"]
        if myPlayer.mn_lvl < myPlayer.max_level:      
            if myPlayer.mn_xp >= myPlayer.mn_lvlUp:
                myPlayer.mining_level_up()
            else:
                print("{} XP left to next level.\n".format(myPlayer.mn_lvlUp - myPlayer.mn_xp))

    # Silver Ore
    elif ore == "Silver Ore":
        print("You swing your pickaxe at the Silver node", end='')
        # Determine Mining time
        if myPlayer.mn_lvl < 12:                                # level 10-12
            skill_wait_time(0)
        elif myPlayer.mn_lvl >= 12 and myPlayer.mn_lvl < 15:    # level 12-15
            skill_wait_time(1)
        elif myPlayer.mn_lvl >= 15 and myPlayer.mn_lvl < 19:    # level 15-19
            skill_wait_time(2)
        else:                                                   # level 19+
            skill_wait_time(3)
        addToInventory("Silver Ore")
        print("You receive Silver Ore!")
        myPlayer.mn_xp += items["Silver Ore"]["EXPERIENCE"] 
        if myPlayer.mn_lvl < myPlayer.max_level:    
            if myPlayer.mn_xp >= myPlayer.mn_lvlUp:
                myPlayer.mining_level_up()
            else:
                print("{} XP left to next level.\n".format(myPlayer.mn_lvlUp - myPlayer.mn_xp))

    # Gold Ore
    elif ore == "Gold Ore":
        print("You swing your pickaxe at the Gold", end='')
        # Determine Mining time
        if myPlayer.mn_lvl < 17:                                # level 15-17
            skill_wait_time(0)
        elif myPlayer.mn_lvl >= 17 and myPlayer.mn_lvl < 20:    # level 17-20
            skill_wait_time(1)
        elif myPlayer.mn_lvl >= 20 and myPlayer.mn_lvl < 22:    # level 20-22
            skill_wait_time(2)
        else:                                                   # level 22+
            skill_wait_time(3)
        addToInventory("Gold Ore")
        print("You receive Gold Ore!")
        myPlayer.mn_xp += items["Gold Ore"]["EXPERIENCE"] 
        if myPlayer.mn_lvl < myPlayer.max_level:    
            if myPlayer.mn_xp >= myPlayer.mn_lvlUp:
                myPlayer.mining_level_up()
            else:
                print("{} XP left to next level.\n".format(myPlayer.mn_lvlUp - myPlayer.mn_xp))

    # Diamond Ore
    elif ore == "Diamond Ore":
        print("You swing your pickaxe at the Diamond node", end='')
        # Determine Mining time
        if myPlayer.mn_lvl < 22:                                # level 20-22
            skill_wait_time(0)
        elif myPlayer.mn_lvl >= 22 and myPlayer.mn_lvl < 23:    # level 22
            skill_wait_time(1)
        elif myPlayer.mn_lvl >= 23 and myPlayer.mn_lvl < 24:    # level 23
            skill_wait_time(2)
        else:                                                   # level 24+
            skill_wait_time(3)
        addToInventory("Diamond Ore")
        print("You receive Diamond Ore!")
        myPlayer.mn_xp += items["Diamond Ore"]["EXPERIENCE"]
        if myPlayer.mn_lvl < myPlayer.max_level:      
            if myPlayer.mn_xp >= myPlayer.mn_lvlUp:
                myPlayer.mining_level_up()
            else:
                print("{} XP left to next level.\n".format(myPlayer.mn_lvlUp - myPlayer.mn_xp))

