from character.player import *
from gameplay.inventory import *
import shelve

# Save game function
# All player attributes and stats are saved
def save_game():
    print("Your progess has been saved.")
    shelfFile = shelve.open('saved_game_file')

    shelfFile['Player Name'] = myPlayer.name                    # Player name
    shelfFile['Max HP'] = myPlayer.max_hp                       # Player max HP
    shelfFile['Player HP'] = myPlayer.hp                        # Current HP
    shelfFile['Max MP'] = myPlayer.max_mp                       # Player max MP
    shelfFile['Player MP'] = myPlayer.mp                        # Current MP
    shelfFile['Player Location'] = myPlayer.location            # Player location
    shelfFile['Gold'] = myPlayer.gold                           # Current gold
    current_inventory = []                                      # Current inventory
    for item in inventory:
        current_inventory.append(item)
    shelfFile['Inventory'] = current_inventory                  
    shelfFile['Inventory Size'] = myPlayer.inventory_size       # Inventory size limit

    shelfFile['Combat XP'] = myPlayer.xp                        # Combat XP
    shelfFile['Combat Required XP'] = myPlayer.lvlUp            # Combat XP required for level up
    shelfFile['Combat Level'] = myPlayer.lvl                    # Current Combat Level
    shelfFile['Max Level'] = myPlayer.max_level                 # Max level for skills

    shelfFile['Strength XP'] = myPlayer.str_xp                  # Strength XP
    shelfFile['Strength Required XP'] = myPlayer.str_lvlUp      # Strength XP required for level up
    shelfFile['Strength Level'] = myPlayer.strength             # Current Strength Level

    shelfFile['Agility XP'] = myPlayer.ag_xp                    # Agility XP
    shelfFile['Agility Required XP'] = myPlayer.ag_lvlUp        # Agility XP required for level up
    shelfFile['Agility Level'] = myPlayer.agility               # Current Agility Level

    shelfFile['Magic XP'] = myPlayer.mag_xp                     # Magic XP
    shelfFile['Magic Required XP'] = myPlayer.mag_lvlUp         # Magic XP required for level
    shelfFile['Magic Level'] = myPlayer.magic                   # Current Magic Level

    shelfFile['Woodcutting XP'] = myPlayer.wc_xp                # Woodcutting XP
    shelfFile['Woodcutting Required XP'] = myPlayer.wc_lvlUp    # Woodcutting XP required for level
    shelfFile['Woodcutting Level'] = myPlayer.wc_lvl            # Current Woodcutting Level

    shelfFile['Fletching XP'] = myPlayer.ft_xp                  # Fletching XP
    shelfFile['Fletching Required XP'] = myPlayer.ft_lvlUp      # Fletching XP required for level
    shelfFile['Fletching Level'] = myPlayer.ft_lvl              # Current Fletching Level

    shelfFile['Mining XP'] = myPlayer.mn_xp                     # Mining XP
    shelfFile['Mining Required XP'] = myPlayer.mn_lvlUp         # Mining XP required for level
    shelfFile['Mining Level'] = myPlayer.mn_lvl                 # Current Mining Level

    shelfFile['Blacksmithing XP'] = myPlayer.bs_xp              # Blacksmithing XP
    shelfFile['Blacksmithing Required XP'] = myPlayer.bs_lvlUp  # Blacksmithing XP required for level
    shelfFile['Blacksmithing Level'] = myPlayer.bs_lvl          # Current Blacksmithing Level

    shelfFile['Head Slot'] = myPlayer.head                      # Head Slot
    shelfFile['Chest Slot'] = myPlayer.chest                    # Chest Slot 
    shelfFile['Leg Slot'] = myPlayer.legs                       # Leg Slot
    shelfFile['Melee Slot'] = myPlayer.melee_weapon             # Melee Slot
    shelfFile['Range Slot'] = myPlayer.range_weapon             # Range Slot  
    shelfFile['Magic Slot'] = myPlayer.magic_weapon             # Magic Slot

    shelfFile.close()

# Load game function
# Load all player stats and attributes
def load_game():
    shelfFile = shelve.open('saved_game_file')

    myPlayer.name = shelfFile['Player Name']                    # Player name
    myPlayer.max_hp = shelfFile['Max HP']                       # Player max HP
    myPlayer.hp = shelfFile['Player HP']                        # Current HP
    myPlayer.max_mp = shelfFile['Max MP']                       # Player max MP
    myPlayer.mp = shelfFile['Player MP']                        # Current MP
    myPlayer.location = shelfFile['Player Location']            # Player location
    myPlayer.gold = shelfFile['Gold']                           # Current gold
    for item in shelfFile['Inventory']:                         # Current inventory
        inventory.append(item)                                 
    myPlayer.inventory_size = shelfFile['Inventory Size']       # Inventory size limit

    myPlayer.xp = shelfFile['Combat XP']                        # Combat xp
    myPlayer.lvlUp = shelfFile['Combat Required XP']            # Combat xp required for level up
    myPlayer.lvl = shelfFile['Combat Level']                    # Current Combat level
    myPlayer.max_level = shelfFile['Max Level']                 # Max level for skills

    myPlayer.str_xp = shelfFile['Strength XP']                  # Strength XP
    myPlayer.str_lvlUp = shelfFile['Strength Required XP']      # Strength XP required for level up
    myPlayer.strength = shelfFile['Strength Level']             # Current Strength level

    myPlayer.ag_xp = shelfFile['Agility XP']                    # Agility XP
    myPlayer.ag_lvlUp = shelfFile['Agility Required XP']        # Agility XP required for level
    myPlayer.agility = shelfFile['Agility Level']               # Current Agility level

    myPlayer.mag_xp = shelfFile['Magic XP']                     # Magic XP 
    myPlayer.mag_lvlUp = shelfFile['Magic Required XP']         # Magic XP required for level
    myPlayer.magic = shelfFile['Magic Level']                   # Current Magic level

    myPlayer.wc_xp = shelfFile['Woodcutting XP']                # Woodcutting XP
    myPlayer.wc_lvlUp = shelfFile['Woodcutting Required XP']    # Woodcutting XP required for level
    myPlayer.wc_lvl = shelfFile['Woodcutting Level']            # Current Woodcutting level

    myPlayer.ft_xp = shelfFile['Fletching XP']                  # Fletching XP
    myPlayer.ft_lvlUp = shelfFile['Fletching Required XP']      # Fletching XP required for level
    myPlayer.ft_lvl = shelfFile['Fletching Level']              # Current Fletching level

    myPlayer.mn_xp = shelfFile['Mining XP']                     # Mining XP
    myPlayer.mn_lvlUp = shelfFile['Mining Required XP']         # Mining XP required for level
    myPlayer.mn_lvl = shelfFile['Mining Level']                 # Current Mining level

    myPlayer.bs_xp = shelfFile['Blacksmithing XP']              # Blacksmithing XP
    myPlayer.bs_lvlUp = shelfFile['Blacksmithing Required XP']  # Blacksmithing XP required for level
    myPlayer.bs_lvl = shelfFile['Blacksmithing Level']          # Current Blacksmithing level

    myPlayer.head = shelfFile['Head Slot']                      # Head Slot 
    myPlayer.chest = shelfFile['Chest Slot']                    # Chest Slot
    myPlayer.legs = shelfFile['Leg Slot']                       # Leg Slot
    myPlayer.melee_weapon = shelfFile['Melee Slot']             # Melee Slot
    myPlayer.range_weapon = shelfFile['Range Slot']             # Range Slot 
    myPlayer.magic_weapon = shelfFile['Magic Slot']             # Magic Slot

    shelfFile.close()

