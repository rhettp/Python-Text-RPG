from prompts.title_screen import *
from gameplay.inventory import *

for i in range(24):
    addToInventory("Copper Ore")
myPlayer.wc_lvl = 24
myPlayer.ft_lvl = 24
myPlayer.mn_lvl = 24
myPlayer.bs_lvl = 24
myPlayer.gold = 0
town_prompt()