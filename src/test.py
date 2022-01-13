from prompts.title_screen import *
from gameplay.inventory import *

for i in items:
    addToInventory(i)
myPlayer.wc_lvl = 24
myPlayer.ft_lvl = 24
myPlayer.mn_lvl = 24
myPlayer.bs_lvl = 24
myPlayer.gold = 10000
myPlayer.lvl = 10
myPlayer.strength = 25
myPlayer.agility = 18
myPlayer.magic = 18
myPlayer.melee_weapon = "Diamond Sword"
town_prompt()