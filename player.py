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
myPlayer = player()