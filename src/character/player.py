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

        self.xp = 0         # Combat XP
        self.lvlUp = 50     # Combat XP required for level up
        self.lvl = 1        # Current Combat level 

        self.strength = 1   # Current Strength level
        self.agility = 1    # Current Agility level
        self.magic = 1      # Current Magic level

        self.wc_xp = 0      # Woodcutting XP
        self.wc_lvlUp = 50  # Woodcutting XP required for level up
        self.wc_lvl = 1     # Current Woodcutting level

        self.mn_xp = 0      # Mining XP
        self.mn_lvlUp = 50  # Mining XP required for level up
        self.mn_lvl = 1     # Current Mining level

        self.bs_xp = 0      # Blacksmithing XP
        self.bs_lvlUp = 50  # Blacksmithing XP required for level up
        self.bs_lvl = 1     # Current Blacksmithing level
        
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
        print("Name:            {}".format(self.name))
        print("Combat:          {}".format(self.lvl))
        print("Strength:        {}".format(self.strength))
        print("Agility:         {}".format(self.agility))
        print("Magic:           {}".format(self.magic))
        print("Woodcutting:     {}".format(self.wc_lvl))
        print("Mining:          {}".format(self.mn_lvl))
        print("Blacksmithing:   {}\n".format(self.bs_lvl))

    def rest(self):
        self.hp = self.max_hp
        self.mp = self.max_mp

    # Combat level up
    def level_up(self):
        self.lvl += 1
        self.max_hp += 5
        self.xp -= self.lvlUp
        self.lvlUp = round(self.lvlUp * 1.2)
        print("Congatulations your Combat level increased to {}!".format(self.lvl))
        print("{} XP to next level.\n".format(myPlayer.lvlUp - myPlayer.xp))

    # Woodcutting level up
    def woodcutting_level_up(self):
        self.wc_lvl += 1
        self.wc_xp -= self.wc_lvlUp
        self.wc_lvlUp = round(self.wc_lvlUp * 1.2)
        print("Congatulations your Woodcutting level increased to {}!".format(self.wc_lvl))
        print("{} XP to next level.\n".format(myPlayer.wc_lvlUp - myPlayer.wc_xp))

    # Mining level up
    def mining_level_up(self):
        self.mn_lvl += 1
        self.mn_xp -= self.mn_lvlUp
        self.mn_lvlUp = round(self.mn_lvlUp * 1.2)
        print("Congatulations your Mining level increased to {}!".format(self.mn_lvl))
        print("{} XP to next level.\n".format(myPlayer.mn_lvlUp - myPlayer.mn_xp))

    # Blacksmithing level up
    def blacksmithing_level_up(self):
        self.bs_lvl += 1
        self.bs_xp -= self.bs_lvlUp
        self.bs_lvlUp = round(self.bs_lvlUp * 1.2)
        print("Congatulations your Blacksmithing level increased to {}!".format(self.bs_lvl))
        print("{} XP to next level.\n".format(myPlayer.bs_lvlUp - myPlayer.bs_xp))

myPlayer = player()