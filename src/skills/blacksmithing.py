from prompts.clear_console import *
from character.player import *
from gameplay.inventory import *
from skills.skill_wait_time import *

##### Blacksmithing #####

# Blacksmithing prompt
def blacksmithing_prompt():
    print("What would you like to do?")
    print("1) Forge")
    print("2) Smith")
    print("3) View Inventory")
    print("4) Back")
    while True:
        action = input('> ')
        if action == '1':       # Forge
            if any(i in ["Copper Ore", "Iron Ore", "Silver Ore", "Gold Ore", "Diamond Ore"] for i in inventory):    # Check if player has ore
                clearConsole()
                print("\n#################")
                print("# Blacksmithing #")
                print("#################\n")
                myPlayer.display_stats()
                forge_prompt()
                break  
            else:
                print("You don't have any ore.")
                continue
        elif action == '2':     # Smith
            if any(i in ["Copper Bar", "Iron Bar", "Silver Bar", "Gold Bar", "Diamond Bar"] for i in inventory):    # Check if player has bars
                clearConsole()
                print("\n#################")
                print("# Blacksmithing #")
                print("#################\n")
                myPlayer.display_stats()
                smith_prompt()
                break  
            else:
                print("You don't have any bars.")
                continue
        elif action == '3':     # Inventory
            clearConsole()
            print("\n#################")
            print("# Blacksmithing #")
            print("#################\n")
            inventory_prompt()
            blacksmithing_prompt()
            break
        elif action == '4':     # Back
            clearConsole()
            break
        else:                   # Input Validation
            print("Please enter a valid ore.")
            continue

# Forge prompt
def forge_prompt():
    print("Which ore would you like to smelt?")
    print('1) Copper Ore')
    print('2) Iron Ore')
    print("3) Silver Ore")
    print("4) Gold Ore")
    print('5) Diamond Ore')
    print('6) View Inventory')
    print('7) Back')
    while True:
        action = input('> ')
        if action == '1':       # Copper Ore
            if inventory.count("Copper Ore") > 0:   # 1 Copper Ore needed
                clearConsole()
                print("\n#################")
                print("# Blacksmithing #")
                print("#################\n")
                forge("Copper Ore")
                myPlayer.display_stats()
                forge_prompt()
                break
            else:
                print("You need at least 1 Copper Ore to smelt it into bars.")
        elif action == '2':       # Iron Ore
            if inventory.count("Iron Ore") >= 2 and myPlayer.bs_lvl >= 5:       # 2 Iron Ore and at least lvl 5
                clearConsole()
                print("\n#################")
                print("# Blacksmithing #")
                print("#################\n")
                forge("Iron Ore")
                myPlayer.display_stats()
                forge_prompt()
                break
            elif myPlayer.bs_lvl < 5:
                print("You need a Blacksmithing level of at least 5 to smelt Iron Ore.")
            else:
                print("You need at least 2 Iron Ore to smelt it into bars.")
        elif action == '3':       # Silver Ore
            if inventory.count("Silver Ore") >= 3 and myPlayer.bs_lvl >= 10:    # 3 Silver Ore and at least lvl 10
                clearConsole()
                print("\n#################")
                print("# Blacksmithing #")
                print("#################\n")
                forge("Silver Ore")
                myPlayer.display_stats()
                forge_prompt()
                break
            elif myPlayer.bs_lvl < 10:
                print("You need a Blacksmithing level of at least 10 to smelt Silver Ore.")
            else:
                print("You need at least 3 Silver Ore to smelt it into bars.")
        elif action == '4':       # Gold Ore
            if inventory.count("Gold Ore") >= 4 and myPlayer.bs_lvl >= 15:      # 4 Gold Ore and at least lvl 15
                clearConsole()
                print("\n#################")
                print("# Blacksmithing #")
                print("#################\n")
                forge("Gold Ore")
                myPlayer.display_stats()
                forge_prompt()
                break
            elif myPlayer.bs_lvl < 15:
                print("You need a Blacksmithing level of at least 15 to smelt Gold Ore.")
            else:
                print("You need at least 4 Gold Ore to smelt it into bars.")
        elif action == '5':       # Diamond Ore
            if inventory.count("Diamond Ore") >= 5 and myPlayer.bs_lvl >= 20:   # 5 Diamond Ore and at least lvl 20
                clearConsole()
                print("\n#################")
                print("# Blacksmithing #")
                print("#################\n")
                forge("Diamond Ore")
                myPlayer.display_stats()
                forge_prompt()
                break
            elif myPlayer.bs_lvl < 20:
                print("You need a Blacksmithing level of at least 20 to smelt Diamond Ore.")
            else:
                print("You need at least 5 Diamond Ore to smelt it into bars")
        elif action == '6':     # Inventory
            clearConsole()
            print("\n#################")
            print("# Blacksmithing #")
            print("#################\n")
            inventory_prompt()
            forge_prompt()
            break
        elif action == '7':     # Back
            clearConsole()
            print("\n#################")
            print("# Blacksmithing #")
            print("#################\n")
            myPlayer.display_stats()
            blacksmithing_prompt()
            break
        else:                   # Input Validation
            print("Please enter a valid ore.")
            continue

