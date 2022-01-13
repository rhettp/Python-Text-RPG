from prompts.title_screen import *
from gameplay.inventory import *

for i in items:
    addToInventory(i)
myPlayer.wc_lvl = 24
myPlayer.ft_lvl = 24
myPlayer.mn_lvl = 24
myPlayer.bs_lvl = 24
forest_prompt()