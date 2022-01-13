from gameplay.movement import *
from gameplay.combat import *
from gameplay.inventory import *
from character.enemy import *
from character.player import *
from skills.woodcutting import *
from skills.fletching import *
from skills.mining import *
from skills.blacksmithing import *

##### Prompts ##### 

# Town prompt
def town_prompt():
    print('What would you like to do?')
    print('1) Shop')
    print('2) Rest')
    print('3) Look')
    print('4) Travel')
    print('5) View Inventory')
    print('6) Character Info')
    print('7) Quit')
    while True:
        action = input('> ')
        if action == '1':       # Shop     
            os.system('clear')
            print_location()
            myPlayer.display_stats()
            shop_selection()
            town_prompt()
            break
        elif action == '2':     # Rest
            os.system('clear')
            print_location()
            myPlayer.rest()
            myPlayer.display_stats()
            town_prompt()
            break
        elif action == '3':     # Look
            os.system('clear')
            print_location()
            print(world_zone[myPlayer.location]["DESCRIPTION"])
            print("\n")
            myPlayer.display_stats()
            town_prompt()
            break
        elif action == '4':     # Travel
            os.system('clear')
            print_location()
            myPlayer.display_stats()
            player_move()
            prompt_choice()
            break
        elif action == '5':     # Inventory
            os.system('clear')
            print_location()
            inventory_prompt()
            town_prompt()
            break
        elif action == '6':     # Character
            os.system('clear')
            print('\n' + ('#' * (4 + len(myPlayer.name))))
            print('# {} #'.format(myPlayer.name))
            print('#' * (4 + len(myPlayer.name)))
            print("\n")
            myPlayer.character_info()
            myPlayer.display_stats()
            character_prompt()
            town_prompt()
            break
        elif action == '7':     # Quit
            sys.exit()
        else:                   # Input validation
            print("Please enter a valid action.")
            continue

# Shop selection prompt
def shop_selection():
    print("Where would you like to shop?")
    print("1) General Store")
    print("2) Blacksmith")
    print("3) Magic Shop")
    print("4) Back")    # Go back a menu

    while True:
        destination = input('> ')
        if destination == '1':
            myPlayer.location = "General Store"
            os.system('clear')
            print_location()
            myPlayer.display_stats()
            shop_prompt()
            break
        elif destination == '2':
            myPlayer.location = "Blacksmith"
            os.system('clear')
            print_location()
            myPlayer.display_stats()
            shop_prompt()
            break
        elif destination == '3':
            myPlayer.location = "Magic Shop"
            os.system('clear')
            print_location()
            myPlayer.display_stats()
            shop_prompt()
            break
        elif destination == '4':    # Back
            os.system('clear')
            print_location()
            myPlayer.display_stats()
            break
        else:
            print("Please enter a valid shop.")
            continue

# Shopping prompt
def shop_prompt():
    print('What would you like to do?')
    print('1) Buy')
    print('2) Sell')
    print('3) Look')
    print('4) View Inventory')
    print('5) Character Info')
    print('6) Leave')
    print('7) Quit')
    while True:
        action = input('> ')
        if action == '1':       # Buy
            os.system('clear')
            buy_prompt()
            shop_prompt()
            break
        elif action == '2':     # Sell
            os.system('clear')
            if not inventory:   # Empty inventory
                print_location()
                print("Your inventory is empty.\n")
                myPlayer.display_stats()
                shop_prompt()
                break
            else:
                sell_prompt()
                shop_prompt()
                break
        elif action == '3':     # Look
            os.system('clear')
            print_location()
            print(shops[myPlayer.location]["DESCRIPTION"])
            print("\n")
            myPlayer.display_stats()
            shop_prompt()
            break
        elif action == '4':     # Inventory
            os.system('clear')
            print_location()
            inventory_prompt()
            shop_prompt()
            break
        elif action == '5':     # Character
            os.system('clear')
            print('\n' + ('#' * (4 + len(myPlayer.name))))
            print('# {} #'.format(myPlayer.name))
            print('#' * (4 + len(myPlayer.name)))
            print("\n")
            myPlayer.character_info()
            myPlayer.display_stats()
            character_prompt()
            shop_prompt()
            break
        elif action == '6':     # Leave
            os.system('clear')
            myPlayer.location = "Town"
            print_location()
            myPlayer.display_stats()
            town_prompt()
            break
        elif action == '7':     # Quit
            sys.exit()
        else:                   # Input Validation
            print("Please enter a valid action.")
            continue