# Forging function
def forge(ore):
    # Copper Ore
    if ore == "Copper Ore":
        print("You start smelting the Copper Ore in the forge", end="")
        # Determine Blacksmithing time
        if myPlayer.bs_lvl < 2:                                 # level 1-2
            skill_wait_time(0)
        elif myPlayer.bs_lvl >= 2 and myPlayer.bs_lvl < 5:      # level 2-5
            skill_wait_time(1)
        elif myPlayer.bs_lvl >= 5 and myPlayer.bs_lvl < 9:      # level 5-9
            skill_wait_time(2)                  
        else:                                                   # level 9+
            skill_wait_time(3)
        
        # Remove ore from inventory
        removeItem(ore)     # -1 Copper ore
        addToInventory("Copper Bar")
        print("You receive a Copper Bar!")
        myPlayer.bs_xp += items["Copper Bar"]["EXPERIENCE"]
        if myPlayer.bs_lvl < myPlayer.max_level:      
            if myPlayer.bs_xp >= myPlayer.bs_lvlUp:
                myPlayer.blacksmithing_level_up()
            else:
                print("{} XP left to next level.\n".format(myPlayer.bs_lvlUp - myPlayer.bs_xp))

    # Iron Ore
    elif ore == "Iron Ore":
        print("You start smelting the Iron Ore in the forge", end='')
        # Determine Blacksmithing time
        if myPlayer.bs_lvl < 7:                                 # level 5-7
            skill_wait_time(0)
        elif myPlayer.bs_lvl >= 7 and myPlayer.bs_lvl < 10:     # level 7-10
            skill_wait_time(1)
        elif myPlayer.bs_lvl >= 10 and myPlayer.bs_lvl < 14:    # level 10-14
            skill_wait_time(2)
        else:                                                   # level 14+
            skill_wait_time(3)

        # Remove ore from inventory
        for i in range(2):  # -2 Iron ore
            removeItem(ore)
        addToInventory("Iron Bar")
        print("You receive an Iron Bar!")
        myPlayer.bs_xp += items["Iron Bar"]["EXPERIENCE"]
        if myPlayer.bs_lvl < myPlayer.max_level:       
            if myPlayer.bs_xp >= myPlayer.bs_lvlUp:
                myPlayer.blacksmithing_level_up()
            else:
                print("{} XP left to next level.\n".format(myPlayer.bs_lvlUp - myPlayer.bs_xp))

    # Silver Ore
    elif ore == "Silver Ore":
        print("You start smelting the Silver Ore in the forge", end='')
        # Determine Blacksmithing time
        if myPlayer.bs_lvl < 12:                                # level 10-12
            skill_wait_time(0)
        elif myPlayer.bs_lvl >= 12 and myPlayer.bs_lvl < 15:    # level 12-15
            skill_wait_time(1)
        elif myPlayer.bs_lvl >= 15 and myPlayer.bs_lvl < 19:    # level 15-19
            skill_wait_time(2)
        else:                                                   # level 19+
            skill_wait_time(3)

        # Remove ore from inventory
        for i in range(3):  # -3 Silver ore
            removeItem(ore)
        addToInventory("Silver Bar")
        print("You receive a Silver Bar!")
        myPlayer.bs_xp += items["Silver Bar"]["EXPERIENCE"]
        if myPlayer.bs_lvl < myPlayer.max_level:       
            if myPlayer.bs_xp >= myPlayer.bs_lvlUp:
                myPlayer.blacksmithing_level_up()
            else:
                print("{} XP left to next level.\n".format(myPlayer.bs_lvlUp - myPlayer.bs_xp))

    # Gold Ore    
    elif ore == "Gold Ore":
        print("You start smelting the Gold Ore in the forge", end='')
        # Determine Blacksmithing time
        if myPlayer.bs_lvl < 17:                                # level 15-17
            skill_wait_time(0)
        elif myPlayer.bs_lvl >= 17 and myPlayer.bs_lvl < 20:    # level 17-20
            skill_wait_time(1)
        elif myPlayer.bs_lvl >= 20 and myPlayer.bs_lvl < 22:    # level 20-22
            skill_wait_time(2)
        else:                                                   # level 22+
            skill_wait_time(3)

        # Remove ore from inventory
        for i in range(4):  # -4 Gold ore
            removeItem(ore)
        addToInventory("Gold Bar")
        print("You receive a Gold Bar!")
        myPlayer.bs_xp += items["Gold Bar"]["EXPERIENCE"]
        if myPlayer.bs_lvl < myPlayer.max_level:       
            if myPlayer.bs_xp >= myPlayer.bs_lvlUp:
                myPlayer.blacksmithing_level_up()
            else:
                print("{} XP left to next level.\n".format(myPlayer.bs_lvlUp - myPlayer.bs_xp))

    # Diamond Ore
    elif ore == "Diamond Ore":
        print("You start smelting the Diamond Ore in the forge", end='')
        # Determine Blacksmithing time
        if myPlayer.bs_lvl < 22:                                # level 20-22
            skill_wait_time(0)
        elif myPlayer.bs_lvl >= 22 and myPlayer.bs_lvl < 23:    # level 22
            skill_wait_time(1)
        elif myPlayer.bs_lvl >= 23 and myPlayer.bs_lvl < 24:    # level 23
            skill_wait_time(2)
        else:                                                   # level 24+
            skill_wait_time(3)

        # Remove ore from inventory
        for i in range(5):  # -5 Diamond ore
            removeItem(ore)
        addToInventory("Diamond Bar")
        print("You receive a Diamond Bar!")
        myPlayer.bs_xp += items["Diamond Bar"]["EXPERIENCE"]
        if myPlayer.bs_lvl < myPlayer.max_level:      
            if myPlayer.bs_xp >= myPlayer.bs_lvlUp:
                myPlayer.blacksmithing_level_up()
            else:
                print("{} XP left to next level.\n".format(myPlayer.bs_lvlUp - myPlayer.bs_xp))

# Smith prompt
def smith_prompt():
    print("What would you like to make?")
    print('1) Helmet (2 Bars)')
    print('2) Sword (3 Bars)')
    print("3) Platelegs (4 Bars)")
    print("4) Platebody (5 Bars)")
    print('5) View Inventory')
    print('6) Back')
    while True:
        action = input('> ')
        if action == '1':       # Helmet
            clearConsole()
            print("\n#################")
            print("# Blacksmithing #")
            print("#################\n")
            myPlayer.display_stats()
            helmet_prompt()
            break
        elif action == '2':     # Sword
            clearConsole()
            print("\n#################")
            print("# Blacksmithing #")
            print("#################\n")
            myPlayer.display_stats()
            sword_prompt()
            break
        elif action == '3':     # Platelegs
            clearConsole()
            print("\n#################")
            print("# Blacksmithing #")
            print("#################\n")
            myPlayer.display_stats()
            platelegs_prompt()
            break
        elif action == '4':     # Platebody
            clearConsole()
            print("\n#################")
            print("# Blacksmithing #")
            print("#################\n")
            myPlayer.display_stats()
            platebody_prompt()
            break
        elif action == '5':     # Inventory
            clearConsole()
            print("\n#################")
            print("# Blacksmithing #")
            print("#################\n")
            inventory_prompt()
            smith_prompt()
            break
        elif action == '6':     # Back
            clearConsole()
            print("\n#################")
            print("# Blacksmithing #")
            print("#################\n")
            myPlayer.display_stats()
            blacksmithing_prompt()
            break
        else:                   # Input Validation
            print("Please enter a valid ore.")
            continue

