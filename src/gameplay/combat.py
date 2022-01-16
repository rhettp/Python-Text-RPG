import sys
import time
import random
from character.player import *
from character.enemy import *
from prompts.prompts import *
from gameplay.inventory import *
from prompts.clear_console import *

##### Combat #####

# Global variables used for stat xp distribution
used_strength = False
used_agility = False
used_magic = False

# Base combat state
def combat_state(enemy):
    global used_strength, used_agility, used_magic
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
            used_strength = True
            melee_attack(enemy)
            break
        elif action == '2':     # Range
            if myPlayer.range_weapon == "None":         # Check if Player has bow equipped
                print("You don't have a Bow equipped.")
                continue
            else:
                used_agility = True
                range_attack(enemy)
                break
        elif action == '3':     # Magic
            magic_prompt(enemy)
            break
        elif action == '4':     # Item
            item_prompt(enemy)
            break
        elif action == '5':     # Flee
            if flee():  # If successful
                used_strength = False
                used_agility = False
                used_magic = False
                clearConsole()
                print_location()
                print("You successfully escaped the {}!\n".format(enemy.name))
                enemy.hp = enemy.max_hp     # Reset enemy health
                myPlayer.display_stats()
                break
            else:       # Failed to flee
                clearConsole()
                print("\n##########")
                print("# Combat #")
                print("##########\n")
                print("Your attempt to flee the {} was unsuccessful!".format(enemy.name))
                enemy.display_stats()
                enemy_attack(enemy)
                break
        else:
            print("Please enter a valid action")
            continue

# Melee Attack function
def melee_attack(enemy):
    if miss():
        damage = 0
    elif myPlayer.melee_weapon == "None":
        if myPlayer.strength < 6:
            damage = random.randrange(1, 3)
        else:
            damage = random.randrange(1, round(myPlayer.strength / 2))
    else:
        if myPlayer.strength < 3:
            damage = random.randrange(1, round(myPlayer.strength + 1) + round(items[myPlayer.melee_weapon]["DAMAGE"] / 2)) 
        else:
            damage = random.randrange(1, round(myPlayer.strength / 2) + round(items[myPlayer.melee_weapon]["DAMAGE"] / 2) + 1)
    enemy.hp -= damage
    clearConsole()
    if damage == 0:
        print("\n##########")
        print("# Combat #")
        print("##########\n")
        print("You miss your attack!")
        enemy.display_stats()
        enemy_attack(enemy)
    elif enemy.is_dead():
        combat_victory(enemy)
    else:
        print("\n##########")
        print("# Combat #")
        print("##########\n")
        print("You hit the {} for {} damage!".format(enemy.name, damage))
        enemy.display_stats()
        enemy_attack(enemy)

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
        if myPlayer.agility < 3:
            damage = random.randrange(1, round(myPlayer.agility + 1) + round(items[myPlayer.range_weapon]["DAMAGE"] / 2))
        else:
            damage = random.randrange(1, round(myPlayer.agility / 2) + round(items[myPlayer.range_weapon]["DAMAGE"] / 2) + 1)
    enemy.hp -= damage
    clearConsole()
    if damage == 0:
        print("\n##########")
        print("# Combat #")
        print("##########\n")
        print("You miss your shot!")
        enemy.display_stats()
        enemy_attack(enemy)
    elif enemy.is_dead():
        combat_victory(enemy)
    else:
        print("\n##########")
        print("# Combat #")
        print("##########\n")
        print("Your arrow strikes the {} for {} damage!".format(enemy.name, damage))
        enemy.display_stats()
        enemy_attack(enemy)

