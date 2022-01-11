from prompts.title_screen import *
from gameplay.inventory import *

myPlayer.ft_lvl = 2
for i in range (100):
    addToInventory("Copper Ore")
    addToInventory("Iron Ore")
    addToInventory("Copper Bar")
    addToInventory("Iron Bar")
myPlayer.bs_lvl = 9
mine_prompt()