# Helmet prompt
def helmet_prompt():
    print("What type of Helmet do you want to make?")
    print('1) Copper')
    print('2) Iron')
    print('3) Silver')
    print('4) Gold')
    print('5) Diamond')
    print('6) View Inventory')
    print('7) Back')
    while True:
        action = input('> ')
        if action == '1':       # Copper
            if inventory.count("Copper Bar") >= 2 and myPlayer.bs_lvl >= 2:     # 2 Copper bars and at least lvl 2
                clearConsole()
                print("\n#################")
                print("# Blacksmithing #")
                print("#################\n")
                smith("Copper Helmet")
                myPlayer.display_stats()
                helmet_prompt()
                break
            elif myPlayer.bs_lvl < 2:
                print("You need a Blacksmithing level of at least 2 to make a Copper Helmet.")
            else:
                print("You need at least 2 Copper Bars to make a Helmet.")
        elif action == '2':       # Iron
            if inventory.count("Iron Bar") >= 2 and myPlayer.bs_lvl >= 6:       # 2 Iron Bars and at least lvl 6
                clearConsole()
                print("\n#################")
                print("# Blacksmithing #")
                print("#################\n")
                smith("Iron Helmet")
                myPlayer.display_stats()
                helmet_prompt()
                break
            elif myPlayer.bs_lvl < 6:
                print("You need a Blacksmithing level of at least 6 to make an Iron Helmet.")
            else:
                print("You need at least 2 Iron Bars to make a Helmet")
        elif action == '3':       # Silver
            if inventory.count("Silver Bar") >= 2 and myPlayer.bs_lvl >= 11:    # 2 Silver Bars and at least lvl 11
                clearConsole()
                print("\n#################")
                print("# Blacksmithing #")
                print("#################\n")
                smith("Silver Helmet")
                myPlayer.display_stats()
                helmet_prompt()
                break
            elif myPlayer.bs_lvl < 11:
                print("You need a Blacksmithing level of at least 11 to make a Silver Helmet")
            else:
                print("You need at least 2 Silver Bars to make a Helmet.")
        elif action == '4':       # Gold
            if inventory.count("Gold Bar") >= 2 and myPlayer.bs_lvl >= 16:      # 2 Gold Bars and at least lvl 16
                clearConsole()
                print("\n#################")
                print("# Blacksmithing #")
                print("#################\n")
                smith("Gold Helmet")
                myPlayer.display_stats()
                helmet_prompt()
                break
            elif myPlayer.bs_lvl < 16:
                print("You need a Blacksmithing level of at least 16 to make a Gold Helmet")
            else:
                print("You need at least 2 Gold Bars to make a Helmet.")
        elif action == '5':       # Diamond
            if inventory.count("Diamond Bar") >= 2 and myPlayer.bs_lvl >= 21:    # 2 Diamond Bars and at least lvl 21
                clearConsole()
                print("\n#################")
                print("# Blacksmithing #")
                print("#################\n")
                smith("Diamond Helmet")
                myPlayer.display_stats()
                helmet_prompt()
                break
            elif myPlayer.bs_lvl < 21:
                print("You need a Blacksmithing level of at least 21 to make a Diamond Helmet")
            else:
                print("You need at least 2 Diamond Bars to make a Helmet.")
        elif action == '6':     # Inventory
            clearConsole()
            print("\n#################")
            print("# Blacksmithing #")
            print("#################\n")
            inventory_prompt()
            helmet_prompt()
            break
        elif action == '7':     # Back
            clearConsole()
            print("\n#################")
            print("# Blacksmithing #")
            print("#################\n")
            myPlayer.display_stats()
            smith_prompt()
            break
        else:                   # Input Validation
            print("Please enter a valid ore.")
            continue

# Sword prompt
def sword_prompt():
    print("What type of Sword do you want to make?")
    print('1) Copper')
    print('2) Iron')
    print('3) Silver')
    print('4) Gold')
    print('5) Diamond')
    print('6) View Inventory')
    print('7) Back')
    while True:
        action = input('> ')
        if action == '1':       # Copper
            if inventory.count("Copper Bar") >= 3 and myPlayer.bs_lvl >= 3:     # 3 Copper bars and at least lvl 3
                clearConsole()
                print("\n#################")
                print("# Blacksmithing #")
                print("#################\n")
                smith("Copper Sword")
                myPlayer.display_stats()
                sword_prompt()
                break
            elif myPlayer.bs_lvl < 3:
                print("You need a Blacksmithing level of at least 3 to make a Copper Sword.")
            else:
                print("You need at least 3 Copper Bars to make a Sword.")
        elif action == '2':       # Iron
            if inventory.count("Iron Bar") >= 3 and myPlayer.bs_lvl >= 7:       # 3 Iron Bars and at least lvl 7
                clearConsole()
                print("\n#################")
                print("# Blacksmithing #")
                print("#################\n")
                smith("Iron Sword")
                myPlayer.display_stats()
                sword_prompt()
                break
            elif myPlayer.bs_lvl < 7:
                print("You need a Blacksmithing level of at least 7 to make an Iron Sword.")
            else:
                print("You need at least 3 Iron Bars to make a Sword")
        elif action == '3':       # Silver
            if inventory.count("Silver Bar") >= 3 and myPlayer.bs_lvl >= 12:    # 3 Silver Bars and at least lvl 12
                clearConsole()
                print("\n#################")
                print("# Blacksmithing #")
                print("#################\n")
                smith("Silver Sword")
                myPlayer.display_stats()
                sword_prompt()
                break
            elif myPlayer.bs_lvl < 12:
                print("You need a Blacksmithing level of at least 12 to make a Silver Sword")
            else:
                print("You need at least 3 Silver Bars to make a Sword.")
        elif action == '4':       # Gold
            if inventory.count("Gold Bar") >= 3 and myPlayer.bs_lvl >= 17:    # 3 Gold Bars and at least lvl 17
                clearConsole()
                print("\n#################")
                print("# Blacksmithing #")
                print("#################\n")
                smith("Gold Sword")
                myPlayer.display_stats()
                sword_prompt()
                break
            elif myPlayer.bs_lvl < 17:
                print("You need a Blacksmithing level of at least 17 to make a Gold Sword")
            else:
                print("You need at least 3 Gold Bars to make a Sword.")
        elif action == '5':       # Diamond
            if inventory.count("Diamond Bar") >= 3 and myPlayer.bs_lvl >= 22:    # 3 Diamond Bars and at least lvl 22
                clearConsole()
                print("\n#################")
                print("# Blacksmithing #")
                print("#################\n")
                smith("Diamond Sword")
                myPlayer.display_stats()
                sword_prompt()
                break
            elif myPlayer.bs_lvl < 22:
                print("You need a Blacksmithing level of at least 22 to make a Diamond Sword")
            else:
                print("You need at least 3 Diamond Bars to make a Sword.")
        elif action == '6':     # Inventory
            clearConsole()
            print("\n#################")
            print("# Blacksmithing #")
            print("#################\n")
            inventory_prompt()
            sword_prompt()
            break
        elif action == '7':     # Back
            clearConsole()
            print("\n#################")
            print("# Blacksmithing #")
            print("#################\n")
            myPlayer.display_stats()
            smith_prompt()
            break
        else:                   # Input Validation
            print("Please enter a valid ore.")
            continue

