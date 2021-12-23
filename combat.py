import cmd
import textwrap
import sys
import os
import time
import random
from player import *
from enemy import *

##### Combat #####

def combat_prompt():
    print("What would you like to do?")
    print("1) Attack")
    print("2) Magic")
    print("3) Items-")
    
    while True:
        action = input("> ")
        if action == '1':
            attack(goblin)
            combat_prompt()
        elif action == '2':
            print("Magic")
        elif action == '3':
            print("Items")
        else:
            print("Please enter a valid action")
            continue

def attack(enemy):
    enemy.hp -= myPlayer.attack
    if enemy.is_dead():
        print("You killed the {}!".format(enemy.name))
    else:
        print("The {} has {} hp left.".format(enemy.name, enemy.hp))

combat_prompt()