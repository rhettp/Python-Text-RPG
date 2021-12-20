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
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 't1'
myPlayer = player()