# Platelegs prompt
def platelegs_prompt():
    print("What type of Platelegs do you want to make?")
    print('1) Copper')
    print('2) Iron')
    print('3) Silver')
    print('4) Gold')
    print('5) Diamond')
    print('6) View Inventory')
    print('7) Back')
    while True:
        action = input('> ')
        if action == '1':       # Copper
            if inventory.count("Copper Bar") >= 4 and myPlayer.bs_lvl >= 4:     # 4 Copper bars and at least lvl 4
                clearConsole()
                print("\n#################")
                print("# Blacksmithing #")
                print("#################\n")
                smith("Copper Platelegs")
                myPlayer.display_stats()
                platelegs_prompt()
                break
            elif myPlayer.bs_lvl < 4:
                print("You need a Blacksmithing level of at least 4 to make Copper Platelegs.")
            else:
                print("You need at least 4 Copper Bars to make a Platelegs.")
        elif action == '2':       # Iron
            if inventory.count("Iron Bar") >= 4 and myPlayer.bs_lvl >= 8:       # 4 Iron Bars and at least lvl 8
                clearConsole()
                print("\n#################")
                print("# Blacksmithing #")
                print("#################\n")
                smith("Iron Platelegs")
                myPlayer.display_stats()
                platelegs_prompt()
                break
            elif myPlayer.bs_lvl < 8:
                print("You need a Blacksmithing level of at least 8 to make Iron Platelegs.")
            else:
                print("You need at least 4 Iron Bars to make a Platelegs")
        elif action == '3':       # Silver
            if inventory.count("Silver Bar") >= 4 and myPlayer.bs_lvl >= 13:    # 4 Silver Bars and at least lvl 13
                clearConsole()
                print("\n#################")
                print("# Blacksmithing #")
                print("#################\n")
                smith("Silver Platelegs")
                myPlayer.display_stats()
                platelegs_prompt()
                break
            elif myPlayer.bs_lvl < 13:
                print("You need a Blacksmithing level of at least 13 to make Silver Platelegs")
            else:
                print("You need at least 4 Silver Bars to make a Platelegs.")
        elif action == '4':       # Gold
            if inventory.count("Gold Bar") >= 4 and myPlayer.bs_lvl >= 18:    # 4 Gold Bars and at least lvl 18
                clearConsole()
                print("\n#################")
                print("# Blacksmithing #")
                print("#################\n")
                smith("Gold Platelegs")
                myPlayer.display_stats()
                platelegs_prompt()
                break
            elif myPlayer.bs_lvl < 18:
                print("You need a Blacksmithing level of at least 18 to make Gold Platelegs")
            else:
                print("You need at least 4 Gold Bars to make a Platelegs.")
        elif action == '5':       # Diamond
            if inventory.count("Diamond Bar") >= 4 and myPlayer.bs_lvl >= 23:    # 4 Diamond Bars and at least lvl 23
                clearConsole()
                print("\n#################")
                print("# Blacksmithing #")
                print("#################\n")
                smith("Diamond Platelegs")
                myPlayer.display_stats()
                platelegs_prompt()
                break
            elif myPlayer.bs_lvl < 23:
                print("You need a Blacksmithing level of at least 23 to make a Diamond Platelegs")
            else:
                print("You need at least 4 Diamond Bars to make a Platelegs.")
        elif action == '6':     # Inventory
            clearConsole()
            print("\n#################")
            print("# Blacksmithing #")
            print("#################\n")
            inventory_prompt()
            platelegs_prompt()
            break
        elif action == '7':     # Back
            clearConsole()
            print("\n#################")
            print("# Blacksmithing #")
            print("#################\n")
            myPlayer.display_stats()
            smith_prompt()
            break
        else:                   # Input Validation
            print("Please enter a valid ore.")
            continue