# Buying prompt
def buy_prompt():
    print_location()
    if myPlayer.location == "General Store":
        if myPlayer.inventory_size == 25:
            print("Big Bag:\t {}".format(items["Big Bag"]["DESCRIPTION"]))
        elif myPlayer.inventory_size == 50:
            print("Bigger Bag:\t {}".format(items["Bigger Bag"]["DESCRIPTION"]))
        elif myPlayer.inventory_size == 75:
            print("Biggest Bag:\t {}".format(items["Biggest Bag"]["DESCRIPTION"]))
        for item in general_store_buy_set:
            print("{}:\t {}".format(item, items[item]["DESCRIPTION"]))
    elif myPlayer.location == "Blacksmith":
        for item in blacksmith_buy_set:
            if item not in ["Copper Platelegs", "Copper Platebody", "Silver Platelegs",\
                "Silver Platebody", "Diamond Platelegs", "Diamond Platebody"]:
                print("{}:\t\t {}".format(item, items[item]["DESCRIPTION"]))
            elif item in ["Copper Platebody", "Silver Platebody"]:
                print("{}: {:>23}".format(item, items[item]["DESCRIPTION"]))
            else:
                print("{}: {:>24}".format(item, items[item]["DESCRIPTION"]))
    else:
        for item in magic_shop_buy_set:
            if item not in ["Super Health Potion", "Super Mana Potion", "Staff"]:
                print("{}:\t\t{}".format(item, items[item]["DESCRIPTION"]))
            elif item != "Staff":
                print("{} {:>25}".format(item, items[item]["DESCRIPTION"]))
            else:
                print("{} {:>31}".format(item, items[item]["DESCRIPTION"]))
    print("\n")
    myPlayer.display_stats()
    print("Which item would you like to buy?")
    while True:
        item = input('> ')
        if item in bag_set:     # Buy inventory upgrade
            os.system('clear')
            print_location()
            print("{}: {} gold\n".format(item, items[item]["VALUE"]))
            myPlayer.display_stats()
            print("Your inventory will increase to {} items.".format(items[item]["SIZE"]))
            print("Would you like to purchase it?")
            while True:
                action = input('> ')
                if action in ["yes","Yes","YES"] and myPlayer.gold >= items[item]["VALUE"]:
                    os.system('clear')
                    print_location()
                    print("You bought the {} for {} gold.".format(item, items[item]["VALUE"]))
                    print("\n")
                    myPlayer.inventory_size = items[item]["SIZE"]
                    myPlayer.gold -= items[item]["VALUE"]
                    myPlayer.display_stats()
                    shop_prompt()
                    break
                elif action in ["yes","Yes","YES"] and myPlayer.gold < items[item]["VALUE"]:
                    print("You don't have enough gold for the {}.".format(item))
                elif action in ["no","No","NO","back","Back","BACK"]:
                    os.system('clear')
                    print_location()
                    print("You did not buy the {}.".format(item))
                    print("\n")
                    myPlayer.display_stats()
                    shop_prompt()
                    break
                else:
                    print("Please enter a valid action.")
                    continue
        elif item in general_store_buy_set or item in blacksmith_buy_set or item in magic_shop_buy_set:
            os.system('clear')
            print_location()
            print("{}: {} gold\n".format(item, items[item]["VALUE"]))
            myPlayer.display_stats()
            print("How many {}(s) do you want to buy?".format(item))
            while True:
                print("> ", end='')
                try:
                    number = int(input())
                except:
                    print("Please enter a valid number.")
                else:
                    if number == 0:         # 0 items
                        os.system('clear')
                        print_location()
                        print("No {}(s) were bought.".format(item))
                        print("\n")
                        myPlayer.display_stats()
                        shop_prompt()
                        break
                    elif number == 1 and myPlayer.gold >= number * items[item]["VALUE"]:       # 1 item
                        os.system('clear')
                        print_location()
                        print("You bought a(n) {} for {} gold.".format(item, items[item]["VALUE"]))
                        print("\n")
                        addToInventory(item)
                        myPlayer.gold -= items[item]["VALUE"]
                        myPlayer.display_stats()
                        shop_prompt()
                        break
                    elif myPlayer.gold < number * items[item]["VALUE"]:                       # Not enough gold
                        print("You don't have enough gold for {} {}(s).".format(number, item))
                        continue
                    elif number > 1 and myPlayer.gold >= number * items[item]["VALUE"]:       # Multiple items
                        os.system('clear')
                        print_location()
                        sum = 0
                        for i in range(number):
                            addToInventory(item)
                            sum += items[item]["VALUE"]
                        myPlayer.gold -= sum
                        print("You bought {} {}(s) for {} gold.".format(number, item, sum))
                        print("\n")
                        myPlayer.display_stats()
                        shop_prompt()
                        break
                    else:
                        print("Please enter a valid number.")
                        continue
            break
        elif item in ["none", "None", "NONE", "back", "Back", "BACK"]:  # Buy no items/go back
            os.system('clear')
            print_location()
            myPlayer.display_stats()
            shop_prompt()
            break
        else:
            print("Please enter a valid item.")
            continue

