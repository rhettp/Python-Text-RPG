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
        self.strength = 1
        self.agility = 1
        self.magic = 1
        
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

myPlayer = player()