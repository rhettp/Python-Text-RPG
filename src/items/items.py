from character.player import *

##### Items #####

# General Store buy set
general_store_buy_set = ["Oak Log", "Willow Log", "Maple Log", "Oak Bow (u)", "Willow Bow (u)", "Maple Bow (u)", "Bow String", "Oak Bow", "Willow Bow", "Maple Bow"]

# General Store sell set 
general_sell_set = ["Oak Log", "Willow Log", "Maple Log", "Yew Log", "Oak Bow (u)", "Willow Bow (u)", "Maple Bow (u)",\
     "Yew Bow (u)", "Bow String", "Oak Bow", "Willow Bow", "Maple Bow", "Yew Bow"]

# Blacksmith buy set
blacksmith_buy_set = ["Copper Ore", "Iron Ore", "Silver Ore", "Copper Bar", "Iron Bar", "Silver Bar", "Copper Sword",\
    "Copper Helmet","Copper Platelegs", "Copper Platebody", "Iron Sword", "Iron Helmet", "Iron Platelegs", "Iron Platebody",\
         "Silver Sword", "Silver Helmet","Silver Platelegs", "Silver Platebody"]

# Blacksmith sell set
blacksmith_sell_set = ["Copper Ore", "Iron Ore", "Silver Ore", "Gold Ore", "Diamond Ore", "Copper Bar", "Iron Bar",\
     "Silver Bar", "Gold Bar", "Diamond Bar", "Copper Sword", "Copper Helmet","Copper Platelegs", "Copper Platebody",\
          "Iron Sword", "Iron Helmet", "Iron Platelegs", "Iron Platebody", "Silver Sword", "Silver Helmet", "Silver Platelegs",\
               "Silver Platebody", "Gold Sword", "Gold Helmet", "Gold Platelegs", "Gold Platebody", "Diamond Sword",\
                   "Diamond Helmet", "Diamond Platelegs", "Diamond Platebody"]

# Magic Shop items
magic_shop_buy_set = ["Health Potion","Super Health Potion", "Mana Potion", "Super Mana Potion", "Restore Potion",\
    "Staff", "Magic Staff", "Greater Staff"]

# Magic Shop sell set
magic_shop_sell_set = ["Health Potion","Super Health Potion", "Mana Potion", "Super Mana Potion", "Restore Potion",\
     "Magic Log", "Magic Bow (u)", "Magic Bow", "Staff", "Magic Staff", "Greater Staff"]

# Helmet set
helmet_set = ["Copper Helmet", "Iron Helmet", "Silver Helmet", "Gold Helmet", "Diamond Helmet"]

# Platebody set
platebody_set = ["Copper Platebody", "Iron Platebody", "Silver Platebody", "Gold Platebody", "Diamond Platebody"]

# Platelegs set
platelegs_set = ["Copper Platelegs", "Iron Platelegs", "Silver Platelegs", "Gold Platelegs", "Diamond Platelegs"]

# Melee Weapon set
melee_set = ["Copper Sword", "Iron Sword", "Silver Sword", "Gold Sword", "Diamond Sword"]

# Range Weapon set
range_set = ["Oak Bow", "Willow Bow", "Maple Bow", "Yew Bow", "Magic Bow"]

# Magic Weapon set
staff_set = ["Staff", "Magic Staff", "Greater Staff"]