# Selling prompt
def sell_prompt():
    print_location()
    item_set = set(inventory)
    if myPlayer.location == "General Store":
        for item in item_set:
            if item in general_sell_set:
                print("{} \t({}) : {} gold".format(item, inventory.count(item), items[item]["VALUE"]))
    elif myPlayer.location == "Blacksmith":
        for item in item_set:
            if item in blacksmith_sell_set:
                if item not in ["Copper Platelegs", "Copper Platebody", "Silver Platelegs",\
                "Silver Platebody", "Diamond Platelegs", "Diamond Platebody"]:
                    print("{} \t\t({}) : {} gold".format(item, inventory.count(item), items[item]["VALUE"]))
                else:
                    print("{} \t({}) : {} gold".format(item, inventory.count(item), items[item]["VALUE"]))
    else:
        for item in item_set:
            if item in magic_shop_sell_set:     
                if item not in ["Super Health Potion", "Super Mana Potion", "Staff"]:
                    print("{} \t\t({}) : {} gold".format(item, inventory.count(item), items[item]["VALUE"]))
                elif item != "Staff":
                    print("{} \t({}) : {} gold".format(item, inventory.count(item), items[item]["VALUE"]))
                else:
                    print("{} \t\t\t({}) : {} gold".format(item, inventory.count(item), items[item]["VALUE"]))
    print("\n")
    myPlayer.display_stats()
    print("Which item would you like to sell?")
    while True:
        item = input('> ')
        if item in inventory:
            print("How many {}(s) do you want to sell?".format(item))
            while True:
                print("> ", end='')
                try:
                    number = int(input())
                except:
                    print("Please enter a valid number.")
                else:
                    if number == 0:         # 0 items
                        os.system('clear')
                        print_location()
                        print("No {}(s) were sold.".format(item))
                        print("\n")
                        myPlayer.display_stats()
                        shop_prompt()
                        break
                    elif number == 1:       # 1 item
                        os.system('clear')
                        print_location()
                        print("You sold a(n) {} for {} gold.".format(item, items[item]["VALUE"]))
                        print("\n")
                        removeItem(item)
                        myPlayer.gold += items[item]["VALUE"]
                        myPlayer.display_stats()
                        shop_prompt()
                        break
                    elif number > inventory.count(item):    # More items than in inventory
                        print("You don't have {} {}(s).".format(number, item))
                        continue
                    elif number > 1 and number <= inventory.count(item):    # Multiple items
                        os.system('clear')
                        print_location()
                        sum = 0
                        for i in range(number):
                            removeItem(item)
                            sum += items[item]["VALUE"]
                        myPlayer.gold += sum
                        print("You sold {} {}(s) for {} gold.".format(number, item, sum))
                        print("\n")
                        myPlayer.display_stats()
                        shop_prompt()
                        break
                    else:
                        print("Please enter a valid number.")
                        continue
            break
        elif item in ["all","All", "ALL"]:  # Sell all items
            os.system('clear')
            print_location()
            sum = 0
            for i in inventory:
                sum += items[i]["VALUE"]
            inventory.clear()
            myPlayer.gold += sum
            print("All items were sold for {} gold.".format(sum))
            print("\n")
            myPlayer.display_stats()
            shop_prompt()
            break
        elif item in ["none", "None", "NONE", "back", "Back", "BACK"]:  # Sell no items/go back
            os.system('clear')
            print_location()
            myPlayer.display_stats()
            shop_prompt()
            break
        else:
            print("Please enter a valid item.")
            continue

