import cmd
import textwrap
import sys
import os
import time
import random
from character.player import *
from character.enemy import *
from prompts.prompts import *

##### Combat #####

# Base combat state
def combat_state(enemy):
    myPlayer.display_stats()
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
            magic_prompt(enemy)
            break
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
        print("\n##########")
        print("# Combat #")
        print("##########\n")
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

# Magic choice prompt
def magic_prompt(enemy):
    os.system('clear')
    print("\n##########")
    print("# Combat #")
    print("##########\n")
    enemy.display_stats()
    myPlayer.display_stats()
    print("What spell would you like to cast?")
    print("1) Fireball")
    print("2) Icebolt")
    print("3) Heal")
    print("4) Back")

    while True:
        action = input("> ")
        if action == '1':       # Fireball
            if myPlayer.mp < 20:
                print("Not enough MP to cast Fireball.")
                continue
            else:
                fireball(enemy)
                break
        elif action == '2':     # Icebolt
            if myPlayer.mp < 30:
                print("Not enough MP to cast Icebolt.")
                continue
            else:
                icebolt(enemy)
                break
        elif action == '3':     # Heal
            if myPlayer.mp < 40:
                print("Not enough MP to cast Heal.")
                continue
            elif myPlayer.hp == myPlayer.max_hp:
                print("Already at full HP.")
                continue
            else:
                heal(enemy)
                break
        elif action == '4':     # Back
            os.system('clear')
            print("\n##########")
            print("# Combat #")
            print("##########\n")
            enemy.display_stats()
            combat_state(enemy)
            break
        else:
            print("Please enter a valid spell")
            continue

# Fireball
def fireball(enemy):
    myPlayer.mp -= 20
    damage = myPlayer.magic * 2
    enemy.hp -= damage
    os.system('clear')
    if enemy.is_dead():
        combat_victory(enemy)
    else:
        print("\n##########")
        print("# Combat #")
        print("##########\n")
        print("You hit the {} with a fireball for {} damage!".format(enemy.name, damage))
        enemy.display_stats()
        enemy_attack(enemy)
        combat_state(enemy)

# Icebolt
def icebolt(enemy):
    myPlayer.mp -= 30
    damage = myPlayer.magic * 2
    enemy.hp -= damage
    os.system('clear')
    if enemy.is_dead():
        combat_victory(enemy)
    else:
        print("\n##########")
        print("# Combat #")
        print("##########\n")
        print("You hit the {} with a iceball for {} damage!".format(enemy.name, damage))
        enemy.display_stats()
        enemy_attack(enemy)
        combat_state(enemy)

# Heal
def heal(enemy):
    myPlayer.mp -= 40
    if myPlayer.hp + 40 > myPlayer.max_hp:      #Prevent overhealing
        healed = myPlayer.max_hp - myPlayer.hp
        myPlayer.hp = myPlayer.max_hp
    else:
        healed = 40
        myPlayer.hp += healed
    os.system('clear')
    print("\n##########")
    print("# Combat #")
    print("##########\n")
    print("You heal yourself for {} HP.".format(healed))
    enemy.display_stats()
    enemy_attack(enemy)
    combat_state(enemy)

# Combat Victory Function
def combat_victory(enemy):
    print_location()
    print("You killed the {}!".format(enemy.name))
    print("You receive {} gold!".format(enemy.gold))
    myPlayer.gold += enemy.gold
    print("You gained {} XP!".format(enemy.xp))
    myPlayer.xp += enemy.xp
    if myPlayer.xp >= myPlayer.lvlUp:
        myPlayer.level_up()
    else:
        print("{} XP left to next level.\n".format(myPlayer.lvlUp - myPlayer.xp))
    myPlayer.display_stats()

# Combat Defeat function
def combat_defeat(enemy):
    print("You were killed by the {}!".format(enemy.name))
    sys.exit()