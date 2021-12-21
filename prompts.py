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