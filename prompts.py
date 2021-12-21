from player_movement import *

def prompt():
    print('\n==========================')
    print('What would you like to do?')
    print('1) Train')
    print('2) Travel')
    print('3) Inventory')
    print('4) Character')
    print('5) Quit')
    while True:
        action = input('> ')
        if action == '2':
            player_move()
            break
        elif action == '5':
            sys.exit()
        else:
            print("Please enter a valid action.")
            continue