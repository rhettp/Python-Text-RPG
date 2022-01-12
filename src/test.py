from prompts.title_screen import *
from gameplay.inventory import *

myPlayer.ft_lvl = 2
for i in items:
    addToInventory(i)
myPlayer.bs_lvl = 9
town_prompt()