import cmd
import textwrap
import sys
import os
import time
import random
from character.player import *
from character.enemy import *
from prompts.prompts import *
from gameplay.inventory import *

##### Combat #####

# Base combat state
def combat_state(enemy):
    myPlayer.display_stats()
    print("What would you like to do?")
    print("1) Melee Attack")
    print("2) Range Attack")
    print("3) Magic")
    print("4) Item")
    print("5) Flee")
    while True:
        action = input("> ")
        if action == '1':       # Melee
            melee_attack(enemy)
            break
        elif action == '2':     # Range
            if myPlayer.range_weapon == "None":         # Check if Player has bow equipped
                print("You don't have a Bow equipped.")
                continue
            else:
                range_attack(enemy)
                break
        elif action == '3':     # Magic
            magic_prompt(enemy)
            break
        elif action == '4':     # Item
            item_prompt(enemy)
            break
        elif action == '5':     # Flee
            if flee():
                os.system('clear')
                print_location()
                print("You successfully escaped the {}!\n".format(enemy.name))
                myPlayer.display_stats()
                break
            else:
                os.system('clear')
                print("\n##########")
                print("# Combat #")
                print("##########\n")
                print("Your attempt to flee the {} was unsuccessful!".format(enemy.name))
                enemy.display_stats()
                enemy_attack(enemy)
                combat_state(enemy)
                break
        else:
            print("Please enter a valid action")
            continue

# Melee Attack function
def melee_attack(enemy):
    if miss():
        damage = 0
    elif myPlayer.melee_weapon == "None":
        damage = random.randrange(1, myPlayer.strength * 2 + 1)
    else:
        damage = random.randrange(1, myPlayer.strength * 2 + items[myPlayer.melee_weapon]["DAMAGE"] + 1)
    enemy.hp -= damage
    os.system('clear')
    if damage == 0:
        print("\n##########")
        print("# Combat #")
        print("##########\n")
        print("You miss your attack!")
        enemy.display_stats()
        enemy_attack(enemy)
        combat_state(enemy)
    elif enemy.is_dead():
        combat_victory(enemy)
    else:
        print("\n##########")
        print("# Combat #")
        print("##########\n")
        print("You hit the {} for {} damage!".format(enemy.name, damage))
        enemy.display_stats()
        enemy_attack(enemy)
        combat_state(enemy)

# Miss Function to determine if Player attack misses
# Returns True if 0 is randomly chosen, False otherwise
def miss():
    if myPlayer.agility < 5:                                # Agility < 5
        rng = random.randrange(3)   # 25% chance
        if rng == 0:
            return True
        else:
            return False
    elif myPlayer.agility >= 5 and myPlayer.agility < 10:   # Agility level (5-9)
        rng = random.randrange(6)   # 14% chance
        if rng == 0:
            return True
        else:
            return False
    elif myPlayer.agility >= 10 and myPlayer.agility < 15:  # Agility level (10-14)
        rng = random.randrange(9)   # 10% chance
        if rng == 0:
            return True
        else:
            return False
    elif myPlayer.agility >= 15 and myPlayer.agility < 20:  # Agility level (15-19)
        rng = random.randrange(12)  # 7.7% chance
        if rng == 0:
            return True
        else:
            return False
    elif myPlayer.agility >= 20 and myPlayer.agility < 25:  # Agility level (20-24)
        rng = random.randrange(15)  # 6.25% chance
        if rng == 0:
            return True
        else:
            return False
    elif myPlayer.agility == 25:                            # Agility max level (25)
        rng = random.randrange(20)  # 4.8% chance
        if rng == 0:
            return True
        else:
            return False

