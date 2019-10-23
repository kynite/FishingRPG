# CS 30
# Period 4
# Date : 10/22/2019
# Krutik Rana
# Program description : Creating dictionaries for the game

# Prints out a statement telling user a list of characters is upcoming
print("These are the characters:")
# Dictionary of friendly characters with values
characters = {
    "Xunerophore": "100", "Shopkeeper": "the person you can buy\
 items from."
             }
# A special loop with different lines for friendly characters
for k, v in characters.items():
    if k == "Xunerophore":
        print(f"The main character is {k} with {v}HP")
    elif k == "Shopkeeper":
        print(f"The {k} is {v}")

print("\n")
print("These are the enemies:")
# Dictionary of Enemies with values
enemies = {'Salmon': {'HP': 10, 'Attack': 2},
           'GoldFish': {'HP': 5, 'Attack': 1},
           'Guppy': {'HP': 3, 'Attack': 2},
           'Hammerhead Shark': {'HP': 15, 'Attack': 4},
           'The Great White': {'HP': 20, 'Attack': 8},
           'Saw Shark': {'HP': 25, 'Attack': 6},
           'Ethereal Ultimatum': {'HP': 1000, 'Attack': 20}
           }
# A Loop created for the enemies
for k, v in enemies.items():
    print(f"{k} is an enemy with {v['HP']}HP and {v['Attack']} Attack Damage")

# Prints out a bunch of dashed lines to seperate characters and inventory
print("----------------------------------------------------------------------")
# Prints text stating this is the inventory
print("This is the inventory:")
# Creates a dictionary of weapons
weapons_inventory = {'Stick': 1, 'Bat': 3, 'Spiked Bat': 5, 'Sword': 10}
# Creates a dictionary with a list of uses for the fishing rods
fishingrod_inventory = {'Basic rod': ['Salmon', 'GoldFish', 'Guppy'],
                        'Better rod': ['Hammerhead Sharks', 'The Great White',
                                       'Saw Sharks'],
                        'Ethereal Rod': ['Ethereal Ultimatum']
                        }
# Creates a dictionary of items that can heal you
healthitems_inventory = {'Sandwich': 20, 'Medkit': 50, 'Pills': '5',
                         'Grass': 10
                         }
# A print statement telling you its listing the weapons in the inventory
print("(Weapons)")
# A loop for all the weapons in the weapons inventory also stating the damage
for k, v in weapons_inventory.items():
    print(f"In your weapon stash you have a {k} that deals {v} Damage")
# Prints a seperating line
print("\n")
# A print statement telling you its listing the fishing rods in the inventory
print("(Fishing Rods)")
# A loop that loops through each rod and what fish you can capture with it
for k, v in fishingrod_inventory.items():
    for n in range(len(v)):
        print(f"In your fishing rod stash you have a {k} that allows you to \
capture {v[n]}")

# Prints a seperating line
print("\n")
# A print statement telling you its listing the health items in the inventory
print("(Health Items)")
# A loop that goes through each health item and how much the item heals for
for k, v in healthitems_inventory.items():
    print(f"In your backpack you are carrying {k} that heals for {v}HP")

# Prints out a bunch of dashed lines to seperate inventory and locations
print("----------------------------------------------------------------------")
# Prints text stating these are the locations
print("These are the locations:")
# Creates a dictionary with a list of fishes available at each lake
locations = {'Hooligan Lake': ['Salmon', 'GoldFish', 'Guppy'],
             'Where are we now Lake': ['Hammerhead Sharks', 'The Great White',
                                       'Saw Sharks'],
             'Ethereal Lake': ['Ethereal Ultim\
atum']
             }
# A loop that loops through each lake and what fish are at the lake
for k, v in locations.items():
    for n in range(len(v)):
        print(f"Travel to {k}? This Lake contains {v[n]}")
