import cmd
import textwrap
import sys
import os
import time
from character.player import *
from gameplay.inventory import *
from skills.skill_wait_time import *

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
    # Oak Bow
    if logs == "Oak Log":
        print("You start cutting the logs into an Oak Bow", end="")
        # Determine Fletching time
        if myPlayer.ft_lvl < 2:                                 # level 1-2
            skill_wait_time(0)
        elif myPlayer.ft_lvl >= 2 and myPlayer.ft_lvl < 5:      # level 2-5
            skill_wait_time(1)
        elif myPlayer.ft_lvl >= 5 and myPlayer.ft_lvl < 9:      # level 5-9
            skill_wait_time(2)                  
        else:                                                   # level 9+
            skill_wait_time(3)

        # Remove logs from inventory
        for i in range(2):      # -2 Oak logs
            removeItem(logs)
        addToInventory("Oak Bow (u)")
        print("You receive an Oak Bow (u)!")
        myPlayer.ft_xp += items["Oak Bow (u)"]["EXPERIENCE"]      
        if myPlayer.ft_xp >= myPlayer.ft_lvlUp:
            myPlayer.fletching_level_up()
        else:
            print("{} XP left to next level.\n".format(myPlayer.ft_lvlUp - myPlayer.ft_xp))

    # Willow Bow
    elif logs == "Willow Log":
        print("You start cutting the logs into a Willow Bow", end='')
        # Determine Fletching time
        if myPlayer.ft_lvl < 7:                                 # level 5-7
            skill_wait_time(0)
        elif myPlayer.ft_lvl >= 7 and myPlayer.ft_lvl < 10:     # level 7-10
            skill_wait_time(1)
        elif myPlayer.ft_lvl >= 10 and myPlayer.ft_lvl < 14:    # level 10-14
            skill_wait_time(2)
        else:                                                   # level 14+
            skill_wait_time(3)

        # Remove logs from inventory
        for i in range(2):      # -2 Willow logs
            removeItem(logs)
        addToInventory("Willow Bow (u)")
        print("You receive a Willow Bow (u)!")
        myPlayer.ft_xp += items["Willow Bow (u)"]["EXPERIENCE"]     
        if myPlayer.ft_xp >= myPlayer.ft_lvlUp:
            myPlayer.fletching_level_up()
        else:
            print("{} XP left to next level.\n".format(myPlayer.ft_lvlUp - myPlayer.ft_xp))

    # Maple Bow
    elif logs == "Maple Log":
        print("You start cutting the logs into a Maple Bow", end='')
        # Determine Fletching time
        if myPlayer.ft_lvl < 12:                                # level 10-12
            skill_wait_time(0)
        elif myPlayer.ft_lvl >= 12 and myPlayer.ft_lvl < 15:    # level 12-15
            skill_wait_time(1)
        elif myPlayer.ft_lvl >= 15 and myPlayer.ft_lvl < 19:    # level 15-19
            skill_wait_time(2)
        else:                                                   # level 19+
            skill_wait_time(3)

        # Remove logs from inventory
        for i in range(2):      # -2 Maple logs
            removeItem(logs)
        addToInventory("Maple Bow (u)")
        print("You receive a Maple Bow (u)!")
        myPlayer.ft_xp += items["Maple Bow (u)"]["EXPERIENCE"]     
        if myPlayer.ft_xp >= myPlayer.ft_lvlUp:
            myPlayer.fletching_level_up()
        else:
            print("{} XP left to next level.\n".format(myPlayer.ft_lvlUp - myPlayer.ft_xp))

    # Yew Bow
    elif logs == "Yew Log":
        print("You start cutting the logs into a Yew Bow", end='')
        # Determine Fletching time
        if myPlayer.ft_lvl < 17:                                # level 15-17
            skill_wait_time(0)
        elif myPlayer.ft_lvl >= 17 and myPlayer.ft_lvl < 20:    # level 17-20
            skill_wait_time(1)
        elif myPlayer.ft_lvl >= 20 and myPlayer.ft_lvl < 22:    # level 20-22
            skill_wait_time(2)
        else:                                                   # level 22+
            skill_wait_time(3)

        # Remove logs from inventory
        for i in range(2):      # -2 Yew logs
            removeItem(logs)
        addToInventory("Yew Bow (u)")
        print("You receive a Yew Bow (u)!")
        myPlayer.ft_xp += items["Yew Bow (u)"]["EXPERIENCE"]       
        if myPlayer.ft_xp >= myPlayer.ft_lvlUp:
            myPlayer.fletching_level_up()
        else:
            print("{} XP left to next level.\n".format(myPlayer.ft_lvlUp - myPlayer.ft_xp))

    # Magic Bow
    elif logs == "Magic Log":
        print("You start cutting the logs into a Magic Bow", end='')
        # Determine Fletching time
        if myPlayer.ft_lvl < 22:                                # level 20-22
            skill_wait_time(0)
        elif myPlayer.ft_lvl >= 22 and myPlayer.ft_lvl < 23:    # level 22
            skill_wait_time(1)
        elif myPlayer.ft_lvl >= 23 and myPlayer.ft_lvl < 24:    # level 23
            skill_wait_time(2)
        else:                                                   # level 24+
            skill_wait_time(3)

        # Remove logs from inventory
        for i in range(2):      # -2 Magic logs
            removeItem(logs)
        addToInventory("Magic Bow (u)")
        print("You receive a Magic Bow (u)!")
        myPlayer.ft_xp += items["Magic Bow (u)"]["EXPERIENCE"]     
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
        # Oak Bow
        if action == '1':
            # 1 Bow string, 1 Oak Bow (u), and at least lvl 2
            if inventory.count("Bow String") >= 1 and inventory.count("Oak Bow (u)") >= 1 and myPlayer.ft_lvl >= 2:
                os.system('clear')
                print("\n#############")
                print("# Fletching #")
                print("#############\n")
                string("Oak Bow")
                myPlayer.display_stats()
                string_bow_prompt()
                break
            elif myPlayer.ft_lvl < 2:                                                           # level less than 2
                print("You need a Fletching level of at least 2 to make Oak Bows.")
            elif inventory.count("Bow String") < 1 and inventory.count("Oak Bow (u)") < 1:      # No Bow String or Bow (u)
                print("You need a Bow String and an Oak Bow (u) to make an Oak Bow.")
            elif inventory.count("Bow String") >= 1 and inventory.count("Oak Bow (u)") < 1:     # Has Bow String, no Bow (u)
                print("You need an Oak Bow (u) to make an Oak Bow.")
            else:
                print("You need a Bow String to make an Oak Bow.")                              # No Bow String, has Bow (u)

        # Willow Bow
        elif action == '2':
            # 1 Bow string, 1 Willow Bow (u), and at least lvl 6
            if inventory.count("Bow String") >= 1 and inventory.count("Willow Bow (u)") >= 1 and myPlayer.ft_lvl >= 6:       
                os.system('clear')
                print("\n#############")
                print("# Fletching #")
                print("#############\n")
                string("Willow Bow")
                myPlayer.display_stats()
                string_bow_prompt()
                break
            elif myPlayer.ft_lvl < 6:                                                           # level less than 6
                print("You need a Fletching level of at least 6 to make Willow Bows.")
            elif inventory.count("Bow String") < 1 and inventory.count("Willow Bow (u)") < 1:   # No Bow String or Bow (u)
                print("You need a Bow String and a Willow Bow (u) to make a Willow Bow.")
            elif inventory.count("Bow String") >= 1 and inventory.count("Willow Bow (u)") < 1:  # Has Bow String, no Bow (u)
                print("You need a Willow Bow (u) to make a Willow Bow.")
            else:
                print("You need a Bow String to make a Willow Bow.")                            # No Bow String, has Bow (u)

        # Maple Bow
        elif action == '3':
            # 1 Bow string, 1 Maple Bow (u), and at least lvl 11
            if inventory.count("Bow String") >= 1 and inventory.count("Maple Bow (u)") >= 1 and myPlayer.ft_lvl >= 11:        
                os.system('clear')
                print("\n#############")
                print("# Fletching #")
                print("#############\n")
                string("Maple Bow")
                myPlayer.display_stats()
                string_bow_prompt()
                break
            elif myPlayer.ft_lvl < 11:                                                         # level less than 11
                print("You need a Fletching level of at least 11 to make Maple Bows.")
            elif inventory.count("Bow String") < 1 and inventory.count("Maple Bow (u)") < 1:   # No Bow String or Bow (u)
                print("You need a Bow String and a Maple Bow (u) to make a Maple Bow.")
            elif inventory.count("Bow String") >= 1 and inventory.count("Maple Bow (u)") < 1:  # Has Bow String, no Bow (u)
                print("You need a Maple Bow (u) to make a Maple Bow.")
            else:
                print("You need a Bow String to make a Maple Bow.")                            # No Bow String, has Bow (u)

        # Yew Bow
        elif action == '4':
            # 1 Bow string, 1 Yew Bow (u), and at least lvl 16
            if inventory.count("Bow String") >= 1 and inventory.count("Yew Bow (u)") >= 1 and myPlayer.ft_lvl >= 16:        
                os.system('clear')
                print("\n#############")
                print("# Fletching #")
                print("#############\n")
                string("Yew Bow")
                myPlayer.display_stats()
                string_bow_prompt()
                break
            elif myPlayer.ft_lvl < 16:                                                       # level less than 16
                print("You need a Fletching level of at least 16 to make Yew Bows.")
            elif inventory.count("Bow String") < 1 and inventory.count("Yew Bow (u)") < 1:   # No Bow String or Bow (u)
                print("You need a Bow String and a Yew Bow (u) to make a Yew Bow.")
            elif inventory.count("Bow String") >= 1 and inventory.count("Yew Bow (u)") < 1:  # Has Bow String, no Bow (u)
                print("You need a Yew Bow (u) to make a Yew Bow.")
            else:
                print("You need a Bow String to make a Yew Bow.")                            # No Bow String, has Bow (u)

        # Magic Bow
        elif action == '5':   
            # 1 Bow string, 1 Magic Bow (u), and at least lvl 21
            if inventory.count("Bow String") >= 1 and inventory.count("Magic Bow (u)") >= 1 and myPlayer.ft_lvl >= 21:       
                os.system('clear')
                print("\n#############")
                print("# Fletching #")
                print("#############\n")
                string("Magic Bow")
                myPlayer.display_stats()
                string_bow_prompt()
                break
            elif myPlayer.ft_lvl < 21:                                                       # level less than 21
                print("You need a Fletching level of at least 21 to make Magic Bows.")
            elif inventory.count("Bow String") < 1 and inventory.count("Magic Bow (u)") < 1: # No Bow String or Bow (u)
                print("You need a Bow String and a Magic Bow (u) to make a Magic Bow.")
            elif inventory.count("Bow String") >= 1 and inventory.count("Magic Bow (u)") < 1:# Has Bow String, no Bow (u)
                print("You need a Magic Bow (u) to make a Magic Bow.")
            else:
                print("You need a Bow String to make a Magic Bow.")                          # No Bow String, has Bow (u)

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
    # Oak Bow
    if bow == "Oak Bow":
        print("You start stringing the Oak Bow", end="")
        # Determine Fletching time
        if myPlayer.ft_lvl < 3:                                 # level 2-3
            skill_wait_time(0)
        elif myPlayer.ft_lvl >= 3 and myPlayer.ft_lvl < 6:      # level 3-6
            skill_wait_time(1)
        elif myPlayer.ft_lvl >= 6 and myPlayer.ft_lvl < 10:     # level 6-10
            skill_wait_time(2)                  
        else:                                                   # level 10+
            skill_wait_time(3)
        removeItem("Bow String")
        removeItem("Oak Bow (u)")
        addToInventory("Oak Bow")
        print("You receive an Oak Bow!")
        myPlayer.ft_xp += items["Oak Bow"]["EXPERIENCE"]           
        if myPlayer.ft_xp >= myPlayer.ft_lvlUp:
            myPlayer.fletching_level_up()
        else:
            print("{} XP left to next level.\n".format(myPlayer.ft_lvlUp - myPlayer.ft_xp))

    # Willow Bow
    elif bow == "Willow Bow":
        print("You start stringing the Willow Bow", end='')
        # Determine Fletching time
        if myPlayer.ft_lvl < 8:                                 # level 6-8
            skill_wait_time(0)
        elif myPlayer.ft_lvl >= 8 and myPlayer.ft_lvl < 11:     # level 8-11
            skill_wait_time(1)
        elif myPlayer.ft_lvl >= 11 and myPlayer.ft_lvl < 15:    # level 11-15
            skill_wait_time(2)
        else:                                                   # level 15+
            skill_wait_time(3)
        removeItem("Bow String")
        removeItem("Willow Bow (u)")
        addToInventory("Willow Bow")
        print("You receive a Willow Bow!")
        myPlayer.ft_xp += items["Willow Bow"]["EXPERIENCE"]          
        if myPlayer.ft_xp >= myPlayer.ft_lvlUp:
            myPlayer.fletching_level_up()
        else:
            print("{} XP left to next level.\n".format(myPlayer.ft_lvlUp - myPlayer.ft_xp))

    # Maple Bow
    elif bow == "Maple Bow":
        print("You start stringing the Maple Bow", end="")
        # Determine Fletching time
        if myPlayer.ft_lvl < 13:                                # level 11-13
            skill_wait_time(0)
        elif myPlayer.ft_lvl >= 13 and myPlayer.ft_lvl < 16:    # level 13-16
            skill_wait_time(1)
        elif myPlayer.ft_lvl >= 16 and myPlayer.ft_lvl < 20:    # level 16-20
            skill_wait_time(2)
        else:                                                   # level 20+
            skill_wait_time(3)
        removeItem("Bow String")
        removeItem("Maple Bow (u)")
        addToInventory("Maple Bow")
        print("You receive a Maple Bow!")
        myPlayer.ft_xp += items["Maple Bow"]["EXPERIENCE"]          
        if myPlayer.ft_xp >= myPlayer.ft_lvlUp:
            myPlayer.fletching_level_up()
        else:
            print("{} XP left to next level.\n".format(myPlayer.ft_lvlUp - myPlayer.ft_xp))

    # Yew Bow
    elif bow == "Yew Bow":
        print("You start stringing the Yew Bow", end='')
        # Determine Fletching time
        if myPlayer.ft_lvl < 18:                                # level 16-18
            skill_wait_time(0)
        elif myPlayer.ft_lvl >= 18 and myPlayer.ft_lvl < 21:    # level 18-21
            skill_wait_time(1)
        elif myPlayer.ft_lvl >= 21 and myPlayer.ft_lvl < 23:    # level 21-23
            skill_wait_time(2)
        else:                                                   # level 23+
            skill_wait_time(3)
        removeItem("Bow String")
        removeItem("Yew Bow (u)")
        addToInventory("Yew Bow")
        print("You receive a Yew Bow!")
        myPlayer.ft_xp += items["Yew Bow"]["EXPERIENCE"]          
        if myPlayer.ft_xp >= myPlayer.ft_lvlUp:
            myPlayer.fletching_level_up()
        else:
            print("{} XP left to next level.\n".format(myPlayer.ft_lvlUp - myPlayer.ft_xp))

    # Magic Bow
    elif bow == "Magic Bow":
        print("You start stringing the Magic Bow", end='')
        # Determine Fletching time
        if myPlayer.ft_lvl < 23:                                # level 21-23
            skill_wait_time(0)
        elif myPlayer.ft_lvl >= 23 and myPlayer.ft_lvl < 24:    # level 23
            skill_wait_time(1)
        elif myPlayer.ft_lvl >= 24 and myPlayer.ft_lvl < 25:    # level 24
            skill_wait_time(2)
        else:                                                   # level 25
            skill_wait_time(3)
        removeItem("Bow String")
        removeItem("Magic Bow (u)")
        addToInventory("Magic Bow")
        print("You receive a Magic Bow!")
        myPlayer.ft_xp += items["Magic Bow"]["EXPERIENCE"]        
        if myPlayer.ft_xp >= myPlayer.ft_lvlUp:
            myPlayer.fletching_level_up()
        else:
            print("{} XP left to next level.\n".format(myPlayer.ft_lvlUp - myPlayer.ft_xp))