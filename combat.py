import cmd
import textwrap
import sys
import os
import time
import random
from player import *
from enemy import *

##### Combat #####

# Base combat state
def combat_state(enemy):
    myPlayer.display_stats()
    print('==========================')
    print("What would you like to do?")
    print("1) Attack")
    print("2) Magic")
    print("3) Items-")
    
    while True:
        action = input("> ")
        if action == '1':
            attack(enemy)
            break
        elif action == '2':
            print("Magic")
        elif action == '3':
            print("Items")
        else:
            print("Please enter a valid action")
            continue

# Attack function
def attack(enemy):
    damage = myPlayer.strength * 2
    enemy.hp -= damage
    os.system('clear')
    if enemy.is_dead():
        combat_victory(enemy)
    else:
        print("You hit the {} for {} damage!".format(enemy.name, damage))
        enemy.display_stats()
        enemy_attack(enemy)
        combat_state(enemy)

# Enemy attack function
def enemy_attack(enemy):
    damage = enemy.damage
    myPlayer.hp -= damage
    if myPlayer.is_dead():
        os.system('clear')
        combat_defeat(enemy)
    else:
        print("The {} hit you for {} damage!".format(enemy.name, damage))

# Combat Victory Function
def combat_victory(enemy):
    print("You killed the {}!".format(enemy.name))
    print("You receive {} gold!".format(enemy.gold))
    myPlayer.gold += enemy.gold

# Combat Defeat function
def combat_defeat(enemy):
    print("You were killed by the {}!".format(enemy.name))
    sys.exit()