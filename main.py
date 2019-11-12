# CS 30
# Period 4
# Date : 11/12/2019
# Krutik Rana
# Program description : Orginizing the game into functions


def friendly_characters():
    """Loops for friendly character in the game"""
    # Special for loop that lists the friendly character in the game
    for k, v in characters.items():
        if k == "Xunerophore":
            print(f"The main character is {k} with {v}HP")
        elif k == "Shopkeeper":
            print(f"The {k} is {v}")


def enemies_list():
    """Loop for enemies in the game"""
    # Special loop that lists the enemies in the game
    for k, v in enemies.items():
        print(f"{k} is an enemy with {v['HP']}HP and {v['Attack']} Attack\
        Damage")


def inventory():
    """Commands to access the characters inventory"""
    # While loop to continously play
    while True:
        # Print statement detailing how to go to the last menu
        print('\ntype q to go back to previous menu')
        # Aquiring user input for what they want to access of the inventory
        user = input('action: ')
        # Making the user input all lower case to match if and elif statements
        user = user.lower()
        # Checks to see if the user typed weapon
        if user == 'weapon':
            # Loop that lists out weapons and their stats
            for k, v in weapons_inventory.items():
                print(f"In your weapon stash you have a {k} that deals {v} Dam\
age")
        # Checks to see if user typed fishing rod
        elif user == 'fishing rod':
            # Loop that lists out fishing rods in inventory and their stats
            for k in fishingrod_inventory:
                print(f"\nIn your fishing rod stash you have a {k}:")
                for v in fishingrod_inventory[k]:
                    print(f"This fishing rod can capture {v}")
        # Checks to see if user typed heal
        elif user == 'heal':
            # Loop that lists out health items in inventory
            for k, v in healthitems_inventory.items():
                print(f"In your backpack you are carrying {k} that heals\
 for {v}HP")
        # Checks to see if user typed q
        elif user == 'q':
            # Quits this part of the menu
            break
        # Checks to see if the user typed anything else
        else:
            # Tells user it is an invalid option
            print('Invalid option')


def location():
    """Commands that allow you to travel to different locations"""
    # While loop for continous play
    while True:
        # Tells user to type q to go to the previous menu
        print('\ntype q to go back to previous menu')
        # Asks for user input of what location they would like to go to
        user = input('select location: ')
        # Makes all user inputs lower cased to match if and elif statements
        user = user.lower()
        # Checks to see if user typed in specific location
        if user == 'hooligan lake':
            # prints out that they are traveling to that location
            print('traveling to Hooligan lake')
        # Checks to see if user typed in specific location
        elif user == 'where are we now lake':
            # prints out that they are traveling to that location
            print('traveling to Where are we now lake')
        # Checks to see if user typed in specific location
        elif user == 'ethereal lake':
            # prints out that they are traveling to that location
            print('traveling to Ethereal lake')
        # Checks to see if user typed in q
        elif user == 'q':
            # Quits this part of the menu
            break
        # Checks to see if user typed in specific location
        elif user == 'residential lake':
            # prints out that they are traveling to that location
            print('traveling to Residential Lake')
        # Checks to see if user typed anything else
        else:
            # Tells user it is an invalid option
            print('invalid option')


def ingame_menu():
    """The menu that appears after the main menu/the first menu"""
    # While loop for continous play
    while True:
        # Tells user that typing q goes to the main menu
        print('type q to go back to the main menu')
        # Asks for user input
        menu = input('type location or inventory: ')
        # Makes all the user input into lower case
        menu = menu.lower()
        # Checks to see if user typed inventory
        if menu == 'inventory':
            # Tells user to type in certain commands to access further menus
            print('type [weapon], [fishing rod], [heal]')
            # Runs the inventory function
            inventory()
        # Checks to see if user typed location
        elif menu == 'location':
            # A loop that lists out the locations
            for k in locations:
                print(f"\nTravel to {k}?")
                for v in locations[k]:
                    print(f"This Lake contains {v}")
            # Runs the location function
            location()
        # Checks to see if user typed in q
        elif menu == 'q':
            # Goes to main menu
            break
        # Checks to see if anything else was typed in
        else:
            # Tells user that was an invalid selection
            print('invalid select again')


def main_menu():
    """The main menu of the game, the first one you see"""
    # While loop for continous play
    while True:
        # Prints out name of the game
        print('Ethereal Ultimatum')
        # Just something to seperate the title
        print('----------------')
        # Informs user to type y to play the game
        print('type y to play the game')
        # Informs user to type q to quit the game
        print('type q to quit the game')
        # Gets user input
        selection = input('Make your selection: ')
        # Converts user input into all lower case
        selection = selection.lower()
        # Checks to see if y is typed
        if selection == 'y':
            # Runs the ingame menu function
            ingame_menu()
        # Checks to see if q is typed
        elif selection == 'q':
            # Ends the game
            break
            # Tells user game has ended
            print('game ended')
        # Checks to see if anything else is typed
        else:
            # Tells user it is an invalid option
            print('Invalid option')


# Dictionary of friendly characters with values
characters = {
    "Xunerophore": "100", "Shopkeeper": "the person you can buy\
 items from."
             }

# Dictionary of Enemies with values
enemies = {'Salmon': {'HP': 10, 'Attack': 2},
           'GoldFish': {'HP': 5, 'Attack': 1},
           'Guppy': {'HP': 3, 'Attack': 2},
           'Hammerhead Shark': {'HP': 15, 'Attack': 4},
           'The Great White': {'HP': 20, 'Attack': 8},
           'Saw Shark': {'HP': 25, 'Attack': 6},
           'Ethereal Ultimatum': {'HP': 1000, 'Attack': 20}
           }

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

# Creates a dictionary with a list of fishes available at each lake
locations = {'Hooligan Lake': ['Salmon', 'GoldFish', 'Guppy'],
             'Where are we now Lake': ['Hammerhead Sharks', 'The Great White',
                                       'Saw Sharks'],
             'Ethereal Lake': ['Ethereal Ultim\
atum'], 'Residential Lake': ['Shopkeeper'],
             }
# Calls main menu function
main_menu()
