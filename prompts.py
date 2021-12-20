from player_movement import *

def prompt():
    print('\n' + '==========================')
    print('What would you like to do?')
    print('-Travel-')
    print('-Quit-')
    while True:
        action = input('> ').lower()
        if action == 'travel':
            player_move(action)
            break
        elif action == 'quit':
            sys.exit()
        else:
            print("Please enter a valid action.")
            continue