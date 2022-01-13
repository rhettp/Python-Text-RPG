import cmd
import textwrap
import sys
import os
import time
import random

##### Player setup #####
class player:
    def __init__(self):
        self.name = 'Player'
        self.max_hp = 100
        self.hp = self.max_hp
        self.max_mp = 100
        self.mp = self.max_mp
        self.location = 'Town'
        self.gold = 100
        self.inventory_size = 25

        self.xp = 0                 # Combat XP
        self.lvlUp = 50             # Combat XP required for level up
        self.lvl = 1                # Current Combat level
        self.max_level = 25         # Max level for skills 

        self.str_xp = 0             # Strength XP
        self.str_lvlUp = 50         # Strength XP required for level up
        self.strength = 1           # Current Strength level

        self.ag_xp = 0              # Agility XP
        self.ag_lvlUp = 50          # Agility XP required for level up
        self.agility = 1            # Current Agility level

        self.mag_xp = 0             # Magic XP
        self.mag_lvlUp = 50         # Magic XP required for level up
        self.magic = 1              # Current Magic level

        self.wc_xp = 0              # Woodcutting XP
        self.wc_lvlUp = 50          # Woodcutting XP required for level up
        self.wc_lvl = 1             # Current Woodcutting level

        self.ft_xp = 0              # Fletching XP
        self.ft_lvlUp = 50          # Fletching XP required for level up
        self.ft_lvl = 1             # Current Fletching level

        self.mn_xp = 0              # Mining XP
        self.mn_lvlUp = 50          # Mining XP required for level up
        self.mn_lvl = 1             # Current Mining level

        self.bs_xp = 0              # Blacksmithing XP
        self.bs_lvlUp = 50          # Blacksmithing XP required for level up
        self.bs_lvl = 1             # Current Blacksmithing level

        self.head = "None"          # Head Slot
        self.chest = "None"         # Chest Slot
        self.legs = "None"          # Leg Slot
        self.melee_weapon = "None"  # Melee Slot
        self.range_weapon = "None"  # Range Slot
        self.magic_weapon = "None"  # Magic Slot
        
    # Check if player is dead
    def is_dead(self):
        return self.hp <= 0

    # Display current player stats
    def display_stats(self):
        print('======================================')
        print('HP: {}/{}   MP: ({}/{})  Gold: {}'.format(self.hp,self.max_hp, self.mp, self.max_mp, self.gold))
        print('======================================')

    # Display character info
    def character_info(self):
        text = "Gear"
        options = [self.head, self.chest, self.legs, self.melee_weapon, self.range_weapon, self.magic_weapon]
        longest = max(options, key=len) # Find longest string length b/w gear options
        space = 17 + len(longest)       # Space based on longest string
        gear = text.center(space," ")   # Center "Gear" using longest string
        print("---------------------            " + '-' * space)
        print("        Stats                    " + gear)
        print("---------------------            " + '-' * space)
        print("Combat:            {}\t\t Head:            {}".format(self.lvl, self.head))
        print("Strength:          {}\t\t Chest:           {}".format(self.strength, self.chest))
        print("Agility:           {}\t\t Legs:            {}".format(self.agility, self.legs))
        print("Magic:             {}\t\t".format(self.magic))
        print("Woodcutting:       {}\t\t Melee Weapon:    {}".format(self.wc_lvl, self.melee_weapon))
        print("Fletching:         {}\t\t Range Weapon:    {}".format(self.ft_lvl, self.range_weapon))
        print("Mining:            {}\t\t Magic Weapon:    {}".format(self.mn_lvl, self.magic_weapon))
        print("Blacksmithing:     {}\t\t\n".format(self.bs_lvl))

    def rest(self):
        rest1 = ("You find a room at one of the local inns and rest for the night")
        periods = (".....\n")
        for character in rest1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        for character in periods:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.6)
        print("You feel energized! Your HP and MP have been restored.\n")
        self.hp = self.max_hp
        self.mp = self.max_mp

    # Combat level up
    def level_up(self):
        self.lvl += 1
        self.max_hp += 5
        self.xp -= self.lvlUp
        if self.lvl == self.max_level:
            print("Congatulations you increased Combat to the max level!\n")
        else:
            self.lvlUp = round(self.lvlUp * 1.2)
            print("Congatulations your Combat level increased to {}!".format(self.lvl))
            print("{} XP to next level.\n".format(myPlayer.lvlUp - myPlayer.xp))

    # Strength level up
    def strength_level_up(self):
        self.strength += 1
        self.str_xp -= self.str_lvlUp
        if self.strength == self.max_level:
            print("Congatulations you increased Strength to the max level!\n")
        else:
            self.str_lvlUp = round(self.str_lvlUp * 1.2)
            print("Congatulations your Strength level increased to {}!".format(self.strength))
            print("{} XP to next level.\n".format(myPlayer.str_lvlUp - myPlayer.str_xp))

    # Agility level up
    def agility_level_up(self):
        self.agility += 1
        self.ag_xp -= self.ag_lvlUp
        if self.agility == self.max_level:
            print("Congatulations you increased Agility to the max level!\n")
        else:
            self.ag_lvlUp = round(self.ag_lvlUp * 1.2)
            print("Congatulations your Agility level increased to {}!".format(self.agility))
            print("{} XP to next level.\n".format(myPlayer.ag_lvlUp - myPlayer.ag_xp))

    # Magic level up
    def magic_level_up(self):
        self.magic += 1
        self.max_mp += 5
        self.mag_xp -= self.mag_lvlUp
        if self.magic == self.max_level:
            print("Congatulations you increased Magic to the max level!\n")
        else:
            self.mag_lvlUp = round(self.mag_lvlUp * 1.2)
            print("Congatulations your Magic level increased to {}!".format(self.magic))
            print("{} XP to next level.\n".format(myPlayer.mag_lvlUp - myPlayer.mag_xp))

    # Woodcutting level up
    def woodcutting_level_up(self):
        self.wc_lvl += 1
        self.wc_xp -= self.wc_lvlUp
        if self.wc_lvl == self.max_level:
            print("Congatulations you increased Woodcutting to the max level!\n")
        else:
            self.wc_lvlUp = round(self.wc_lvlUp * 1.2)
            print("Congatulations your Woodcutting level increased to {}!".format(self.wc_lvl))
            print("{} XP to next level.\n".format(myPlayer.wc_lvlUp - myPlayer.wc_xp))

    # Fletching level up
    def fletching_level_up(self):
        self.ft_lvl += 1
        self.ft_xp -= self.ft_lvlUp
        if self.ft_lvl == self.max_level:
            print("Congatulations you increased Fletching to the max level!\n")
        else:
            self.ft_lvlUp = round(self.ft_lvlUp * 1.2)
            print("Congatulations your Fletching level increased to {}!".format(self.ft_lvl))
            print("{} XP to next level.\n".format(myPlayer.ft_lvlUp - myPlayer.ft_xp))

    # Mining level up
    def mining_level_up(self):
        self.mn_lvl += 1
        self.mn_xp -= self.mn_lvlUp
        if self.mn_lvl == self.max_level:
            print("Congatulations you increased Mining to the max level!\n")
        else:
            self.mn_lvlUp = round(self.mn_lvlUp * 1.2)
            print("Congatulations your Mining level increased to {}!".format(self.mn_lvl))
            print("{} XP to next level.\n".format(myPlayer.mn_lvlUp - myPlayer.mn_xp))

    # Blacksmithing level up
    def blacksmithing_level_up(self):
        self.bs_lvl += 1
        self.bs_xp -= self.bs_lvlUp
        if self.bs_lvl == self.max_level:
            print("Congatulations you increased Blacksmithing to the max level!\n")
        else:
            self.bs_lvlUp = round(self.bs_lvlUp * 1.2)
            print("Congatulations your Blacksmithing level increased to {}!".format(self.bs_lvl))
            print("{} XP to next level.\n".format(myPlayer.bs_lvlUp - myPlayer.bs_xp))

myPlayer = player()

