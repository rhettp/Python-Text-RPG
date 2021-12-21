from player_movement import *

##### Prompts ##### 

# Town prompt
def town_prompt():
    print('\n==========================')
    print('What would you like to do?')
    print('1) Train')
    print('2) Look')
    print('3) Shop')
    print('4) Travel')
    print('5) Inventory')
    print('6) Character')
    print('7) Quit')
    while True:
        action = input('> ')
        if action == '1':
            print("train")
        elif action == '2':
            print("\n" + world_zone[myPlayer.location][DESCRIPTION])
            town_prompt()
        elif action == '3':
            player_shop()
            break
        elif action == '4':
            player_move()
            break
        elif action == '5':
            print("inventory")
        elif action == '6':
            print("Character")
        elif action == '7':
            sys.exit()
        else:
            print("Please enter a valid action.")
            continue

# Shops prompt
# TODO: Create buy and sell actions
def shop_prompt():
    print('\n==========================')
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
        if action == '1':
            print("buy")
        elif action == '2':
            print("sell")
        elif action == '3':
            print("\n" + shops[myPlayer.location][DESCRIPTION])
            shop_prompt()
        elif action == '4':
            print('inventory')
        elif action == '5':
            print('character')
        elif action == '6':
            myPlayer.location = "Town"
            break
        elif action == '7':
            sys.exit()
        else:
            print("Please enter a valid action.")
            continue