# Forest prompt
def forest_prompt():
    print('What would you like to do?')
    print('1) Combat (1-5)')
    print('2) Woodcutting')
    print('3) Fletching')
    print('4) Look')
    print('5) Travel')
    print('6) View Inventory')
    print('7) Character Info')
    print('8) Quit')
    while True:
        action = input('> ')
        if action == '1':       # Combat
            os.system('clear')
            print("\n##########")
            print("# Combat #")
            print("##########\n")
            enemy = random.choice(forest_enemies)
            print('A {} approaches!\n'.format(enemy.name))
            enemy.display_stats()
            combat_state(enemy)
            forest_prompt()
            break
        elif action == '2':     # Woodcutting
            os.system('clear')
            print("\n###############")
            print("# Woodcutting #")
            print("###############\n\n")
            myPlayer.display_stats()
            woodcutting_prompt()
            print_location()
            myPlayer.display_stats()
            forest_prompt()
            break
        elif action == '3':     # Fletching
            os.system('clear')
            print("\n#############")
            print("# Fletching #")
            print("#############\n\n")
            myPlayer.display_stats()
            fletching_prompt()
            print_location()
            myPlayer.display_stats()
            forest_prompt()
            break
        elif action == '4':     # Look
            os.system('clear')
            print_location()
            print(world_zone[myPlayer.location]["DESCRIPTION"])
            print("\n")
            myPlayer.display_stats()
            forest_prompt()
            break
        elif action == '5':     # Travel
            os.system('clear')
            print_location()
            myPlayer.display_stats()
            player_move()
            prompt_choice()
            break
        elif action == '6':     # Inventory
            os.system('clear')
            print_location()
            inventory_prompt()
            forest_prompt()
            break
        elif action == '7':     # Character
            os.system('clear')
            print('\n' + ('#' * (4 + len(myPlayer.name))))
            print('# {} #'.format(myPlayer.name))
            print('#' * (4 + len(myPlayer.name)))
            print("\n")
            myPlayer.character_info()
            myPlayer.display_stats()
            character_prompt()
            forest_prompt()
            break
        elif action == '8':     # Exit
            sys.exit()
        else:                   # Input Validation
            print("Please enter a valid action.")
            continue

# Mine prompt
def mine_prompt():
    print('What would you like to do?')
    print('1) Combat (6-10)')
    print('2) Mining')
    print('3) Blacksmithing')
    print('4) Look')
    print('5) Travel')
    print('6) View Inventory')
    print('7) Character Info')
    print('8) Quit')
    while True:
        action = input('> ')
        if action == '1':       # Combat
            os.system('clear')
            print("\n##########")
            print("# Combat #")
            print("##########\n")
            enemy = random.choice(mine_enemies)
            print('A {} approaches!\n'.format(enemy.name))
            enemy.display_stats()
            combat_state(enemy)
            mine_prompt()
            break
        elif action == '2':     # Mining
            os.system('clear')
            print("\n##########")
            print("# Mining #")
            print("##########\n\n")
            myPlayer.display_stats()
            mining_prompt()
            print_location()
            myPlayer.display_stats()
            mine_prompt()
            break
        elif action == '3':      # Blacksmithing
            os.system('clear')
            print("\n#################")
            print("# Blacksmithing #")
            print("#################\n\n")
            myPlayer.display_stats()
            blacksmithing_prompt()
            print_location()
            myPlayer.display_stats()
            mine_prompt()
            break
        elif action == '4':     # Look
            os.system('clear')
            print_location()
            print(world_zone[myPlayer.location]["DESCRIPTION"])
            print("\n")
            myPlayer.display_stats()
            mine_prompt()
            break
        elif action == '5':     # Travel
            os.system('clear')
            print_location()
            myPlayer.display_stats()
            player_move()
            prompt_choice()
            break
        elif action == '6':     # Inventory
            os.system('clear')
            print_location()
            inventory_prompt()
            mine_prompt()
            break
        elif action == '7':     # Character
            os.system('clear')
            print('\n' + ('#' * (4 + len(myPlayer.name))))
            print('# {} #'.format(myPlayer.name))
            print('#' * (4 + len(myPlayer.name)))
            print("\n")
            myPlayer.character_info()
            myPlayer.display_stats()
            character_prompt()
            mine_prompt()
            break
        elif action == '8':     # Exit
            sys.exit()
        else:                   # Input Validation
            print("Please enter a valid action.")
            continue