# Enemy attack function
def enemy_attack(enemy):
    if player_defense() >= 0 and player_defense() < 10:     # 0-9 defense
        damage = random.randrange(enemy.max_hit + 1)
    elif player_defense() >= 10 and player_defense() < 15:  # 10-14 defense
        damage = random.randrange(enemy.max_hit)
    elif player_defense() >= 15 and player_defense() < 20:  # 15-19 defense
        damage = random.randrange(enemy.max_hit - 1)
    elif player_defense() >= 20 and player_defense() < 25:  # 20-24 defense
        if enemy.max_hit - 3 <= 0:
            damage = 0
        else:
            damage = random.randrange(enemy.max_hit - 3)
    elif player_defense() >= 25 and player_defense() < 30:  # 25-29 defense
        if enemy.max_hit - 5 <= 0:
            damage = 0
        else:
            damage = random.randrange(enemy.max_hit - 5)
    elif player_defense() >= 30 and player_defense() < 35:  # 30-34 defense
        if enemy.max_hit - 7 <= 0:
            damage = 0
        else:
            damage = random.randrange(enemy.max_hit - 7)
    elif player_defense() >= 35 and player_defense() < 39:  # 35-38 defense
        if enemy.max_hit - 9 <= 0:
            damage = 0
        damage = random.randrange(enemy.max_hit - 9)
    else:
        if enemy.max_hit - 10 <= 0:
            damage = 0                                      # 39 defense
        else:
            damage = random.randrange(enemy.max_hit - 10)
    myPlayer.hp -= damage
    if damage == 0:
        print("The {} missed its attack!".format(enemy.name))
        combat_state(enemy)
    elif myPlayer.is_dead():
        combat_defeat(enemy)
    else:
        print("The {} hits you for {} damage!".format(enemy.name, damage))
        combat_state(enemy)

# Calculate Player's total defense
def player_defense():
    # No helmet/chest/legs
    if myPlayer.head == "None" and myPlayer.chest == "None" and myPlayer.legs == "None":      
        return 0
    # No helmet and no chest
    elif myPlayer.head == "None" and myPlayer.chest == "None":
        return items[myPlayer.legs]["DEFENSE"]
    # No helmet and no legs
    elif myPlayer.head == "None" and myPlayer.legs == "None":
        return items[myPlayer.chest]["DEFENSE"]
    # No chest and no legs 
    elif myPlayer.chest == "None" and myPlayer.legs == "None":
        return items[myPlayer.head]["DEFENSE"]
    # No head
    elif myPlayer.head == "None":
        return items[myPlayer.chest]["DEFENSE"] + items[myPlayer.legs]["DEFENSE"]
    # No chest
    elif myPlayer.chest == "None":
        return items[myPlayer.head]["DEFENSE"] + items[myPlayer.legs]["DEFENSE"]
    # No legs
    elif myPlayer.legs == "None":
        return items[myPlayer.head]["DEFENSE"] + items[myPlayer.chest]["DEFENSE"]
    # All slots equipped
    else:
        return items[myPlayer.head]["DEFENSE"] + items[myPlayer.chest]["DEFENSE"] + items[myPlayer.legs]["DEFENSE"]

# Magic choice prompt
def magic_prompt(enemy):
    clearConsole()
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
    global used_magic

    while True:
        action = input("> ")
        if action == '1':       # Fireball
            if myPlayer.mp < 20:
                print("Not enough MP to cast Fireball.")
                continue
            else:
                used_magic = True
                fireball(enemy)
                break
        elif action == '2':     # Icebolt
            if myPlayer.mp < 30:
                print("Not enough MP to cast Icebolt.")
                continue
            else:
                used_magic = True
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
                used_magic = True
                heal(enemy)
                break
        elif action == '4':     # Back
            clearConsole()
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
        damage = random.randrange(1, round(myPlayer.magic / 2) + 5)
    else:
        damage = random.randrange(1, round(myPlayer.magic / 2) + round(items[myPlayer.magic_weapon]["DAMAGE"] / 2) + 5)
    enemy.hp -= damage
    clearConsole()
    if damage == 0:
        print("\n##########")
        print("# Combat #")
        print("##########\n")
        print("Your fireball misses the {}!".format(enemy.name))
        enemy.display_stats()
        enemy_attack(enemy)
    elif enemy.is_dead():
        combat_victory(enemy)
    else:
        print("\n##########")
        print("# Combat #")
        print("##########\n")
        print("You hit the {} with a fireball for {} damage!".format(enemy.name, damage))
        enemy.display_stats()
        enemy_attack(enemy)

