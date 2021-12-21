import cmd
import textwrap
import sys
import os
import time
import random

##### World Map #####

# Location constants
ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'

# TODO: Finalize locations and fill out descriptions
# World Zones
world_zone = {
    'Town': {
        DESCRIPTION: 'Center of town',
        EXAMINATION: ''
    },
    'Castle': {
        DESCRIPTION: 'description',
        EXAMINATION: ''
    },
    'Forest': {
        DESCRIPTION: 'description',
        EXAMINATION: ''
    },
    'Mine': {
        DESCRIPTION: 'description',
        EXAMINATION: ''
    },
    "Dragon's Lair": {
        DESCRIPTION: 'description',
        EXAMINATION: ''
    },
}

# Town Shops
shops = {
    'Blacksmith': {
        DESCRIPTION: 'description',
        EXAMINATION: ''
    },
    'Magic Shop': {
        DESCRIPTION: 'description',
        EXAMINATION: ''
    },
    'General Store': {
        DESCRIPTION: 'description',
        EXAMINATION: ''
    },
}