# Range Attack function
def range_attack(enemy):
    if miss():
        damage = 0
    else:
        damage = random.randrange(1, myPlayer.agility * 2 + items[myPlayer.range_weapon]["DAMAGE"] + 1)
    enemy.hp -= damage
    os.system('clear')
    if damage == 0:
        print("\n##########")
        print("# Combat #")
        print("##########\n")
        print("You miss your shot!")
        enemy.display_stats()
        enemy_attack(enemy)
        combat_state(enemy)
    elif enemy.is_dead():
        combat_victory(enemy)
    else:
        print("\n##########")
        print("# Combat #")
        print("##########\n")
        print("Your arrow strikes the {} for {} damage!".format(enemy.name, damage))
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
    if miss():
        damage = 0
    elif myPlayer.magic_weapon == "None":
        damage = random.randrange(1, myPlayer.magic * 2 + 5)
    else:
        damage = random.randrange(1, myPlayer.magic * 2 + items[myPlayer.magic_weapon]["DAMAGE"] + 5)
    enemy.hp -= damage
    os.system('clear')
    if damage == 0:
        print("\n##########")
        print("# Combat #")
        print("##########\n")
        print("Your fireball misses the {}!".format(enemy.name))
        enemy.display_stats()
        enemy_attack(enemy)
        combat_state(enemy)
    elif enemy.is_dead():
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
    if miss():
        damage = 0
    elif myPlayer.magic_weapon == "None":
        damage = random.randrange(1, myPlayer.magic * 2 + 9)
    else:
        damage = random.randrange(1, myPlayer.magic * 2 + items[myPlayer.magic_weapon]["DAMAGE"] + 9)
    enemy.hp -= damage
    os.system('clear')
    if damage == 0:
        print("\n##########")
        print("# Combat #")
        print("##########\n")
        print("Your icebolt misses the {}!".format(enemy.name))
        enemy.display_stats()
        enemy_attack(enemy)
        combat_state(enemy)
    if enemy.is_dead():
        combat_victory(enemy)
    else:
        print("\n##########")
        print("# Combat #")
        print("##########\n")
        print("You hit the {} with an icebolt for {} damage!".format(enemy.name, damage))
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

