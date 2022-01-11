from prompts.title_screen import *
from gameplay.inventory import *

myPlayer.ft_lvl = 2
for i in range (100):
    addToInventory("Oak Log")
    addToInventory("Bow String")
forest_prompt()