# Platebody prompt
def platebody_prompt():
    print("What type of Platebody do you want to make?")
    print('1) Copper')
    print('2) Iron')
    print('3) Silver')
    print('4) Gold')
    print('5) Diamond')
    print('6) View Inventory')
    print('7) Back')
    while True:
        action = input('> ')
        if action == '1':       # Copper
            if inventory.count("Copper Bar") >= 5 and myPlayer.bs_lvl >= 5:     # 5 Copper bars and at least lvl 5
                clearConsole()
                print("\n#################")
                print("# Blacksmithing #")
                print("#################\n")
                smith("Copper Platebody")
                myPlayer.display_stats()
                platebody_prompt()
                break
            elif myPlayer.bs_lvl < 5:
                print("You need a Blacksmithing level of at least 5 to make a Copper Platebody.")
            else:
                print("You need at least 5 Copper Bars to make a Platebody.")
        elif action == '2':       # Iron
            if inventory.count("Iron Bar") >= 5 and myPlayer.bs_lvl >= 9:       # 5 Iron Bars and at least lvl 9
                clearConsole()
                print("\n#################")
                print("# Blacksmithing #")
                print("#################\n")
                smith("Iron Platebody")
                myPlayer.display_stats()
                platebody_prompt()
                break
            elif myPlayer.bs_lvl < 9:
                print("You need a Blacksmithing level of at least 9 to make an Iron Platebody.")
            else:
                print("You need at least 5 Iron Bars to make an Platebody")
        elif action == '3':       # Silver
            if inventory.count("Silver Bar") >= 5 and myPlayer.bs_lvl >= 14:    # 5 Silver Bars and at least lvl 14
                clearConsole()
                print("\n#################")
                print("# Blacksmithing #")
                print("#################\n")
                smith("Silver Platebody")
                myPlayer.display_stats()
                platebody_prompt()
                break
            elif myPlayer.bs_lvl < 14:
                print("You need a Blacksmithing level of at least 14 to make a Silver Platebody")
            else:
                print("You need at least 5 Silver Bars to make a Platebody.")
        elif action == '4':       # Gold
            if inventory.count("Gold Bar") >= 5 and myPlayer.bs_lvl >= 19:    # 5 Gold Bars and at least lvl 19
                clearConsole()
                print("\n#################")
                print("# Blacksmithing #")
                print("#################\n")
                smith("Gold Platebody")
                myPlayer.display_stats()
                platebody_prompt()
                break
            elif myPlayer.bs_lvl < 19:
                print("You need a Blacksmithing level of at least 19 to make a Gold Platebody")
            else:
                print("You need at least 5 Gold Bars to make a Platebody.")
        elif action == '5':       # Diamond
            if inventory.count("Diamond Bar") >= 5 and myPlayer.bs_lvl >= 24:    # 5 Diamond Bars and at least lvl 24
                clearConsole()
                print("\n#################")
                print("# Blacksmithing #")
                print("#################\n")
                smith("Diamond Platebody")
                myPlayer.display_stats()
                platebody_prompt()
                break
            elif myPlayer.bs_lvl < 24:
                print("You need a Blacksmithing level of at least 24 to make a Diamond Platebody")
            else:
                print("You need at least 5 Diamond Bars to make a Platebody.")
        elif action == '6':     # Inventory
            clearConsole()
            print("\n#################")
            print("# Blacksmithing #")
            print("#################\n")
            inventory_prompt()
            platebody_prompt()
            break
        elif action == '7':     # Back
            clearConsole()
            print("\n#################")
            print("# Blacksmithing #")
            print("#################\n")
            myPlayer.display_stats()
            smith_prompt()
            break
        else:                   # Input Validation
            print("Please enter a valid ore.")
            continue

