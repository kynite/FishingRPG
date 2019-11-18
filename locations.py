# CS 30
# Period 4
# Date : 11/18/2019
# Krutik Rana
# Program description : Locations in a seperate file
from tabulate import tabulate


def location():
    """Commands that allow for movement on the map"""
    # While loop for continous play
    while True:
        # Array of the map, formated using tabulate
        map = [[None, None, 'Ethereal Lake', None, None],
               [None, None, None, None, None],
               ['Juilot Lake', None, None, None, 'Kytersize Lake'],
               [None, None, None, None, None],
               [None, 'Where are we now lake', None, 'Hooligan Lake', None],
               [None, None, 'Residential Lake', None, None],
               [None, None, None, 'Player', 'Home']]
        # Prints map out in a grid style using tabulate
        print(tabulate(map, tablefmt="grid"))
        # Tells user to type q to go to the previous menu
        print('\ntype q to go back to previous menu')
        print('North')
        print('West')
        print('East')
        print('South')
        # Asks for user input of what location they would like to go to
        user = input('Select a Movement: ')
        # Makes all user inputs lower cased to match if and elif statements
        user = user.lower()
        # Checks to see if user typed in movement command
        if user == 'north':
            # prints out Movement
            print('Travelling North!')
        # Checks to see if user typed in movement command
        elif user == 'west':
            # prints out Movement
            print('Travelling West!')
        # Checks to see if user typed in movement command
        elif user == 'east':
            # prints out Movement
            print('Travelling East!')
        # Checks to see if user typed in movement command
        elif user == 'south':
            # prints out Movement
            print('Travelling South!')
            # Checks to see if user typed q
        elif user == 'q':
            # Quits this part of the menu
            break
        # Checks to see if user typed anything else
        else:
            # Tells user it is an invalid option
            print('invalid option')


# Creates a dictionary with a list of fishes available at each lake
locations = {'Hooligan Lake': ['Salmon', 'GoldFish', 'Guppy'],
             'Where are we now Lake': ['Hammerhead Sharks', 'The Great White',
                                       'Saw Sharks'],
             'Ethereal Lake': ['Ethereal Ultim\
atum'], 'Residential Lake': ['Shopkeeper'],
             }
