import cmd
import textwrap
import sys
import os
import time
import random

##### World Map #####

# World Zones
world_zone = {
    'Town': {
        "DESCRIPTION": 'Center of town'
    },
    'Swamp': {
        "DESCRIPTION": 'DESCRIPTION'
    },
    'Forest': {
        "DESCRIPTION": 'DESCRIPTION'
    },
    'Mine': {
        "DESCRIPTION": 'DESCRIPTION'
    },
    "Dragon's Lair": {
        "DESCRIPTION": 'DESCRIPTION'
    },
    "Graveyard": {
        "DESCRIPTION": 'DESCRIPTION'
    },
}

# Town Shops
shops = {
    'Blacksmith': {
        "DESCRIPTION": 'DESCRIPTION'
    },
    'Magic Shop': {
        "DESCRIPTION": 'DESCRIPTION'
    },
    'General Store': {
        "DESCRIPTION": 'DESCRIPTION'
    },
}
