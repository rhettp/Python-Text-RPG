from prompts.clear_console import *
from items.items import *
from character.player import *
from gameplay.movement import *

##### Inventory #####

# Player inventory as list
inventory = []

# Add item to inventory
def addToInventory(item):
    inventory.append(item)

# Remove item from inventory
def removeItem(item):
    inventory.remove(item)

# Drop/remove player determined number of items from inventory
def dropItemPrompt():
    print("Which item would you like to drop?")
    while True:
        item = input('> ')
        if item in inventory:
            print("How many {}(s) do you want to drop?".format(item))
            while True:
                print("> ", end='')
                try:
                    number = int(input())
                except:
                    print("Please enter a valid number.")
                else:
                    if number == 0:
                        clearConsole()
                        print_location()
                        print("No {}s were dropped.".format(item))
                        print("\n")
                        inventory_prompt()
                        break
                    elif number == 1:
                        clearConsole()
                        print_location()
                        print("You dropped a(n) {}".format(item))
                        print("\n")
                        removeItem(item)
                        inventory_prompt()
                        break
                    elif number > inventory.count(item):
                        print("You don't have {} {}s.".format(number, item))
                        continue
                    elif number > 1 and number <= inventory.count(item):
                        clearConsole()
                        print_location()
                        print("You dropped {} {}s.".format(number, item))
                        print("\n")
                        for i in range(number):
                            removeItem(item)
                        inventory_prompt()
                        break
                    else:
                        print("Please enter a valid number.")
                        continue
            break
        elif item in ["all","All", "ALL"]:
            clearConsole()
            print_location()
            print("All items were dropped.")
            inventory.clear()
            print("\n")
            inventory_prompt()
            break
        elif item in ["none", "None", "NONE", "back", "Back", "BACK"]:
            clearConsole()
            print_location()
            inventory_prompt()
            break
        else:
            print("Please enter a valid item.")
            continue

# Show player inventory with item count
def showIventory():
    item_set = set(inventory)
    if not inventory:
        print("Your inventory is empty.")
    else:
        for item in item_set:
            if item not in ["Super Health Potion", "Super Mana Potion", "Staff", "Silver Platelegs",\
                 "Silver Platebody", "Diamond Platelegs", "Diamond Platebody", "Copper Platelegs", "Copper Platebody"]:
                print("{} \t    ({}) : {}".format(item, inventory.count(item), items[item]["DESCRIPTION"]))
            elif item in ["Diamond Platebody", "Diamond Platelegs", "Super Mana Potion"]:
                print("{}   ({}) : {}".format(item, inventory.count(item), items[item]["DESCRIPTION"]))
            elif item == "Staff":
                print("{}\t\t    ({}) : {}".format(item, inventory.count(item), items[item]["DESCRIPTION"]))
            elif item == "Super Health Potion":
                print("{} ({}) : {}".format(item, inventory.count(item), items[item]["DESCRIPTION"]))
            else:
                print("{}    ({}) : {}".format(item, inventory.count(item), items[item]["DESCRIPTION"]))

# Inventory Prompt
def inventory_prompt():
    showIventory()
    print("\n")
    myPlayer.display_stats()
    print("What would you like to do?")
    print("1) Drop item")
    print("2) Back")

    while True:
        action = input('> ')
        if action == '1':     # Drop item
            clearConsole()
            print_location()
            if not inventory:
                inventory_prompt()
                break
            else:
                showIventory()
                print("\n")
                myPlayer.display_stats()
                dropItemPrompt()
                break
        elif action == '2':     # Back
            clearConsole()
            print_location()
            myPlayer.display_stats()
            break
        else:
            print("Please enter a valid action.")
            continue