# Smithing function
def smith(item):

    ### Helmets ###
    
    # Copper Helmet
    if item == "Copper Helmet":
        print("You start hammering the Copper", end='')
        # Determine Blacksmithing time
        if myPlayer.bs_lvl < 3:                                 # level 2-3
            skill_wait_time(0)
        elif myPlayer.bs_lvl >= 3 and myPlayer.bs_lvl < 6:      # level 3-6
            skill_wait_time(1)
        elif myPlayer.bs_lvl >= 6 and myPlayer.bs_lvl < 10:     # level 6-10
            skill_wait_time(2)                  
        else:                                                   # level 10+
            skill_wait_time(3)

        # Remove bars from inventory
        for i in range(2):  # -2 Copper bars
            removeItem("Copper Bar")
        addToInventory("Copper Helmet")
        print("You receive a Copper Helmet!")
        myPlayer.bs_xp += items["Copper Helmet"]["EXPERIENCE"]
        if myPlayer.bs_lvl < myPlayer.max_level:  
            if myPlayer.bs_xp >= myPlayer.bs_lvlUp:
                myPlayer.blacksmithing_level_up()
            else:
                print("{} XP left to next level.\n".format(myPlayer.bs_lvlUp - myPlayer.bs_xp))

    # Iron Helmet
    elif item == "Iron Helmet":
        print("You start hammering the Iron", end='')
        # Determine Blacksmithing time
        if myPlayer.bs_lvl < 8:                                 # level 6-8
            skill_wait_time(0)
        elif myPlayer.bs_lvl >= 8 and myPlayer.bs_lvl < 11:     # level 8-11
            skill_wait_time(1)
        elif myPlayer.bs_lvl >= 11 and myPlayer.bs_lvl < 15:    # level 11-15
            skill_wait_time(2)
        else:                                                   # level 15+
            skill_wait_time(3)

        # Remove bars from inventory
        for i in range(2):  # -2 Iron bars
            removeItem("Iron Bar")
        addToInventory("Iron Helmet")
        print("You receive an Iron Helmet!")
        myPlayer.bs_xp += items["Iron Helmet"]["EXPERIENCE"] 
        if myPlayer.bs_lvl < myPlayer.max_level: 
            if myPlayer.bs_xp >= myPlayer.bs_lvlUp:
                myPlayer.blacksmithing_level_up()
            else:
                print("{} XP left to next level.\n".format(myPlayer.bs_lvlUp - myPlayer.bs_xp))

    # Silver Helmet
    elif item == "Silver Helmet":
        print("You start hammering the Silver", end='')
        # Determine Blacksmithing time
        if myPlayer.bs_lvl < 13:                                # level 11-13
            skill_wait_time(0)
        elif myPlayer.bs_lvl >= 13 and myPlayer.bs_lvl < 16:    # level 13-16
            skill_wait_time(1)
        elif myPlayer.bs_lvl >= 16 and myPlayer.bs_lvl < 20:    # level 16-20
            skill_wait_time(2)
        else:                                                   # level 20+
            skill_wait_time(3)

        # Remove bars from inventory
        for i in range(2):  # -2 Silver bars
            removeItem("Silver Bar")
        addToInventory("Silver Helmet")
        print("You receive a Silver Helmet!")
        myPlayer.bs_xp += items["Silver Helmet"]["EXPERIENCE"] 
        if myPlayer.bs_lvl < myPlayer.max_level: 
            if myPlayer.bs_xp >= myPlayer.bs_lvlUp:
                myPlayer.blacksmithing_level_up()
            else:
                print("{} XP left to next level.\n".format(myPlayer.bs_lvlUp - myPlayer.bs_xp))

    # Gold Helmet
    elif item == "Gold Helmet":
        print("You start hammering the Gold", end='')
        # Determine Blacksmithing time
        if myPlayer.bs_lvl < 18:                                # level 16-18
            skill_wait_time(0)
        elif myPlayer.bs_lvl >= 18 and myPlayer.bs_lvl < 21:    # level 18-21
            skill_wait_time(1)
        elif myPlayer.bs_lvl >= 21 and myPlayer.bs_lvl < 23:    # level 21-23
            skill_wait_time(2)
        else:                                                   # level 23+
            skill_wait_time(3)

        # Remove bars from inventory
        for i in range(2):  # -2 Gold bars
            removeItem("Gold Bar")
        addToInventory("Gold Helmet")
        print("You receive a Gold Helmet!")
        myPlayer.bs_xp += items["Gold Helmet"]["EXPERIENCE"]
        if myPlayer.bs_lvl < myPlayer.max_level:    
            if myPlayer.bs_xp >= myPlayer.bs_lvlUp:
                myPlayer.blacksmithing_level_up()
            else:
                print("{} XP left to next level.\n".format(myPlayer.bs_lvlUp - myPlayer.bs_xp))

    # Diamond Helmet
    elif item == "Diamond Helmet":
        print("You start hammering the Diamond", end='')
        # Determine Blacksmithing time
        if myPlayer.bs_lvl < 23:                                # level 21-23
            skill_wait_time(0)
        elif myPlayer.bs_lvl >= 23 and myPlayer.bs_lvl < 24:    # level 23
            skill_wait_time(1)
        elif myPlayer.bs_lvl >= 24 and myPlayer.bs_lvl < 25:    # level 24
            skill_wait_time(2)
        else:                                                   # level 25
            skill_wait_time(3)

        # Remove bars from inventory
        for i in range(2):  # -2 Diamond bars
            removeItem("Diamond Bar")
        addToInventory("Diamond Helmet")
        print("You receive a Diamond Helmet!")
        myPlayer.bs_xp += items["Diamond Helmet"]["EXPERIENCE"]
        if myPlayer.bs_lvl < myPlayer.max_level:  
            if myPlayer.bs_xp >= myPlayer.bs_lvlUp:
                myPlayer.blacksmithing_level_up()
            else:
                print("{} XP left to next level.\n".format(myPlayer.bs_lvlUp - myPlayer.bs_xp))


    ### Swords ###

    # Copper Sword
    elif item == "Copper Sword":
        print("You start hammering the Copper", end='')
        # Determine Blacksmithing time
        if myPlayer.bs_lvl < 4:                                 # level 3-4
            skill_wait_time(0)
        elif myPlayer.bs_lvl >= 4 and myPlayer.bs_lvl < 7:      # level 4-7
            skill_wait_time(1)
        elif myPlayer.bs_lvl >= 7 and myPlayer.bs_lvl < 11:     # level 7-11
            skill_wait_time(2)                  
        else:                                                   # level 11+
            skill_wait_time(3)

        # Remove bars from inventory
        for i in range(3):  # -3 Copper bars
            removeItem("Copper Bar")
        addToInventory("Copper Sword")
        print("You receive a Copper Sword!")
        myPlayer.bs_xp += items["Copper Sword"]["EXPERIENCE"] 
        if myPlayer.bs_lvl < myPlayer.max_level:    
            if myPlayer.bs_xp >= myPlayer.bs_lvlUp:
                myPlayer.blacksmithing_level_up()
            else:
                print("{} XP left to next level.\n".format(myPlayer.bs_lvlUp - myPlayer.bs_xp))

    # Iron Sword
    elif item == "Iron Sword":
        print("You start hammering the Iron", end='')
        # Determine Blacksmithing time
        if myPlayer.bs_lvl < 9:                                 # level 7-9
            skill_wait_time(0)
        elif myPlayer.bs_lvl >= 9 and myPlayer.bs_lvl < 12:     # level 9-12
            skill_wait_time(1)
        elif myPlayer.bs_lvl >= 12 and myPlayer.bs_lvl < 16:    # level 12-16
            skill_wait_time(2)
        else:                                                   # level 16+
            skill_wait_time(3)


        # Remove bars from inventory
        for i in range(3):  # -3 Iron bars
            removeItem("Iron Bar")
        addToInventory("Iron Sword")
        print("You receive an Iron Sword!")
        myPlayer.bs_xp += items["Iron Sword"]["EXPERIENCE"] 
        if myPlayer.bs_lvl < myPlayer.max_level:      
            if myPlayer.bs_xp >= myPlayer.bs_lvlUp:
                myPlayer.blacksmithing_level_up()
            else:
                print("{} XP left to next level.\n".format(myPlayer.bs_lvlUp - myPlayer.bs_xp))

    # Silver Sword
    elif item == "Silver Sword":
        print("You start hammering the Silver", end='')
        # Determine Blacksmithing time
        if myPlayer.bs_lvl < 14:                                # level 12-14
            skill_wait_time(0)
        elif myPlayer.bs_lvl >= 14 and myPlayer.bs_lvl < 17:    # level 14-17
            skill_wait_time(1)
        elif myPlayer.bs_lvl >= 17 and myPlayer.bs_lvl < 21:    # level 17-21
            skill_wait_time(2)
        else:                                                   # level 21+
            skill_wait_time(3)

        # Remove bars from inventory
        for i in range(3):  # -3 Silver bars
            removeItem("Silver Bar")
        addToInventory("Silver Sword")
        print("You receive a Silver Sword!")
        myPlayer.bs_xp += items["Silver Sword"]["EXPERIENCE"] 
        if myPlayer.bs_lvl < myPlayer.max_level:     
            if myPlayer.bs_xp >= myPlayer.bs_lvlUp:
                myPlayer.blacksmithing_level_up()
            else:
                print("{} XP left to next level.\n".format(myPlayer.bs_lvlUp - myPlayer.bs_xp))

    # Gold Sword
    elif item == "Gold Sword":
        print("You start hammering the Gold", end='')
        # Determine Blacksmithing time
        if myPlayer.bs_lvl < 19:                                # level 17-19
            skill_wait_time(0)
        elif myPlayer.bs_lvl >= 19 and myPlayer.bs_lvl < 21:    # level 19-21
            skill_wait_time(1)
        elif myPlayer.bs_lvl >= 21 and myPlayer.bs_lvl < 23:    # level 21-23
            skill_wait_time(2)
        else:                                                   # level 23+
            skill_wait_time(3)

        # Remove bars from inventory
        for i in range(3):  # -3 Gold bars
            removeItem("Gold Bar")
        addToInventory("Gold Sword")
        print("You receive a Gold Sword!")
        myPlayer.bs_xp += items["Gold Sword"]["EXPERIENCE"] 
        if myPlayer.bs_lvl < myPlayer.max_level:       
            if myPlayer.bs_xp >= myPlayer.bs_lvlUp:
                myPlayer.blacksmithing_level_up()
            else:
                print("{} XP left to next level.\n".format(myPlayer.bs_lvlUp - myPlayer.bs_xp))

    # Diamond Sword
    elif item == "Diamond Sword":
        print("You start hammering the Diamond", end='')
        # Determine Blacksmithing time
        if myPlayer.bs_lvl < 23:                                # level 22-23
            skill_wait_time(0)
        elif myPlayer.bs_lvl >= 23 and myPlayer.bs_lvl < 24:    # level 23
            skill_wait_time(1)
        elif myPlayer.bs_lvl >= 24 and myPlayer.bs_lvl < 25:    # level 24
            skill_wait_time(2)
        else:                                                   # level 25
            skill_wait_time(3)

        # Remove bars from inventory
        for i in range(3):  # -3 Diamond bars
            removeItem("Diamond Bar")
        addToInventory("Diamond Sword")
        print("You receive a Diamond Sword!")
        myPlayer.bs_xp += items["Diamond Sword"]["EXPERIENCE"] 
        if myPlayer.bs_lvl < myPlayer.max_level:    
            if myPlayer.bs_xp >= myPlayer.bs_lvlUp:
                myPlayer.blacksmithing_level_up()
            else:
                print("{} XP left to next level.\n".format(myPlayer.bs_lvlUp - myPlayer.bs_xp))


    ### Platelegs ###

    # Copper Platelegs
    elif item == "Copper Platelegs":
        print("You start hammering the Copper", end='')
        # Determine Blacksmithing time
        if myPlayer.bs_lvl < 5:                                 # level 4-5
            skill_wait_time(0)
        elif myPlayer.bs_lvl >= 5 and myPlayer.bs_lvl < 8:      # level 5-8
            skill_wait_time(1)
        elif myPlayer.bs_lvl >= 8 and myPlayer.bs_lvl < 12:     # level 8-12
            skill_wait_time(2)                  
        else:                                                   # level 12+
            skill_wait_time(3)

        # Remove bars from inventory
        for i in range(4):  # -4 Copper bars
            removeItem("Copper Bar")
        addToInventory("Copper Platelegs")
        print("You receive Copper Platelegs!")
        myPlayer.bs_xp += items["Copper Platelegs"]["EXPERIENCE"] 
        if myPlayer.bs_lvl < myPlayer.max_level: 
            if myPlayer.bs_xp >= myPlayer.bs_lvlUp:
                myPlayer.blacksmithing_level_up()
            else:
                print("{} XP left to next level.\n".format(myPlayer.bs_lvlUp - myPlayer.bs_xp))

    # Iron Platelegs
    elif item == "Iron Platelegs":
        print("You start hammering the Iron", end='')
        # Determine Blacksmithing time
        if myPlayer.bs_lvl < 10:                                # level 8-10
            skill_wait_time(0)
        elif myPlayer.bs_lvl >= 10 and myPlayer.bs_lvl < 13:    # level 10-13
            skill_wait_time(1)
        elif myPlayer.bs_lvl >= 13 and myPlayer.bs_lvl < 17:    # level 13-17
            skill_wait_time(2)
        else:                                                   # level 17+
            skill_wait_time(3)

        # Remove bars from inventory
        for i in range(4):  # -4 Iron bars
            removeItem("Iron Bar")
        addToInventory("Iron Platelegs")
        print("You receive Iron Platelegs!")
        myPlayer.bs_xp += items["Iron Platelegs"]["EXPERIENCE"] 
        if myPlayer.bs_lvl < myPlayer.max_level:   
            if myPlayer.bs_xp >= myPlayer.bs_lvlUp:
                myPlayer.blacksmithing_level_up()
            else:
                print("{} XP left to next level.\n".format(myPlayer.bs_lvlUp - myPlayer.bs_xp))

    # Silver Platelegs
    elif item == "Silver Platelegs":
        print("You start hammering the Silver", end='')
        # Determine Blacksmithing time
        if myPlayer.bs_lvl < 15:                                # level 13-15
            skill_wait_time(0)
        elif myPlayer.bs_lvl >= 15 and myPlayer.bs_lvl < 18:    # level 15-18
            skill_wait_time(1)
        elif myPlayer.bs_lvl >= 18 and myPlayer.bs_lvl < 22:    # level 18-22
            skill_wait_time(2)
        else:                                                   # level 22+
            skill_wait_time(3)

        # Remove bars from inventory
        for i in range(4):  # -4 Silver bars
            removeItem("Silver Bar")
        addToInventory("Silver Platelegs")
        print("You receive Silver Platelegs!")
        myPlayer.bs_xp += items["Silver Platelegs"]["EXPERIENCE"]
        if myPlayer.bs_lvl < myPlayer.max_level: 
            if myPlayer.bs_xp >= myPlayer.bs_lvlUp:
                myPlayer.blacksmithing_level_up()
            else:
                print("{} XP left to next level.\n".format(myPlayer.bs_lvlUp - myPlayer.bs_xp))

    # Gold Platelegs
    elif item == "Gold Platelegs":
        print("You start hammering the Gold", end='')
        # Determine Blacksmithing time
        if myPlayer.bs_lvl < 20:                                # level 18-20
            skill_wait_time(0)
        elif myPlayer.bs_lvl >= 20 and myPlayer.bs_lvl < 22:    # level 20-22
            skill_wait_time(1)
        elif myPlayer.bs_lvl >= 22 and myPlayer.bs_lvl < 23:    # level 22-23
            skill_wait_time(2)
        else:                                                   # level 23+
            skill_wait_time(3)

        # Remove bars from inventory
        for i in range(4):  # -4 Gold bars
            removeItem("Gold Bar")
        addToInventory("Gold Platelegs")
        print("You receive Gold Platelegs!")
        myPlayer.bs_xp += items["Gold Platelegs"]["EXPERIENCE"]  
        if myPlayer.bs_lvl < myPlayer.max_level:  
            if myPlayer.bs_xp >= myPlayer.bs_lvlUp:
                myPlayer.blacksmithing_level_up()
            else:
                print("{} XP left to next level.\n".format(myPlayer.bs_lvlUp - myPlayer.bs_xp))

    #Diamond Platelegs
    elif item == "Diamond Platelegs":
        print("You start hammering the Diamond", end='')
        # Determine Blacksmithing time
        if myPlayer.bs_lvl < 24:                                # level 23-24
            skill_wait_time(0)
        elif myPlayer.bs_lvl >= 24 and myPlayer.bs_lvl < 25:    # level 24
            skill_wait_time(1)
        else:                                                   # level 25
            skill_wait_time(2)

        # Remove bars from inventory
        for i in range(4):  # -4 Diamond bars
            removeItem("Diamond Bar")
        addToInventory("Diamond Platelegs")
        print("You receive Diamond Platelegs!")
        myPlayer.bs_xp += items["Diamond Platelegs"]["EXPERIENCE"] 
        if myPlayer.bs_lvl < myPlayer.max_level: 
            if myPlayer.bs_xp >= myPlayer.bs_lvlUp:
                myPlayer.blacksmithing_level_up()
            else:
                print("{} XP left to next level.\n".format(myPlayer.bs_lvlUp - myPlayer.bs_xp))


    ### Platebody ###

    # Copper Platebody
    elif item == "Copper Platebody":
        print("You start hammering the Copper", end='')
        # Determine Blacksmithing time
        if myPlayer.bs_lvl < 6:                                 # level 5-6
            skill_wait_time(0)
        elif myPlayer.bs_lvl >= 6 and myPlayer.bs_lvl < 9:      # level 6-9
            skill_wait_time(1)
        elif myPlayer.bs_lvl >= 9 and myPlayer.bs_lvl < 13:     # level 9-13
            skill_wait_time(2)                  
        else:                                                   # level 13+
            skill_wait_time(3)

        # Remove bars from inventory
        for i in range(5):  # -5 Copper bars
            removeItem("Copper Bar")
        addToInventory("Copper Platebody")
        print("You receive a Copper Platebody!")
        myPlayer.bs_xp += items["Copper Platebody"]["EXPERIENCE"] 
        if myPlayer.bs_lvl < myPlayer.max_level: 
            if myPlayer.bs_xp >= myPlayer.bs_lvlUp:
                myPlayer.blacksmithing_level_up()
            else:
                print("{} XP left to next level.\n".format(myPlayer.bs_lvlUp - myPlayer.bs_xp))

    # Iron Platebody
    elif item == "Iron Platebody":
        print("You start hammering the Iron", end='')
        # Determine Blacksmithing time
        if myPlayer.bs_lvl < 11:                                # level 9-11
            skill_wait_time(0)
        elif myPlayer.bs_lvl >= 11 and myPlayer.bs_lvl < 14:    # level 11-14
            skill_wait_time(1)
        elif myPlayer.bs_lvl >= 14 and myPlayer.bs_lvl < 18:    # level 14-18
            skill_wait_time(2)
        else:                                                   # level 18+
            skill_wait_time(3)

        # Remove bars from inventory
        for i in range(5):  # -5 Iron bars
            removeItem("Iron Bar")
        addToInventory("Iron Platebody")
        print("You receive an Iron Platebody!")
        myPlayer.bs_xp += items["Iron Platebody"]["EXPERIENCE"]  
        if myPlayer.bs_lvl < myPlayer.max_level:  
            if myPlayer.bs_xp >= myPlayer.bs_lvlUp:
                myPlayer.blacksmithing_level_up()
            else:
                print("{} XP left to next level.\n".format(myPlayer.bs_lvlUp - myPlayer.bs_xp))

    # Silver Platebody
    elif item == "Silver Platebody":
        print("You start hammering the Silver", end='')
        # Determine Blacksmithing time
        if myPlayer.bs_lvl < 16:                                # level 14-16
            skill_wait_time(0)
        elif myPlayer.bs_lvl >= 16 and myPlayer.bs_lvl < 19:    # level 16-19
            skill_wait_time(1)
        elif myPlayer.bs_lvl >= 19 and myPlayer.bs_lvl < 23:    # level 19-23
            skill_wait_time(2)
        else:                                                   # level 23+
            skill_wait_time(3)

        # Remove bars from inventory
        for i in range(5):  # -5 Silver bars
            removeItem("Silver Bar")
        addToInventory("Silver Platebody")
        print("You receive a Silver Platebody!")
        myPlayer.bs_xp += items["Silver Platebody"]["EXPERIENCE"] 
        if myPlayer.bs_lvl < myPlayer.max_level: 
            if myPlayer.bs_xp >= myPlayer.bs_lvlUp:
                myPlayer.blacksmithing_level_up()
            else:
                print("{} XP left to next level.\n".format(myPlayer.bs_lvlUp - myPlayer.bs_xp))

    # Gold Platebody
    elif item == "Gold Platebody":
        print("You start hammering the Gold", end='')
        # Determine Blacksmithing time
        if myPlayer.bs_lvl < 21:                                # level 19-21
            skill_wait_time(0)
        elif myPlayer.bs_lvl >= 21 and myPlayer.bs_lvl < 23:    # level 21-23
            skill_wait_time(1)
        elif myPlayer.bs_lvl >= 23 and myPlayer.bs_lvl < 24:    # level 23-24
            skill_wait_time(2)
        else:                                                   # level 24+
            skill_wait_time(3)

        # Remove bars from inventory
        for i in range(5):  # -5 Gold bars
            removeItem("Gold Bar")
        addToInventory("Gold Platebody")
        print("You receive a Gold Platebody!")
        myPlayer.bs_xp += items["Gold Platebody"]["EXPERIENCE"]  
        if myPlayer.bs_lvl < myPlayer.max_level:  
            if myPlayer.bs_xp >= myPlayer.bs_lvlUp:
                myPlayer.blacksmithing_level_up()
            else:
                print("{} XP left to next level.\n".format(myPlayer.bs_lvlUp - myPlayer.bs_xp))

    # Diamond Platebody
    elif item == "Diamond Platebody":
        print("You start hammering the Diamond", end='')
        # Determine Blacksmithing time
        if myPlayer.bs_lvl < 25:                                # level 24-25
            skill_wait_time(0)
        else:                                                   # level 25
            skill_wait_time(1)

        # Remove bars from inventory
        for i in range(5):  # -5 Diamond bars
            removeItem("Diamond Bar")
        addToInventory("Diamond Platebody")
        print("You receive a Diamond Platebody!")
        myPlayer.bs_xp += items["Diamond Platebody"]["EXPERIENCE"] 
        if myPlayer.bs_lvl < myPlayer.max_level: 
            if myPlayer.bs_xp >= myPlayer.bs_lvlUp:
                myPlayer.blacksmithing_level_up()
            else:
                print("{} XP left to next level.\n".format(myPlayer.bs_lvlUp - myPlayer.bs_xp))