# Icebolt
def icebolt(enemy):
    myPlayer.mp -= 30
    if miss():
        damage = 0
    elif myPlayer.magic_weapon == "None":
        damage = random.randrange(1, round(myPlayer.magic / 2) + 9)
    else:
        damage = random.randrange(1, round(myPlayer.magic / 2) + round(items[myPlayer.magic_weapon]["DAMAGE"] / 2) + 9)
    enemy.hp -= damage
    clearConsole()
    if damage == 0:
        print("\n##########")
        print("# Combat #")
        print("##########\n")
        print("Your icebolt misses the {}!".format(enemy.name))
        enemy.display_stats()
        enemy_attack(enemy)
    if enemy.is_dead():
        combat_victory(enemy)
    else:
        print("\n##########")
        print("# Combat #")
        print("##########\n")
        print("You hit the {} with an icebolt for {} damage!".format(enemy.name, damage))
        enemy.display_stats()
        enemy_attack(enemy)

# Heal
def heal(enemy):
    myPlayer.mp -= 40
    if myPlayer.hp + 40 > myPlayer.max_hp:      #Prevent overhealing
        healed = myPlayer.max_hp - myPlayer.hp
        myPlayer.hp = myPlayer.max_hp
    else:
        healed = 40
        myPlayer.hp += healed
    clearConsole()
    print("\n##########")
    print("# Combat #")
    print("##########\n")
    print("You heal yourself for {} HP.".format(healed))
    enemy.display_stats()
    enemy_attack(enemy)

# Item prompt
def item_prompt(enemy):
    clearConsole()
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
                clearConsole()
                print("\n##########")
                print("# Combat #")
                print("##########\n")
                print("You drink the potion and heal for {} HP!".format(healed))
                enemy.display_stats()
                enemy_attack(enemy)
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
                clearConsole()
                print("\n##########")
                print("# Combat #")
                print("##########\n")
                print("You drink the potion and gain {} MP!".format(mana))
                enemy.display_stats()
                enemy_attack(enemy)
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
                clearConsole()
                print("\n##########")
                print("# Combat #")
                print("##########\n")
                print("You drink the potion and heal fully!")
                enemy.display_stats()
                enemy_attack(enemy)
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
                clearConsole()
                print("\n##########")
                print("# Combat #")
                print("##########\n")
                print("You drink the potion and gain all your mana!")
                enemy.display_stats()
                enemy_attack(enemy)
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
                clearConsole()
                print("\n##########")
                print("# Combat #")
                print("##########\n")
                print("You drink the potion and gain full health and mana!")
                enemy.display_stats()
                enemy_attack(enemy)
                break
        elif action == '6':     # Back
            clearConsole()
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
        rng = random.randrange(9)   # 10% chance
        if rng == 0:
            return True
        else:
            return False
    elif myPlayer.agility >= 20 and myPlayer.agility < 25:  # Agility level (20-24)
        rng = random.randrange(6)   # 14% chance
        if rng == 0:
            return True
        else:
            return False
    elif myPlayer.agility == 25:                            # Agility max level (25)
        rng = random.randrange(3)   # 25% chance
        if rng == 0:
            return True
        else:
            return False

# Combat Victory Function
def combat_victory(enemy):
    print_location()
    print("You killed the {}!".format(enemy.name))
    enemy.hp = enemy.max_hp     # Reset enemy health
    print("You receive {} gold!".format(enemy.gold))
    myPlayer.gold += enemy.gold
    myPlayer.xp += enemy.xp     # Combat xp
    if myPlayer.lvl < myPlayer.max_level:
        if myPlayer.xp >= myPlayer.lvlUp:
            myPlayer.level_up()
        else:
            print("You gained {} Combat XP! {} XP left to next level.".format(enemy.xp, myPlayer.lvlUp - myPlayer.xp))
    stat_xp(enemy)  # Determine stat xp distribution
    myPlayer.display_stats()
    global used_strength, used_agility, used_magic  # Reset globals
    used_strength = False
    used_agility = False
    used_magic = False

