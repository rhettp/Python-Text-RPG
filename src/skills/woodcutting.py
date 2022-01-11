import cmd
import textwrap
import sys
import os
import time
from character.player import *
from gameplay.inventory import *
from skills.skill_wait_time import *

##### Woodcutting #####

# Woodcutting prompt
def woodcutting_prompt():
    print("What type of tree do you want to cut down?")
    print("1) Oak Tree")
    print("2) Willow Tree")
    print("3) Maple Tree")
    print("4) Yew Tree")
    print("5) Magic Tree")
    print("6) View Inventory")
    print("7) Back")
    while True:
        action = input('> ')
        if action == '1':       # Oak tree
            os.system('clear')
            print("\n###############")
            print("# Woodcutting #")
            print("###############\n")
            woodcut("Oak Log")
            myPlayer.display_stats()
            woodcutting_prompt()
            break
        elif action == '2' and myPlayer.wc_lvl < 5:     # Willow tree lvl check
            print("You need a Woodcutting level of at least 5 to cut Willow Trees.")
            continue 
        elif action == '2' and myPlayer.wc_lvl >= 5:    # Willow tree
            os.system('clear')
            print("\n###############")
            print("# Woodcutting #")
            print("###############\n")
            woodcut("Willow Log")
            myPlayer.display_stats()
            woodcutting_prompt()
            break
        elif action == '3' and myPlayer.wc_lvl < 10:    # Maple tree lvl check
            print("You need a Woodcutting level of at least 10 to cut Maple Trees.")
            continue 
        elif action == '3' and myPlayer.wc_lvl >= 10:   # Maple tree
            os.system('clear')
            print("\n###############")
            print("# Woodcutting #")
            print("###############\n")
            woodcut("Maple Log")
            myPlayer.display_stats()
            woodcutting_prompt()
            break
        elif action == '4' and myPlayer.wc_lvl < 15:    # Yew tree lvl check
            print("You need a Woodcutting level of at least 15 to cut Yew Trees.")
            continue 
        elif action == '4' and myPlayer.wc_lvl >= 15:   # Yew tree
            os.system('clear')
            print("\n###############")
            print("# Woodcutting #")
            print("###############\n")
            woodcut("Yew Log")
            myPlayer.display_stats()
            woodcutting_prompt()
            break
        elif action == '5' and myPlayer.wc_lvl < 20:    # Magic tree lvl check
            print("You need a Woodcutting level of at least 20 to cut Magic Trees.")
            continue 
        elif action == '5' and myPlayer.wc_lvl >= 20:   # Magic tree
            os.system('clear')
            print("\n###############")
            print("# Woodcutting #")
            print("###############\n")
            woodcut("Magic Log")
            myPlayer.display_stats()
            woodcutting_prompt()
            break
        elif action == '6':     # Inventory
            os.system('clear')
            print("\n###############")
            print("# Woodcutting #")
            print("###############\n")
            inventory_prompt()
            woodcutting_prompt()
            break
        elif action == '7':     # Back
            os.system('clear')
            break
        else:                   # Input Validation
            print("Please enter a valid tree.")
            continue

