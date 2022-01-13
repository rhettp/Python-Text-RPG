from character.player import *

##### Items #####

# General Store buy set
general_store_buy_set = ["Oak Log", "Willow Log", "Maple Log", "Oak Bow (u)", "Willow Bow (u)", "Maple Bow (u)", "Bow String", "Oak Bow", "Willow Bow", "Maple Bow"]

# General Store sell set 
general_sell_set = ["Oak Log", "Willow Log", "Maple Log", "Yew Log", "Oak Bow (u)", "Willow Bow (u)", "Maple Bow (u)",\
     "Yew Bow (u)", "Bow String", "Oak Bow", "Willow Bow", "Maple Bow", "Yew Bow"]

# Bag set  
bag_set = ["Big Bag", "Bigger Bag", "Biggest Bag"]

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
        "DESCRIPTION": 'A log cut from an Oak Tree.',
        "VALUE": 5,
        "EXPERIENCE": 10
    },
    'Willow Log': {
        "DESCRIPTION": 'A log cut from a Willow Tree.',
        "VALUE": 10,
        "EXPERIENCE": 20
    },
    'Maple Log': {
        "DESCRIPTION": 'A log cut from a Maple Tree.',
        "VALUE": 15,
        "EXPERIENCE": 45
    },
    'Yew Log': {
        "DESCRIPTION": 'A log cut from a Yew Tree.',
        "VALUE": 20,
        "EXPERIENCE": 90
    },
    'Magic Log': {
        "DESCRIPTION": 'A log cut from a Magic Tree.',
        "VALUE": 25,
        "EXPERIENCE": 170
    },
    
    # Bow String
     'Bow String': {
        "DESCRIPTION": 'A string used for bows.',
        "VALUE": 5
    },

    # Unstrung Bows
     'Oak Bow (u)': {
        "DESCRIPTION": 'An unstrung Oak bow.',
        "VALUE": 10,
        "EXPERIENCE": 10
    },
     'Willow Bow (u)': {
        "DESCRIPTION": 'An unstrung Willow bow.',
        "VALUE": 25,
        "EXPERIENCE": 20
    },
     'Maple Bow (u)': {
        "DESCRIPTION": 'An unstrung Maple bow.',
        "VALUE": 40,
        "EXPERIENCE": 45
    },
     'Yew Bow (u)': {
        "DESCRIPTION": 'An unstrung Yew bow.',
        "VALUE": 55,
        "EXPERIENCE": 90
    },
     'Magic Bow (u)': {
        "DESCRIPTION": 'An unstrung Magic bow.',
        "VALUE": 70,
        "EXPERIENCE": 170
    },

    # Bows
     'Oak Bow': {
        "DESCRIPTION": 'A bow made out of Oak with +5 range attack.',
        "VALUE": 20,
        "DAMAGE": 5,
        "EXPERIENCE": 15
    },
     'Willow Bow': {
        "DESCRIPTION": 'A bow made out of Willow with +10 range attack.',
        "VALUE": 35,
        "DAMAGE": 10,
        "EXPERIENCE": 30
    },
     'Maple Bow': {
        "DESCRIPTION": 'A bow made out of Maple with +15 range attack.',
        "VALUE": 50,
        "DAMAGE": 15,
        "EXPERIENCE": 60
    },
     'Yew Bow': {
        "DESCRIPTION": 'A bow made out of Yew with +20 range attack.',
        "VALUE": 70,
        "DAMAGE": 20,
        "EXPERIENCE": 120
    },
     'Magic Bow': {
        "DESCRIPTION": 'A bow made out of Magic logs with +30 range attack.',
        "VALUE": 100,
        "DAMAGE": 30,
        "EXPERIENCE": 240
    },

    # Ore
    'Copper Ore': {
        "DESCRIPTION": 'Ore that can be smelted into Copper Bars.',
        "VALUE": 5,
        "EXPERIENCE": 10
    },
    'Iron Ore': {
        "DESCRIPTION": 'Ore that can be smelted into Iron Bars.',
        "VALUE": 10,
        "EXPERIENCE": 20
    },
    'Silver Ore': {
        "DESCRIPTION": 'Ore that can be smelted into Silver Bars.',
        "VALUE": 15,
        "EXPERIENCE": 45
    },
    'Gold Ore': {
        "DESCRIPTION": 'Ore that can be smelted into Gold Bars.',
        "VALUE": 20,
        "EXPERIENCE": 90
    },
    'Diamond Ore': {
        "DESCRIPTION": 'Ore that can be smelted into Diamond Bars.',
        "VALUE": 25,
        "EXPERIENCE": 170
    },

    # Bars
    'Copper Bar': {
        "DESCRIPTION": 'A bar of Copper used for Blacksmithing.',
        "VALUE": 5,
        "EXPERIENCE": 10
    },
    'Iron Bar': {
        "DESCRIPTION": 'A bar of Iron used for Blacksmithing.',
        "VALUE": 10,
        "EXPERIENCE": 45
    },
    'Silver Bar': {
        "DESCRIPTION": 'A bar of Silver used for Blacksmithing.',
        "VALUE": 15,
        "EXPERIENCE": 60
    },
    'Gold Bar': {
        "DESCRIPTION": 'A bar of Gold used for Blacksmithing.',
        "VALUE": 20,
        "EXPERIENCE": 160
    },
    'Diamond Bar': {
        "DESCRIPTION": 'A bar of Diamond used for Blacksmithing.',
        "VALUE": 25,
        "EXPERIENCE": 450
    },

    # Copper Items
    'Copper Helmet': {
        "DESCRIPTION": 'A Copper helmet with +3 defense.',
        "VALUE": 15,
        "DEFENSE": 3,
        "EXPERIENCE": 15
    },
    'Copper Sword': {
        "DESCRIPTION": 'A Copper sword with +5 attack damage.',
        "VALUE": 20,
        "DAMAGE": 5,
        "EXPERIENCE": 20
    },
    'Copper Platelegs': {
        "DESCRIPTION": 'A set of Copper platelegs with +5 defense.',
        "VALUE": 25,
        "DEFENSE": 5,
        "EXPERIENCE": 25
    },
    'Copper Platebody': {
        "DESCRIPTION": 'A Copper platebody with +7 defense',
        "VALUE": 30,
        "DEFENSE": 7,
        "EXPERIENCE": 35
    },

    # Iron items
    'Iron Helmet': {
        "DESCRIPTION": 'An Iron helmet with +5 defense.',
        "VALUE": 30,
        "DEFENSE": 5,
        "EXPERIENCE": 40
    },
    'Iron Sword': {
        "DESCRIPTION": 'An Iron sword with +10 attack damage.',
        "VALUE": 35,
        "DAMAGE": 10,
        "EXPERIENCE": 50
    },
    'Iron Platelegs': {
        "DESCRIPTION": 'A set of Iron platelegs with +7 defense.',
        "VALUE": 50,
        "DEFENSE": 7,
        "EXPERIENCE": 60
    },
    'Iron Platebody': {
        "DESCRIPTION": 'An Iron platebody with +9 defense.',
        "VALUE": 60,
        "DEFENSE": 9,
        "EXPERIENCE": 70
    },

    # Silver Items
    'Silver Helmet': {
        "DESCRIPTION": 'A Silver helmet with +7 defense.',
        "VALUE": 60,
        "DEFENSE": 7,
        "EXPERIENCE": 80
    },
    'Silver Sword': {
        "DESCRIPTION": 'A Silver sword with +15 attack damage.',
        "VALUE": 70,
        "DAMAGE": 15,
        "EXPERIENCE": 100
    },
    'Silver Platelegs': {
        "DESCRIPTION": 'A set of Silver Platelegs with +9 defense.',
        "VALUE": 100,
        "DEFENSE": 9,
        "EXPERIENCE": 120
    },
    'Silver Platebody': {
        "DESCRIPTION": 'A Silver platebody with +11 defense.',
        "VALUE": 120,
        "DEFENSE": 11,
        "EXPERIENCE": 140
    },

    # Gold Items
    'Gold Helmet': {
        "DESCRIPTION": 'A Gold helmet with +9 defense.',
        "VALUE": 120,
        "DEFENSE": 9,
        "EXPERIENCE": 160
    },
    'Gold Sword': {
        "DESCRIPTION": 'A Gold sword with +20 attack damage.',
        "VALUE": 140,
        "DAMAGE": 20,
        "EXPERIENCE": 190
    },
    'Gold Platelegs': {
        "DESCRIPTION": 'A set of Gold platelegs with +11 defense.',
        "VALUE": 200,
        "DEFENSE": 11,
        "EXPERIENCE": 220
    },
    'Gold Platebody': {
        "DESCRIPTION": 'A Gold platebody with +13 defense.',
        "VALUE": 240,
        "DEFENSE": 13,
        "EXPERIENCE": 250
    },

    # Diamond Items
    'Diamond Helmet': {
        "DESCRIPTION": 'A Diamond helmet with +11 defense.',
        "VALUE": 240,
        "DEFENSE": 11,
        "EXPERIENCE": 350
    },
    'Diamond Sword': {
        "DESCRIPTION": 'A Diamond sword with excellent +30 damage.',
        "VALUE": 280,
        "DAMAGE": 30,
        "EXPERIENCE": 400
    },
    'Diamond Platelegs': {
        "DESCRIPTION": 'A set of Diamond platelegs with +13 defense.',
        "VALUE": 400,
        "DEFENSE": 13,
        "EXPERIENCE": 450
    },
    'Diamond Platebody': {
        "DESCRIPTION": 'A Diamond platebody with +15 defense.',
        "VALUE": 480,
        "DEFENSE": 15,
        "EXPERIENCE": 500
    },

    # Potions
     'Health Potion': {
        "DESCRIPTION": 'A potion that restores 50 HP.',
        "VALUE": 50,
        "EFFECT": 50
    },
     'Mana Potion': {
        "DESCRIPTION": 'A potion that restores 50 MP.',
        "VALUE": 50,
        "EFFECT": 50
    },
     'Super Health Potion': {
        "DESCRIPTION": 'A potion that fully restores HP.',
        "VALUE": 100,
        "EFFECT": myPlayer.max_hp
    },
     'Super Mana Potion': {
        "DESCRIPTION": 'A potion that fully restores MP.',
        "VALUE": 100,
        "EFFECT": myPlayer.max_mp
    },
     'Restore Potion': {
        "DESCRIPTION": 'A potion that fully restores HP and MP.',
        "VALUE": 200,
        "EFFECT": myPlayer.max_hp,
        "EFFECT_2": myPlayer.max_mp
    },

    # Staffs
     'Staff': {
        "DESCRIPTION": 'A basic staff with +10 magic damage.',
        "VALUE": 200,
        "DAMAGE": 10
    },
     'Magic Staff': {
        "DESCRIPTION": 'A magic staff with +20 magic damage.',
        "VALUE": 800,
        "DAMAGE": 20
    },
     'Greater Staff': {
        "DESCRIPTION": 'A greater magic staff with +30 magic damage.',
        "VALUE": 1500,
        "DAMAGE": 30
    },

    # Bags
     'Big Bag': {
        "DESCRIPTION": 'A big bag that can hold up to 50 items.',
        "VALUE": 200,
        "SIZE": 50
    },
     'Bigger Bag': {
        "DESCRIPTION": 'A bigger bag that can hold up to 75 items.',
        "VALUE": 500,
        "SIZE": 75
    },
     'Biggest Bag': {
        "DESCRIPTION": 'The biggest bag around! Holds up to 100 items!',
        "VALUE": 1000,
        "SIZE": 100
    },
}