# Swamp prompt
def swamp_prompt():
    print('What would you like to do?')
    print('1) Combat (11-15)')
    print('2) Look')
    print('3) Travel')
    print('4) View Inventory')
    print('5) Character Info')
    print('6) Quit')
    while True:
        action = input('> ')
        if action == '1':       # Combat
            os.system('clear')
            print("\n##########")
            print("# Combat #")
            print("##########\n")
            enemy = random.choice(swamp_enemies)
            print('A(n) {} approaches!\n'.format(enemy.name))
            enemy.display_stats()
            combat_state(enemy)
            swamp_prompt()
            break
        elif action == '2':     # Look
            os.system('clear')
            print_location()
            print(world_zone[myPlayer.location]["DESCRIPTION"])
            print("\n")
            myPlayer.display_stats()
            swamp_prompt()
            break
        elif action == '3':     # Travel
            os.system('clear')
            print_location()
            myPlayer.display_stats()
            player_move()
            prompt_choice()
            break
        elif action == '4':     # Inventory
            os.system('clear')
            print_location()
            inventory_prompt()
            swamp_prompt()
            break
        elif action == '5':     # Character
            os.system('clear')
            print('\n' + ('#' * (4 + len(myPlayer.name))))
            print('# {} #'.format(myPlayer.name))
            print('#' * (4 + len(myPlayer.name)))
            print("\n")
            myPlayer.character_info()
            myPlayer.display_stats()
            character_prompt()
            swamp_prompt()
            break
        elif action == '6':     # Exit
            sys.exit()
        else:                   # Input Validation
            print("Please enter a valid action.")
            continue

# Graveyard prompt 
def graveyard_prompt():
    print('What would you like to do?')
    print('1) Combat (16-20)')
    print('2) Look')
    print('3) Travel')
    print('4) View Inventory')
    print('5) Character Info')
    print('6) Quit')
    while True:
        action = input('> ')
        if action == '1':       # Combat
            os.system('clear')
            print("\n##########")
            print("# Combat #")
            print("##########\n")
            enemy = random.choice(graveyard_enemies)
            print('A {} approaches!\n'.format(enemy.name))
            enemy.display_stats()
            combat_state(enemy)
            graveyard_prompt()
            break
        elif action == '2':     # Look
            os.system('clear')
            print_location()
            print(world_zone[myPlayer.location]["DESCRIPTION"])
            print("\n")
            myPlayer.display_stats()
            graveyard_prompt()
            break
        elif action == '3':     # Travel
            os.system('clear')
            print_location()
            myPlayer.display_stats()
            player_move()
            prompt_choice()
            break
        elif action == '4':     # Inventory
            os.system('clear')
            print_location()
            inventory_prompt()
            graveyard_prompt()
            break
        elif action == '5':     # Character
            os.system('clear')
            print('\n' + ('#' * (4 + len(myPlayer.name))))
            print('# {} #'.format(myPlayer.name))
            print('#' * (4 + len(myPlayer.name)))
            print("\n")
            myPlayer.character_info()
            myPlayer.display_stats()
            character_prompt()
            graveyard_prompt()
            break
        elif action == '6':     # Exit
            sys.exit()
        else:                   # Input Validation
            print("Please enter a valid action.")
            continue

# Dragon's Lair prompt
def dragon_lair_prompt():
    print('What would you like to do?')
    print('1) Combat (21+)')
    print('2) Look')
    print('3) Travel')
    print('4) View Inventory')
    print('5) Character Info')
    print('6) Quit')
    while True:
        action = input('> ')
        if action == '1':       # Combat
            os.system('clear')
            print("\n##########")
            print("# Combat #")
            print("##########\n")
            enemy = random.choice(lair_enemies)
            print('A {} approaches!\n'.format(enemy.name))
            enemy.display_stats()
            combat_state(enemy)
            dragon_lair_prompt()
            break
        elif action == '2':     # Look
            os.system('clear')
            print_location()
            print(world_zone[myPlayer.location]["DESCRIPTION"])
            print("\n")
            myPlayer.display_stats()
            dragon_lair_prompt()
            break
        elif action == '3':     # Travel
            os.system('clear')
            print_location()
            myPlayer.display_stats()
            player_move()
            prompt_choice()
            break
        elif action == '4':     # Inventory
            os.system('clear')
            print_location()
            inventory_prompt()
            dragon_lair_prompt()
            break
        elif action == '5':     # Character
            os.system('clear')
            print('\n' + ('#' * (4 + len(myPlayer.name))))
            print('# {} #'.format(myPlayer.name))
            print('#' * (4 + len(myPlayer.name)))
            print("\n")
            myPlayer.character_info()
            myPlayer.display_stats()
            character_prompt()
            dragon_lair_prompt()
            break
        elif action == '6':     # Exit
            sys.exit()
        else:                   # Input Validation
            print("Please enter a valid action.")
            continue


