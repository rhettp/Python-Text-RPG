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
    addToInventory("Log")
    addToInventory("Iron Ore")
    addToInventory("Log")
    addToInventory("Iron Ore")
    addToInventory("Iron Ore")
    town_prompt()

if __name__=="__main__":
    main()