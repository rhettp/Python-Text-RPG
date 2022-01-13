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

##### Main Function #####
def main():
    title_screen()
    prompt_choice()

if __name__=="__main__":
    main()