# Prompt based on player location
def prompt_choice():
    os.system('clear')
    print_location()
    myPlayer.display_stats()
    if myPlayer.location == "Town":
        town_prompt()
    elif myPlayer.location in ["Blacksmith", "Magic Shop", "General Store"]:
        shop_prompt()
    elif myPlayer.location == "Forest":
        forest_prompt()
    elif myPlayer.location == "Mine":
        mine_prompt()
    elif myPlayer.location == "Swamp":
        swamp_prompt()
    elif myPlayer.location == "Graveyard":
        graveyard_prompt()
    elif myPlayer.location == "Dragon's Lair":
        dragon_lair_prompt()

# Character prompt
def character_prompt():
    print("What would you like to do?")
    print("1) Change Gear")
    print("2) Back")
    while True:
        action = input('> ')
        if action == '1':       # Change Gear
            os.system('clear')
            print('\n' + ('#' * (4 + len(myPlayer.name))))
            print('# {} #'.format(myPlayer.name))
            print('#' * (4 + len(myPlayer.name)))
            print("\n")
            myPlayer.character_info()
            myPlayer.display_stats()
            change_gear_prompt()
            break
        elif action == '2':       # Back
            os.system('clear')
            print_location()
            myPlayer.display_stats()
            break
        else:                   # Input Validation
            print("Please enter a valid action.")
            continue

# Gear change prompt
def change_gear_prompt():
    print("What gear slot would you like to chnage?")
    print("1) Head Slot")
    print("2) Chest Slot")
    print("3) Legs Slot")
    print("4) Melee Weapon Slot")
    print("5) Range Weapon Slot")
    print("6) Magic Weapon Slot")
    print("7) Back")
    while True:
        action = input('> ')
        if action == '1':       # Head Slot
            if any(item in inventory for item in helmet_set):
                head_slot_prompt()
                os.system('clear')
                print('\n' + ('#' * (4 + len(myPlayer.name))))
                print('# {} #'.format(myPlayer.name))
                print('#' * (4 + len(myPlayer.name)))
                print("\n")
                myPlayer.character_info()
                myPlayer.display_stats()
                character_prompt()
                break
            else:
                print("You don't have a Helmet to equip.")
                continue
        elif action == '2':     # Chest Slot
            if any(item in inventory for item in platebody_set):
                chest_slot_prompt()
                os.system('clear')
                print('\n' + ('#' * (4 + len(myPlayer.name))))
                print('# {} #'.format(myPlayer.name))
                print('#' * (4 + len(myPlayer.name)))
                print("\n")
                myPlayer.character_info()
                myPlayer.display_stats()
                character_prompt()
                break
            else:
                print("You don't have a Platebody to equip.")
                continue
        elif action == '3':     # Legs Slot
            if any(item in inventory for item in platelegs_set):
                legs_slot_prompt()
                os.system('clear')
                print('\n' + ('#' * (4 + len(myPlayer.name))))
                print('# {} #'.format(myPlayer.name))
                print('#' * (4 + len(myPlayer.name)))
                print("\n")
                myPlayer.character_info()
                myPlayer.display_stats()
                character_prompt()
                break
            else:
                print("You don't have a set of Platelegs to equip.")
                continue
        elif action == '4':     # Melee Slot
            if any(item in inventory for item in melee_set):
                melee_slot_prompt()
                os.system('clear')
                print('\n' + ('#' * (4 + len(myPlayer.name))))
                print('# {} #'.format(myPlayer.name))
                print('#' * (4 + len(myPlayer.name)))
                print("\n")
                myPlayer.character_info()
                myPlayer.display_stats()
                character_prompt()
                break
            else:
                print("You don't have a Melee Weapon to equip.")
                continue
        elif action == '5':     # Range Slot
            if any(item in inventory for item in range_set):
                range_slot_prompt()
                os.system('clear')
                print('\n' + ('#' * (4 + len(myPlayer.name))))
                print('# {} #'.format(myPlayer.name))
                print('#' * (4 + len(myPlayer.name)))
                print("\n")
                myPlayer.character_info()
                myPlayer.display_stats()
                character_prompt()
                break
            else:
                print("You don't have a Range Weapon to equip.")
                continue
        elif action == '6':     # Magic Slot
            if any(item in inventory for item in staff_set):
                magic_slot_prompt()
                os.system('clear')
                print('\n' + ('#' * (4 + len(myPlayer.name))))
                print('# {} #'.format(myPlayer.name))
                print('#' * (4 + len(myPlayer.name)))
                print("\n")
                myPlayer.character_info()
                myPlayer.display_stats()
                character_prompt()
                break
            else:
                print("You don't have a Magic Weapon to equip.")
                continue
        elif action == '7':     # Back
            os.system('clear')
            print_location()
            myPlayer.display_stats()
            break
        else:                   # Input Validation
            print("Please enter a valid action")
            continue