# Item prompt
def item_prompt(enemy):
    os.system('clear')
    print("\n##########")
    print("# Combat #")
    print("##########\n")
    enemy.display_stats()
    myPlayer.display_stats()
    print("What item would you like to use?")
    print("1) Health Potion         ({})".format(inventory.count("Health Potion")))
    print("2) Mana Potion           ({})".format(inventory.count("Mana Potion")))
    print("3) Super Health Potion   ({})".format(inventory.count("Super Health Potion")))
    print("4) Super Mana Potion     ({})".format(inventory.count("Super Mana Potion")))
    print("5) Restore Potion        ({})".format(inventory.count("Restore Potion")))
    print("6) Back")

    while True:
        action = input("> ")
        if action == '1':       # Health potion
            if "Health Potion" not in inventory:
                print("You don't have a Health Potion.")
                continue
            elif myPlayer.hp == myPlayer.max_hp:
                print("Already at full HP.")
                continue
            else:
                if myPlayer.hp + items["Health Potion"]["EFFECT"] > myPlayer.max_hp:      #Prevent overhealing
                    healed = myPlayer.max_hp - myPlayer.hp
                    myPlayer.hp = myPlayer.max_hp
                else:
                    healed = items["Health Potion"]["EFFECT"]
                    myPlayer.hp += healed
                removeItem("Health Potion")
                os.system('clear')
                print("\n##########")
                print("# Combat #")
                print("##########\n")
                print("You drink the potion and heal for {} HP!".format(healed))
                enemy.display_stats()
                enemy_attack(enemy)
                combat_state(enemy)
                break
        elif action == '2':     # Mana potion
            if "Mana Potion" not in inventory:
                print("You don't have a Mana Potion.")
                continue
            elif myPlayer.mp == myPlayer.max_mp:
                print("Already at full MP.")
                continue
            else:
                if myPlayer.mp + items["Mana Potion"]["EFFECT"] > myPlayer.max_mp:      #Prevent mana overflow
                    mana = myPlayer.max_mp - myPlayer.mp
                    myPlayer.mp = myPlayer.max_mp
                else:
                    mana = items["Mana Potion"]["EFFECT"]
                    myPlayer.mp += mana
                removeItem("Mana Potion")
                os.system('clear')
                print("\n##########")
                print("# Combat #")
                print("##########\n")
                print("You drink the potion and gain {} MP!".format(mana))
                enemy.display_stats()
                enemy_attack(enemy)
                combat_state(enemy)
                break
        elif action == '3':     # Super health
            if "Super Health Potion" not in inventory:
                print("You don't have a Super Health Potion.")
                continue
            elif myPlayer.hp == myPlayer.max_hp:
                print("Already at full HP.")
                continue
            else:
                myPlayer.hp = items["Super Health Potion"]["EFFECT"]
                removeItem("Super Health Potion")
                os.system('clear')
                print("\n##########")
                print("# Combat #")
                print("##########\n")
                print("You drink the potion and heal fully!")
                enemy.display_stats()
                enemy_attack(enemy)
                combat_state(enemy)
                break
        elif action == '4':     # Super mana
            if "Super Mana Potion" not in inventory:
                print("You don't have a Super Mana Potion.")
                continue
            elif myPlayer.mp == myPlayer.max_mp:
                print("Already at full MP.")
                continue
            else:
                myPlayer.mp = items["Super Mana Potion"]["EFFECT"]
                removeItem("Super Mana Potion")
                os.system('clear')
                print("\n##########")
                print("# Combat #")
                print("##########\n")
                print("You drink the potion and gain all your mana!")
                enemy.display_stats()
                enemy_attack(enemy)
                combat_state(enemy)
                break
        elif action == '5':     # Restore potion
            if "Restore Potion" not in inventory:
                print("You don't have a Restore Potion.")
                continue
            elif myPlayer.hp == myPlayer.max_hp and myPlayer.mp == myPlayer.max_mp:
                print("Already at full HP and MP.")
                continue
            else:
                myPlayer.hp = items["Restore Potion"]["EFFECT"]
                myPlayer.mp = items["Restore Potion"]["EFFECT_2"]
                removeItem("Restore Potion")
                os.system('clear')
                print("\n##########")
                print("# Combat #")
                print("##########\n")
                print("You drink the potion and gain full health and mana!")
                enemy.display_stats()
                enemy_attack(enemy)
                combat_state(enemy)
                break
        elif action == '6':     # Back
            os.system('clear')
            print("\n##########")
            print("# Combat #")
            print("##########\n")
            enemy.display_stats()
            combat_state(enemy)
            break
        else:                   # Input Validation
            print("Please enter a valid item")
            continue

# Flee function to determine if Player successfully flees from Combat
# Returns True if 0 is randomly chosen, False otherwise
def flee():
    if myPlayer.agility < 5:                                # Agility < 5
        rng = random.randrange(20)   # 4.8% chance
        if rng == 0:
            return True
        else:
            return False
    elif myPlayer.agility >= 5 and myPlayer.agility < 10:   # Agility level (5-9)
        rng = random.randrange(15)   # 6.25% chance
        if rng == 0:
            return True
        else:
            return False
    elif myPlayer.agility >= 10 and myPlayer.agility < 15:  # Agility level (10-14)
        rng = random.randrange(12)   # 7.7% chance
        if rng == 0:
            return True
        else:
            return False
    elif myPlayer.agility >= 15 and myPlayer.agility < 20:  # Agility level (15-19)
        rng = random.randrange(9)  # 10% chance
        if rng == 0:
            return True
        else:
            return False
    elif myPlayer.agility >= 20 and myPlayer.agility < 25:  # Agility level (20-24)
        rng = random.randrange(6)  # 14% chance
        if rng == 0:
            return True
        else:
            return False
    elif myPlayer.agility == 25:                            # Agility max level (25)
        rng = random.randrange(3)  # 25% chance
        if rng == 0:
            return True
        else:
            return False

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
