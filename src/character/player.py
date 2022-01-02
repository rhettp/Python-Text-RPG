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
        self.xp = 0
        self.lvlUp = 50
        self.lvl = 1
        self.strength = 1
        self.agility = 1
        self.magic = 1
        self.wc_xp = 0
        self.wc_lvlUp = 50
        self.wc_lvl = 1
        
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

    def level_up(self):
        self.lvl += 1
        self.xp -= self.lvlUp
        self.lvlUp = round(self.lvlUp * 1.5)
        print("Congatulations your level increased to {}!".format(self.lvl))
        print("{} XP to next level.\n".format(myPlayer.lvlUp - myPlayer.xp))

myPlayer = player()