# Head Slot prompt
def head_slot_prompt():
    os.system('clear')
    print('\n' + ('#' * (4 + len(myPlayer.name))))
    print('# {} #'.format(myPlayer.name))
    print('#' * (4 + len(myPlayer.name)))
    print("\n")
    for item in inventory:
        if item in helmet_set:
            if item != "Diamond Helmet":
                print("{}: \t\t{}".format(item, items[item]["DESCRIPTION"]))
            else:
                print("{}: \t{}".format(item, items[item]["DESCRIPTION"]))
    print("\n")
    myPlayer.display_stats()
    print("Which Helmet would you like to equip?")
    while True:
        item = input('> ')
        if item in inventory and item in helmet_set:
            if myPlayer.head == "None":         # First gear equip
                myPlayer.head = item
                removeItem(item)
                break
            else:
                addToInventory(myPlayer.head)   # Replace gear slot
                myPlayer.head = item
                removeItem(item)
                break
        elif item in ["none", "None", "NONE", "back", "Back", "BACK"]:  # No gear change/go back
            os.system('clear')
            print('\n' + ('#' * (4 + len(myPlayer.name))))
            print('# {} #'.format(myPlayer.name))
            print('#' * (4 + len(myPlayer.name)))
            print("\n")
            myPlayer.character_info()
            myPlayer.display_stats()
            break
        else:
            print("Please enter a valid item.")
            continue

# Chest Slot prompt
def chest_slot_prompt():
    os.system('clear')
    print('\n' + ('#' * (4 + len(myPlayer.name))))
    print('# {} #'.format(myPlayer.name))
    print('#' * (4 + len(myPlayer.name)))
    print("\n")
    for item in inventory:
        if item in platebody_set:
            print("{}: \t{}".format(item, items[item]["DESCRIPTION"]))
    print("\n")
    myPlayer.display_stats()
    print("Which Platebody would you like to equip?")
    while True:
        item = input('> ')
        if item in inventory and item in platebody_set:
            if myPlayer.chest == "None":         # First gear equip
                myPlayer.chest = item
                removeItem(item)
                break
            else:
                addToInventory(myPlayer.chest)   # Replace gear slot
                myPlayer.chest = item
                removeItem(item)
                break
        elif item in ["none", "None", "NONE", "back", "Back", "BACK"]:  # No gear change/go back
            os.system('clear')
            print('\n' + ('#' * (4 + len(myPlayer.name))))
            print('# {} #'.format(myPlayer.name))
            print('#' * (4 + len(myPlayer.name)))
            print("\n")
            myPlayer.character_info()
            myPlayer.display_stats()
            break
        else:
            print("Please enter a valid item.")
            continue

# Legs Slot prompt
def legs_slot_prompt():
    os.system('clear')
    print('\n' + ('#' * (4 + len(myPlayer.name))))
    print('# {} #'.format(myPlayer.name))
    print('#' * (4 + len(myPlayer.name)))
    print("\n")
    for item in inventory:
        if item in platelegs_set:
            print("{}: \t{}".format(item, items[item]["DESCRIPTION"]))
    print("\n")
    myPlayer.display_stats()
    print("Which set of Platelegs would you like to equip?")
    while True:
        item = input('> ')
        if item in inventory and item in platelegs_set:
            if myPlayer.legs == "None":         # First gear equip
                myPlayer.legs = item
                removeItem(item)
                break
            else:
                addToInventory(myPlayer.legs)   # Replace gear slot
                myPlayer.legs = item
                removeItem(item)
                break
        elif item in ["none", "None", "NONE", "back", "Back", "BACK"]:  # No gear change/go back
            os.system('clear')
            print('\n' + ('#' * (4 + len(myPlayer.name))))
            print('# {} #'.format(myPlayer.name))
            print('#' * (4 + len(myPlayer.name)))
            print("\n")
            myPlayer.character_info()
            myPlayer.display_stats()
            break
        else:
            print("Please enter a valid item.")
            continue

