from prompts.title_screen import *
from gameplay.inventory import *

for i in items:
    addToInventory(i)
myPlayer.wc_lvl = 24
myPlayer.ft_lvl = 24
myPlayer.mn_lvl = 24
myPlayer.bs_lvl = 24
myPlayer.gold = 10000
myPlayer.lvl = 18
myPlayer.strength = 18
myPlayer.agility = 18
myPlayer.magic = 18
town_prompt()