# Determine stat xp distribution based on Player combat choices
def stat_xp(enemy):
    # Player used only strength
    if used_strength and not used_agility and not used_magic:
        myPlayer.str_xp += enemy.xp
        if myPlayer.strength < myPlayer.max_level:
            if myPlayer.str_xp >= myPlayer.str_lvlUp:
                myPlayer.strength_level_up()
            else:
                print("You gained {} Strength XP! {} XP left to next level.\n".format(enemy.xp, myPlayer.str_lvlUp - myPlayer.str_xp))

    # Player used only agility
    elif used_agility and not used_strength and not used_magic:     
        myPlayer.ag_xp += enemy.xp
        if myPlayer.agility < myPlayer.max_level:
            if myPlayer.ag_xp >= myPlayer.ag_lvlUp:
                myPlayer.agility_level_up()
            else:
                print("You gained {} Agility XP! {} XP left to next level.\n".format(enemy.xp, myPlayer.ag_lvlUp - myPlayer.ag_xp))

    # Player used only magic
    elif used_magic and not used_strength and not used_agility:     
        myPlayer.mag_xp += enemy.xp
        if myPlayer.magic < myPlayer.max_level:
            if myPlayer.mag_xp >= myPlayer.mag_lvlUp:
                myPlayer.magic_level_up()
            else:
                print("You gained {} Magic XP! {} XP left to next level.\n".format(enemy.xp, myPlayer.mag_lvlUp - myPlayer.mag_xp))

    # Player used strength and agility
    elif used_strength and used_agility and not used_magic:         
        xp = round(enemy.xp / 2)    # Divide xp in 2
        myPlayer.str_xp += xp       # Strength
        if myPlayer.strength < myPlayer.max_level:
            if myPlayer.str_xp >= myPlayer.str_lvlUp:
                myPlayer.strength_level_up()
            else:
                print("You gained {} Strength XP! {} XP left to next level.".format(xp, myPlayer.str_lvlUp - myPlayer.str_xp))
        myPlayer.ag_xp += xp        # Agility
        if myPlayer.agility < myPlayer.max_level:
            if myPlayer.ag_xp >= myPlayer.ag_lvlUp:
                myPlayer.agility_level_up()
            else:
                print("You gained {} Agility XP! {} XP left to next level.\n".format(xp, myPlayer.ag_lvlUp - myPlayer.ag_xp))

    # Player used strength and magic
    elif used_strength and used_magic and not used_agility:         
        xp = round(enemy.xp / 2)    # Divide xp in 2
        myPlayer.str_xp += xp       # Strength
        if myPlayer.strength < myPlayer.max_level:
            if myPlayer.str_xp >= myPlayer.str_lvlUp:
                myPlayer.strength_level_up()
            else:
                print("You gained {} Strength XP! {} XP left to next level.".format(xp, myPlayer.str_lvlUp - myPlayer.str_xp))
        myPlayer.mag_xp += xp       # Magic
        if myPlayer.magic < myPlayer.max_level:
            if myPlayer.mag_xp >= myPlayer.mag_lvlUp:
                myPlayer.magic_level_up()
            else:
                print("You gained {} Magic XP! {} XP left to next level.\n".format(xp, myPlayer.mag_lvlUp - myPlayer.mag_xp))

    # Player used agility and magic
    elif used_agility and used_magic and not used_strength:   
        xp = round(enemy.xp / 2)    # Divide xp in 2      
        myPlayer.ag_xp += xp        # Agility
        if myPlayer.agility < myPlayer.max_level:
            if myPlayer.ag_xp >= myPlayer.ag_lvlUp:
                myPlayer.agility_level_up()
            else:
                print("You gained {} Agility XP! {} XP left to next level.".format(xp, myPlayer.ag_lvlUp - myPlayer.ag_xp))
        myPlayer.mag_xp += xp       # Magic
        if myPlayer.magic < myPlayer.max_level:
            if myPlayer.mag_xp >= myPlayer.mag_lvlUp:
                myPlayer.magic_level_up()
            else:
                print("You gained {} Magic XP! {} XP left to next level.\n".format(xp, myPlayer.mag_lvlUp - myPlayer.mag_xp))
        
    # Player used strength/agility/magic
    elif used_strength and used_agility and used_magic:            
        xp = round(enemy.xp / 3)    # Divide xp in 3   
        myPlayer.str_xp += xp       # Strength
        if myPlayer.strength < myPlayer.max_level:
            if myPlayer.str_xp >= myPlayer.str_lvlUp:
                myPlayer.strength_level_up()
            else:
                print("You gained {} Strength XP! {} XP left to next level.".format(xp, myPlayer.str_lvlUp - myPlayer.str_xp))   
        myPlayer.ag_xp += xp        # Agility
        if myPlayer.agility < myPlayer.max_level:
            if myPlayer.ag_xp >= myPlayer.ag_lvlUp:
                myPlayer.agility_level_up()
            else:
                print("You gained {} Agility XP! {} XP left to next level.".format(xp, myPlayer.ag_lvlUp - myPlayer.ag_xp))
        myPlayer.mag_xp += xp       # Magic
        if myPlayer.magic < myPlayer.max_level:
            if myPlayer.mag_xp >= myPlayer.mag_lvlUp:
                myPlayer.magic_level_up()
            else:
                print("You gained {} Magic XP! {} XP left to next level.\n".format(xp, myPlayer.mag_lvlUp - myPlayer.mag_xp))

