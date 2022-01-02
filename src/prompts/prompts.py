from gameplay.movement import *
from gameplay.combat import *
from gameplay.inventory import *
from character.enemy import *
from character.player import *

##### Prompts ##### 

# Town prompt
def town_prompt():
    print('What would you like to do?')
    print('1) Shop')
    print('2) Rest')
    print('3) Look')
    print('4) Travel')
    print('5) Inventory')
    print('6) Character')
    print('7) Quit')
    while True:
        action = input('> ')
        if action == '1':       # Shop     
            player_shop()
            os.system('clear')
            print_location()
            myPlayer.display_stats()
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
            myPlayer.display_stats()
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

# Shops prompt
# TODO: Create buy and sell actions
def shop_prompt():
    print_location()
    myPlayer.display_stats()
    print('What would you like to do?')
    print('1) Buy')
    print('2) Sell')
    print('3) Look')
    print('4) Inventory')
    print('5) Character')
    print('6) Leave')
    print('7) Quit')
    while True:
        action = input('> ')
        if action == '1':       # Buy
            print("buy")
        elif action == '2':     # Sell
            print("sell")
        elif action == '3':     # Look
            print("\n" + shops[myPlayer.location][DESCRIPTION])
            shop_prompt()
        elif action == '4':     # Inventory
            os.system('clear')
            print_location()
            myPlayer.display_stats()
            inventory_prompt()
            shop_prompt()
            break
        elif action == '5':     # Character
            print('character')
        elif action == '6':     # Leave
            myPlayer.location = "Town"
            break
        elif action == '7':     # Quit
            sys.exit()
        else:                   # Input Validation
            print("Please enter a valid action.")
            continue

# Forest prompt
def forest_prompt():
    print_location()
    myPlayer.display_stats()
    print('What would you like to do?')
    print('1) Train combat (1-5)')
    print('2) Train woodcutting')
    print('3) Look')
    print('4) Travel')
    print('5) Inventory')
    print('6) Character')
    print('7) Quit')
    while True:
        action = input('> ')
        if action == '1':       # Train
            os.system('clear')
            print('A {} approaches!\n'.format(Goblin().name))
            Goblin().display_stats()
            combat_state(Goblin())
            forest_prompt()
        elif action == '2':     # Woodcut
            print("woodcut")
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
            myPlayer.display_stats()
            inventory_prompt()
            forest_prompt()
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
    print_location()
    myPlayer.display_stats()
    print('What would you like to do?')
    print('1) Train combat (6-10)')
    print('2) Train mining/blacksmithing')
    print('3) Look')
    print('4) Travel')
    print('5) Inventory')
    print('6) Character')
    print('7) Quit')
    while True:
        action = input('> ')
        if action == '1':       # Train
            print("train")
        elif action == '2':     # Mining
            print("mining")
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
            myPlayer.display_stats()
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