# All items
items = {
    # Logs
    'Oak Log': {
        "DESCRIPTION": 'An oak log.',
        "VALUE": 5,
        "EXPERIENCE": 5
    },
    'Willow Log': {
        "DESCRIPTION": 'A willow log.',
        "VALUE": 10,
        "EXPERIENCE": 10
    },
    'Maple Log': {
        "DESCRIPTION": 'A maple log.',
        "VALUE": 15,
        "EXPERIENCE": 20
    },
    'Yew Log': {
        "DESCRIPTION": 'A yew log.',
        "VALUE": 20,
        "EXPERIENCE": 40
    },
    'Magic Log': {
        "DESCRIPTION": 'A magic log.',
        "VALUE": 25,
        "EXPERIENCE": 80
    },
    
    # Bow String
     'Bow String': {
        "DESCRIPTION": 'A Bow string',
        "VALUE": 5
    },

    # Unstrung Bows
     'Oak Bow (u)': {
        "DESCRIPTION": 'An unstrung Oak bow',
        "VALUE": 10,
        "EXPERIENCE": 10
    },
     'Willow Bow (u)': {
        "DESCRIPTION": 'An unstrung Willow bow',
        "VALUE": 25,
        "EXPERIENCE": 20
    },
     'Maple Bow (u)': {
        "DESCRIPTION": 'An unstrung Maple bow',
        "VALUE": 40,
        "EXPERIENCE": 45
    },
     'Yew Bow (u)': {
        "DESCRIPTION": 'An unstrung Yew bow',
        "VALUE": 55,
        "EXPERIENCE": 90
    },
     'Magic Bow (u)': {
        "DESCRIPTION": 'An unstrung Magic bow',
        "VALUE": 70,
        "EXPERIENCE": 170
    },

    # Bows
     'Oak Bow': {
        "DESCRIPTION": 'An Oak bow',
        "VALUE": 20,
        "DAMAGE": 5,
        "EXPERIENCE": 15
    },
     'Willow Bow': {
        "DESCRIPTION": 'A Willow bow',
        "VALUE": 35,
        "DAMAGE": 10,
        "EXPERIENCE": 30
    },
     'Maple Bow': {
        "DESCRIPTION": 'A Maple bow',
        "VALUE": 50,
        "DAMAGE": 15,
        "EXPERIENCE": 60
    },
     'Yew Bow': {
        "DESCRIPTION": 'A Yew bow',
        "VALUE": 70,
        "DAMAGE": 20,
        "EXPERIENCE": 120
    },
     'Magic Bow': {
        "DESCRIPTION": 'A Magic bow',
        "VALUE": 100,
        "DAMAGE": 30,
        "EXPERIENCE": 240
    },

    # Ore
    'Copper Ore': {
        "DESCRIPTION": 'A single Copper ore.',
        "VALUE": 5,
        "EXPERIENCE": 5
    },
    'Iron Ore': {
        "DESCRIPTION": 'A single Iron ore.',
        "VALUE": 10,
        "EXPERIENCE": 10
    },
    'Silver Ore': {
        "DESCRIPTION": 'A single Silver ore.',
        "VALUE": 15,
        "EXPERIENCE": 20
    },
    'Gold Ore': {
        "DESCRIPTION": 'A single Gold ore.',
        "VALUE": 20,
        "EXPERIENCE": 40
    },
    'Diamond Ore': {
        "DESCRIPTION": 'A single Diamond ore.',
        "VALUE": 25,
        "EXPERIENCE": 80
    },

    # Bars
    'Copper Bar': {
        "DESCRIPTION": 'A single Copper ore.',
        "VALUE": 5,
        "EXPERIENCE": 5
    },
    'Iron Bar': {
        "DESCRIPTION": 'A single Iron bar.',
        "VALUE": 10,
        "EXPERIENCE": 20
    },
    'Silver Bar': {
        "DESCRIPTION": 'A single Silver bar.',
        "VALUE": 15,
        "EXPERIENCE": 60
    },
    'Gold Bar': {
        "DESCRIPTION": 'A single Gold bar.',
        "VALUE": 20,
        "EXPERIENCE": 160
    },
    'Diamond Bar': {
        "DESCRIPTION": 'A single Diamond bar.',
        "VALUE": 25,
        "EXPERIENCE": 450
    },

    # Copper Items
    'Copper Helmet': {
        "DESCRIPTION": 'A Copper helmet.',
        "VALUE": 15,
        "DEFENSE": 3,
        "EXPERIENCE": 15
    },
    'Copper Sword': {
        "DESCRIPTION": 'A Copper sword.',
        "VALUE": 20,
        "DAMAGE": 5,
        "EXPERIENCE": 20
    },
    'Copper Platelegs': {
        "DESCRIPTION": 'Copper platelegs.',
        "VALUE": 25,
        "DEFENSE": 5,
        "EXPERIENCE": 25
    },
    'Copper Platebody': {
        "DESCRIPTION": 'Copper platebody',
        "VALUE": 30,
        "DEFENSE": 7,
        "EXPERIENCE": 35
    },

    # Iron items
    'Iron Helmet': {
        "DESCRIPTION": 'An Iron helmet.',
        "VALUE": 15,
        "DEFENSE": 3,
        "EXPERIENCE": 40
    },
    'Iron Sword': {
        "DESCRIPTION": 'An Iron sword.',
        "VALUE": 35,
        "DAMAGE": 10,
        "EXPERIENCE": 50
    },
    'Iron Platelegs': {
        "DESCRIPTION": 'Iron platelegs.',
        "VALUE": 25,
        "DEFENSE": 5,
        "EXPERIENCE": 60
    },
    'Iron Platebody': {
        "DESCRIPTION": 'Iron platebody',
        "VALUE": 30,
        "DEFENSE": 7,
        "EXPERIENCE": 70
    },

    # Silver Items
    'Silver Helmet': {
        "DESCRIPTION": 'A Silver helmet.',
        "VALUE": 15,
        "DEFENSE": 3,
        "EXPERIENCE": 80
    },
    'Silver Sword': {
        "DESCRIPTION": 'A Silver sword.',
        "VALUE": 50,
        "DAMAGE": 15,
        "EXPERIENCE": 100
    },
    'Silver Platelegs': {
        "DESCRIPTION": 'Silver platelegs.',
        "VALUE": 25,
        "DEFENSE": 5,
        "EXPERIENCE": 120
    },
    'Silver Platebody': {
        "DESCRIPTION": 'Silver platebody',
        "VALUE": 30,
        "DEFENSE": 7,
        "EXPERIENCE": 140
    },

    # Gold Items
    'Gold Helmet': {
        "DESCRIPTION": 'A Gold helmet.',
        "VALUE": 15,
        "DEFENSE": 3,
        "EXPERIENCE": 160
    },
    'Gold Sword': {
        "DESCRIPTION": 'A Gold sword.',
        "VALUE": 70,
        "DAMAGE": 20,
        "EXPERIENCE": 190
    },
    'Gold Platelegs': {
        "DESCRIPTION": 'Gold platelegs.',
        "VALUE": 25,
        "DEFENSE": 5,
        "EXPERIENCE": 220
    },
    'Gold Platebody': {
        "DESCRIPTION": 'Gold platebody',
        "VALUE": 30,
        "DEFENSE": 7,
        "EXPERIENCE": 250
    },

    # Diamond Items
    'Diamond Helmet': {
        "DESCRIPTION": 'A Diamond helmet.',
        "VALUE": 15,
        "DEFENSE": 3,
        "EXPERIENCE": 350
    },
    'Diamond Sword': {
        "DESCRIPTION": 'A Diamond sword.',
        "VALUE": 100,
        "DAMAGE": 30,
        "EXPERIENCE": 400
    },
    'Diamond Platelegs': {
        "DESCRIPTION": 'Diamond platelegs.',
        "VALUE": 25,
        "DEFENSE": 5,
        "EXPERIENCE": 450
    },
    'Diamond Platebody': {
        "DESCRIPTION": 'Diamond platebody',
        "VALUE": 30,
        "DEFENSE": 7,
        "EXPERIENCE": 500
    },

    # Potions
     'Health Potion': {
        "DESCRIPTION": 'A Health potion',
        "VALUE": 50,
        "EFFECT": 50
    },
     'Mana Potion': {
        "DESCRIPTION": 'A Mana potion',
        "VALUE": 50,
        "EFFECT": 50
    },
     'Super Health Potion': {
        "DESCRIPTION": 'A Super Health potion',
        "VALUE": 100,
        "EFFECT": myPlayer.max_hp
    },
     'Super Mana Potion': {
        "DESCRIPTION": 'A Super mana potion',
        "VALUE": 100,
        "EFFECT": myPlayer.max_mp
    },
     'Restore Potion': {
        "DESCRIPTION": 'A Restore potion',
        "VALUE": 200,
        "EFFECT": myPlayer.max_hp,
        "EFFECT_2": myPlayer.max_mp
    },

    # Staffs
     'Staff': {
        "DESCRIPTION": 'A basic staff',
        "VALUE": 100,
        "DAMAGE": 5
    },
     'Magic Staff': {
        "DESCRIPTION": 'A magic staff',
        "VALUE": 100,
        "DAMAGE": 15
    },
     'Greater Staff': {
        "DESCRIPTION": 'A greater magic staff',
        "VALUE": 100,
        "DAMAGE": 30
    },
}
