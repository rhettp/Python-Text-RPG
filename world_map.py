import cmd
import textwrap
import sys
import os
import time
import random

##### World Map #####

# Location constants
ZONENAME = ''
DESCRIPTION = ''
EXAMINATION = ''

# TODO: Finalize locations and fill out descriptions
world_zone = {
    't1': {
        ZONENAME: 'Town',
        DESCRIPTION: 'Center of town',
        EXAMINATION: ''
    },
    't2': {
        ZONENAME: 'Blacksmith Shop',
        DESCRIPTION: 'description',
        EXAMINATION: ''
    },
    't3': {
        ZONENAME: 'General Store',
        DESCRIPTION: 'description',
        EXAMINATION: ''
    },
    't4': {
        ZONENAME: 'Castle',
        DESCRIPTION: 'description',
        EXAMINATION: ''
    },
    'f1': {
        ZONENAME: 'Forest',
        DESCRIPTION: 'description',
        EXAMINATION: ''
    },
    'm1': {
        ZONENAME: 'Mine',
        DESCRIPTION: 'description',
        EXAMINATION: ''
    },
    'd1': {
        ZONENAME: "Dragon's Lair",
        DESCRIPTION: 'description',
        EXAMINATION: ''
    },
}