# Woodcutting function
def woodcut(log):
    if log == "Oak Log":
        print("You swing your axe at the Oak Tree", end="")
        # Determine woodcutting time
        if myPlayer.wc_lvl < 2:                                 # level 1-2
            skill_wait_time(0)
        elif myPlayer.wc_lvl >= 2 and myPlayer.wc_lvl < 5:      # level 2-5
            skill_wait_time(1)
        elif myPlayer.wc_lvl >= 5 and myPlayer.wc_lvl < 9:      # level 5-9
            skill_wait_time(2)                  
        else:                                                   # level 9+
            skill_wait_time(3)
        addToInventory("Oak Log")
        print("You receive an Oak Log!")
        myPlayer.wc_xp += items["Oak Log"]["EXPERIENCE"]      # 5 XP
        if myPlayer.wc_xp >= myPlayer.wc_lvlUp:
            myPlayer.woodcutting_level_up()
        else:
            print("{} XP left to next level.\n".format(myPlayer.wc_lvlUp - myPlayer.wc_xp))
    elif log == "Willow Log":
        print("You swing your axe at the Willow Tree", end="")
        # Determine woodcutting time
        if myPlayer.wc_lvl < 7:                                 # level 5-7
            skill_wait_time(0)
        elif myPlayer.wc_lvl >= 7 and myPlayer.wc_lvl < 10:     # level 7-10
            skill_wait_time(1)
        elif myPlayer.wc_lvl >= 10 and myPlayer.wc_lvl < 14:    # level 10-14
            skill_wait_time(2)
        else:                                                   # level 14+
            skill_wait_time(3)
        addToInventory("Willow Log")
        print("You receive a Willow Log!")
        myPlayer.wc_xp += items["Willow Log"]["EXPERIENCE"]   # 10 XP
        if myPlayer.wc_xp >= myPlayer.wc_lvlUp:
            myPlayer.woodcutting_level_up()
        else:
            print("{} XP left to next level.\n".format(myPlayer.wc_lvlUp - myPlayer.wc_xp))
    elif log == "Maple Log":
        print("You swing your axe at the Maple Tree", end='')
        # Determine woodcutting time
        if myPlayer.wc_lvl < 12:                                # level 10-12
            skill_wait_time(0)
        elif myPlayer.wc_lvl >= 12 and myPlayer.wc_lvl < 15:    # level 12-15
            skill_wait_time(1)
        elif myPlayer.wc_lvl >= 15 and myPlayer.wc_lvl < 19:    # level 15-19
            skill_wait_time(2)
        else:                                                   # level 19+
            skill_wait_time(3)
        addToInventory("Maple Log")
        print("You receive a Maple Log!")
        myPlayer.wc_xp += items["Maple Log"]["EXPERIENCE"]    # 20 XP
        if myPlayer.wc_xp >= myPlayer.wc_lvlUp:
            myPlayer.woodcutting_level_up()
        else:
            print("{} XP left to next level.\n".format(myPlayer.wc_lvlUp - myPlayer.wc_xp))
    elif log == "Yew Log":
        print("You swing your axe at the Yew Tree", end='')
        if myPlayer.wc_lvl < 17:                                # level 15-17
            skill_wait_time(0)
        elif myPlayer.wc_lvl >= 17 and myPlayer.wc_lvl < 20:    # level 17-20
            skill_wait_time(1)
        elif myPlayer.wc_lvl >= 20 and myPlayer.wc_lvl < 22:    # level 20-22
            skill_wait_time(2)
        else:                                                   # level 22+
            skill_wait_time(3)
        addToInventory("Yew Log")
        print("You receive a Yew Log!")
        myPlayer.wc_xp += items["Yew Log"]["EXPERIENCE"]      # 40 XP
        if myPlayer.wc_xp >= myPlayer.wc_lvlUp:
            myPlayer.woodcutting_level_up()
        else:
            print("{} XP left to next level.\n".format(myPlayer.wc_lvlUp - myPlayer.wc_xp))
    elif log == "Magic Log":
        print("You swing your axe at the Magic Tree", end='')
        if myPlayer.wc_lvl < 22:                                # level 20-22
            skill_wait_time(0)
        elif myPlayer.wc_lvl >= 22 and myPlayer.wc_lvl < 23:    # level 22
            skill_wait_time(1)
        elif myPlayer.wc_lvl >= 23 and myPlayer.wc_lvl < 24:    # level 23
            skill_wait_time(2)
        else:                                                   # level 24+
            skill_wait_time(3)
        addToInventory("Magic Log")
        print("You receive a Magic Log!")
        myPlayer.wc_xp += items["Magic Log"]["EXPERIENCE"]    # 80 XP
        if myPlayer.wc_xp >= myPlayer.wc_lvlUp:
            myPlayer.woodcutting_level_up()
        else:
            print("{} XP left to next level.\n".format(myPlayer.wc_lvlUp - myPlayer.wc_xp))
        