# Combat Defeat function
def combat_defeat(enemy):
    global used_strength, used_agility, used_magic  # Reset globals
    used_strength = False
    used_agility = False
    used_magic = False
    enemy.hp = enemy.max_hp     # Reset enemy health
    clearConsole()
    print("\n##########")
    print("# Combat #")
    print("##########\n")
    defeat1 = ("You were defeated by the {}!\n".format(enemy.name))
    defeat2 = ("You fall unconscious...")
    for character in defeat1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in defeat2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(2)
    
    clearConsole()
    print_location()
    defeat3 = ("Some time later")
    for character in defeat3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    periods = ("...\n")
    for character in periods:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(1)
    time.sleep(0.5)

    # Player has at least 2 items and 2 gold
    if len(inventory) >= 2 and myPlayer.gold >= 2:
        defeat4 = ("You awaken and discover half of your gold and inventory is gone!\n\n")
        myPlayer.gold = round(myPlayer.gold / 2)            # Player gold divided in half
        for i in range(round(len(inventory) / 2)):          # Remove half of inventory randomly
            inventory.pop(random.randrange(len(inventory)))

    # Player has less than 2 items and at least 2 gold
    elif len(inventory) < 2 and myPlayer.gold >= 2:
        defeat4 = ("You awaken and discover half of your gold is gone!\n\n")
        myPlayer.gold = round(myPlayer.gold / 2)            # Player gold divided in half

    # Player has at least 2 items and less than 2 gold
    elif len(inventory) >= 2 and myPlayer.gold < 2:
        defeat4 = ("You awaken and discover half of your inventory is gone!\n\n")
        for i in range(round(len(inventory) / 2)):          # Remove half of inventory randomly
            inventory.pop(random.randrange(len(inventory)))
    
    # Player has less than 2 items and less than 2 gold
    else:
        defeat4 = ("You awaken and feel sore from the battle with the {}.".format(enemy.name))

    for character in defeat4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(2)
    myPlayer.hp = myPlayer.max_hp                   # Player hp back at max
    myPlayer.mp = myPlayer.max_mp                   # Player mp back at max
    myPlayer.display_stats()

    