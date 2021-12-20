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
world_zone = {
    'Town': {
        DESCRIPTION: 'Center of town',
        EXAMINATION: ''
    },
    'Blacksmith': {
        DESCRIPTION: 'description',
        EXAMINATION: ''
    },
    'General Store': {
        DESCRIPTION: 'description',
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