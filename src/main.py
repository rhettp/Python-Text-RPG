"""
Rhett Proctor
Python Text RPG
"""

import cmd
import textwrap
import sys
import os
import time
import random
from prompts.title_screen import *
from gameplay.inventory import *

##### Main Function #####
def main():
    #title_screen()
    addToInventory("Health Potion")
    addToInventory("Mana Potion")
    addToInventory("Super Health Potion")
    addToInventory("Super Mana Potion")
    addToInventory("Restore Potion")
    prompt_choice()

if __name__=="__main__":
    main()