# Melee Slot prompt
def melee_slot_prompt():
    os.system('clear')
    print('\n' + ('#' * (4 + len(myPlayer.name))))
    print('# {} #'.format(myPlayer.name))
    print('#' * (4 + len(myPlayer.name)))
    print("\n")
    for item in inventory:
        if item in melee_set:
            print("{}: \t{}".format(item, items[item]["DESCRIPTION"]))
    print("\n")
    myPlayer.display_stats()
    print("Which Melee Weapon would you like to equip?")
    while True:
        item = input('> ')
        if item in inventory and item in melee_set:
            if myPlayer.melee_weapon == "None":         # First gear equip
                myPlayer.melee_weapon = item
                removeItem(item)
                break
            else:
                addToInventory(myPlayer.melee_weapon)   # Replace gear slot
                myPlayer.melee_weapon = item
                removeItem(item)
                break
        elif item in ["none", "None", "NONE", "back", "Back", "BACK"]:  # No gear change/go back
            os.system('clear')
            print('\n' + ('#' * (4 + len(myPlayer.name))))
            print('# {} #'.format(myPlayer.name))
            print('#' * (4 + len(myPlayer.name)))
            print("\n")
            myPlayer.character_info()
            myPlayer.display_stats()
            break
        else:
            print("Please enter a valid item.")
            continue

# Range Slot prompt
def range_slot_prompt():
    os.system('clear')
    print('\n' + ('#' * (4 + len(myPlayer.name))))
    print('# {} #'.format(myPlayer.name))
    print('#' * (4 + len(myPlayer.name)))
    print("\n")
    for item in inventory:
        if item in range_set:
            print("{}: \t{}".format(item, items[item]["DESCRIPTION"]))
    print("\n")
    myPlayer.display_stats()
    print("Which Range Weapon would you like to equip?")
    while True:
        item = input('> ')
        if item in inventory and item in range_set:
            if myPlayer.range_weapon == "None":         # First gear equip
                myPlayer.range_weapon = item
                removeItem(item)
                break
            else:
                addToInventory(myPlayer.range_weapon)   # Replace gear slot
                myPlayer.range_weapon = item
                removeItem(item)
                break
        elif item in ["none", "None", "NONE", "back", "Back", "BACK"]:  # No gear change/go back
            os.system('clear')
            print('\n' + ('#' * (4 + len(myPlayer.name))))
            print('# {} #'.format(myPlayer.name))
            print('#' * (4 + len(myPlayer.name)))
            print("\n")
            myPlayer.character_info()
            myPlayer.display_stats()
            break
        else:
            print("Please enter a valid item.")
            continue

# Magic Slot prompt
def magic_slot_prompt():
    os.system('clear')
    print('\n' + ('#' * (4 + len(myPlayer.name))))
    print('# {} #'.format(myPlayer.name))
    print('#' * (4 + len(myPlayer.name)))
    print("\n")
    for item in inventory:
        if item in staff_set:
            if item == "Staff":
                print("{}: \t\t{}".format(item, items[item]["DESCRIPTION"]))
            else:
                print("{}: \t{}".format(item, items[item]["DESCRIPTION"]))
    print("\n")
    myPlayer.display_stats()
    print("Which Magic Weapon would you like to equip?")
    while True:
        item = input('> ')
        if item in inventory and item in staff_set:
            if myPlayer.magic_weapon == "None":         # First gear equip
                myPlayer.magic_weapon = item
                removeItem(item)
                break
            else:
                addToInventory(myPlayer.magic_weapon)   # Replace gear slot
                myPlayer.magic_weapon = item
                removeItem(item)
                break
        elif item in ["none", "None", "NONE", "back", "Back", "BACK"]:  # No gear change/go back
            os.system('clear')
            print('\n' + ('#' * (4 + len(myPlayer.name))))
            print('# {} #'.format(myPlayer.name))
            print('#' * (4 + len(myPlayer.name)))
            print("\n")
            myPlayer.character_info()
            myPlayer.display_stats()
            break
        else:
            print("Please enter a valid item.")
            continue