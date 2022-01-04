from gameplay.movement import *
from gameplay.combat import *
from gameplay.inventory import *
from character.enemy import *
from character.player import *
from skills.woodcutting import *
from skills.mining import *

##### Prompts ##### 

# Town prompt
def town_prompt():
    print('What would you like to do?')
    print('1) Shop')
    print('2) Rest')
    print('3) Look')
    print('4) Travel')
    print('5) View Inventory')
    print('6) Character')
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
            print("You feel rested. Your HP and MP have been restored.\n")
            myPlayer.display_stats()
            town_prompt()
            break
        elif action == '3':     # Look
            os.system('clear')
            print_location()
            print(world_zone[myPlayer.location][DESCRIPTION])
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
            print("Character")
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
# TODO: Create buy and sell actions
def shop_prompt():
    print('What would you like to do?')
    print('1) Buy')
    print('2) Sell')
    print('3) Look')
    print('4) View Inventory')
    print('5) Character')
    print('6) Leave')
    print('7) Quit')
    while True:
        action = input('> ')
        if action == '1':       # Buy
            print("buy")
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
            print(shops[myPlayer.location][DESCRIPTION])
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
            print('character')
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

# Selling prompt
def sell_prompt():
    print_location()
    item_set = set(inventory)
    if myPlayer.location == "General Store":
        for item in item_set:
            if item in ["Oak Log", "Willow Log", "Maple Log", "Yew Log", "Magic Log"]:
                print("{} ({}): {} gold".format(item, inventory.count(item), items[item][VALUE]))
    elif myPlayer.location == "Blacksmith":
        for item in item_set:
            if item in ["Copper Ore", "Iron Ore", "Silver Ore", "Gold Ore", "Diamond Ore", "Copper Bar", "Iron Bar", "Silver Bar", "Gold Bar", "Diamond Bar"]:
                print("{} ({}): {} gold".format(item, inventory.count(item), items[item][VALUE]))
    else:
        print("magic shop sell items")
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
                        print("No {}s were sold.".format(item))
                        print("\n")
                        myPlayer.display_stats()
                        shop_prompt()
                        break
                    elif number == 1:       # 1 item
                        os.system('clear')
                        print_location()
                        print("You sold a(n) {} for {} gold.".format(item, items[item][VALUE]))
                        print("\n")
                        removeItem(item)
                        myPlayer.gold += items[item][VALUE]
                        myPlayer.display_stats()
                        shop_prompt()
                        break
                    elif number > inventory.count(item):    # More items than in inventory
                        print("You don't have {} {}s.".format(number, item))
                        continue
                    elif number > 1 and number <= inventory.count(item):    # Multiple items
                        os.system('clear')
                        print_location()
                        sum = 0
                        for i in range(number):
                            removeItem(item)
                            sum += items[item][VALUE]
                        myPlayer.gold += sum
                        print("You sold {} {}s for {} gold.".format(number, item, sum))
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
                sum += items[i][VALUE]
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
    print('1) Train Combat (1-5)')
    print('2) Train Woodcutting')
    print('3) Look')
    print('4) Travel')
    print('5) View Inventory')
    print('6) Character')
    print('7) Quit')
    while True:
        action = input('> ')
        if action == '1':       # Train
            os.system('clear')
            print("\n##########")
            print("# Combat #")
            print("##########\n")
            print('A {} approaches!\n'.format(Goblin().name))
            Goblin().display_stats()
            combat_state(Goblin())
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
        elif action == '3':     # Look
            os.system('clear')
            print_location()
            print(world_zone[myPlayer.location][DESCRIPTION])
            print("\n")
            myPlayer.display_stats()
            forest_prompt()
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
            print("Character")
        elif action == '7':     # Exit
            sys.exit()
        else:                   # Input Validation
            print("Please enter a valid action.")
            continue

# Mine prompt
def mine_prompt():
    print('What would you like to do?')
    print('1) Train combat (6-10)')
    print('2) Train mining/blacksmithing')
    print('3) Look')
    print('4) Travel')
    print('5) View Inventory')
    print('6) Character')
    print('7) Quit')
    while True:
        action = input('> ')
        if action == '1':       # Train
            print("train")
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
        elif action == '3':     # Look
            os.system('clear')
            print_location()
            print(world_zone[myPlayer.location][DESCRIPTION])
            print("\n")
            myPlayer.display_stats()
            mine_prompt()
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
            mine_prompt()
            break
        elif action == '6':     # Character
            print("Character")
        elif action == '7':     # Exit
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