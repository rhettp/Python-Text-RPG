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
        self.hp = 100
        self.mp = 100
        self.status_effects = []
        self.location = 'Town'
myPlayer = player()