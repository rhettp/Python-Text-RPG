import cmd
import textwrap
import sys
import os
import time
import random

##### Player setup #####
class player:
    def __init__(self):
        self.name = ''
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
        
    # Check if player is dead
    def is_dead(self):
        return self.hp <= 0

    # Display current player stats
    def display_stats(self):
        print('======================================')
        print('HP: {}/{}   MP: ({}/{})  Gold: {}'.format(self.hp,self.max_hp, self.mp, self.max_mp, self.gold))
        print('======================================')

    def rest(self):
        self.hp = self.max_hp
        self.mp = self.max_mp

    # Combat level up
    def level_up(self):
        self.lvl += 1
        self.xp -= self.lvlUp
        self.lvlUp = round(self.lvlUp * 1.2)
        print("Congatulations your level increased to {}!".format(self.lvl))
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

myPlayer = player()