# CS 30
# Period 4
# Date : 12/9/2019
# Krutik Rana
# Program description : Arriving at a lake interactions
from enemy import *
from random import randint
from world import player


def residential():
    """Place where you will be able to buy items"""
    while True:
        # Welcomes user and asks if they will purchase or leave
        print('Welcome, would you like to [purchase]? or [leave]')
        action = input('choose an action: ')
        # Checks to see if user typed in purchase
        if action == 'purchase':
            print('if the item has an HP value then it is a consumable other\
wise it is a weapon')
            print('type the name of the item to buy it')
            # Runs shop function
            player.buyshop()
        # Checks to see if user typed in leave
        elif action == 'leave':
            # Exits the area and goes back to map
            break
        # Checks to see if user typed q to quit aswell
        elif action == 'q':
            # Exits the area aswell incase users were used to typing q
            break
        else:
            print('invalid input')


def hooligan_lake():
    """Place to Combat easy fish"""
    while True:
        print('would you like to [fish] or [leave]')
        action = input('choose an action: ')
        # Checks to see if user typed in fish
        if action == 'fish':
            # Chooses a random number
            n = randint(1, 10)
            # Check if number is less than 5
            if n < 5:
                # run fight command and print out enemy name
                print('You fished up a Guppy')
                player.fight(Guppy(), 10)
            # Check if number is less than 8
            elif n < 8:
                # run fight command and print out enemy name
                print('You fished up a Goldfish')
                player.fight(GoldFish(), 15)
            # Check if number is less than 11
            elif n < 11:
                # run fight command and print out enemy name
                print('You fished up a Salmon')
                player.fight(Salmon(), 17)
        # Checks to see if user typed in leave
        elif action == 'leave':
            # Exits the area and goes back to map
            break
        # Checks to see if user typed q to quit aswell
        elif action == 'q':
            # Exits the area aswell incase users were used to typing q
            break
        else:
            print('invalid input')


def where_are_we_now():
    """Place to combat normal difficulty fish"""
    while True:
        print('would you like to [fish] or [leave]')
        action = input('choose an action: ')
        # Checks to see if user typed in fish
        if action == 'fish':
            # Same code as hooligan_lake()
            n = randint(1, 10)
            if n < 4:
                print('You fished up a Hammerhead Shark')
                player.fight(Hammerhead(), 24)
            if n < 8:
                print('You fished up a Great White Shark')
                player.fight(GreatWhite(), 28)
            if n < 11:
                print('You fished up a Saw Shark')
                player.fight(SawShark(), 34)
        # Checks to see if user typed in leave
        elif action == 'leave':
            # Exits the area and goes back to map
            break
        # Checks to see if user typed q to quit aswell
        elif action == 'q':
            # Exits the area aswell incase users were used to typing q
            break


def kytersize():
    """Place to combat hard fish"""
    while True:
        print('would you like to [fish] or [leave]')
        action = input('choose an action: ')
        # Checks to see if user typed in fish
        if action == 'fish':
            # Same code as hooligan_lake()
            n = randint(1, 50)
            if n < 25:
                player.fight(CatFish(), 50)
            elif n < 40:
                player.fight(PufferFish(), 65)
            elif n < 51:
                player.fight(AnglerFish(), 100)
        # Checks to see if user typed in leave
        elif action == 'leave':
            # Exits the area and goes back to map
            break
        # Checks to see if user typed q to quit aswell
        elif action == 'q':
            # Exits the area aswell incase users were used to typing q
            break


def juliot():
    """Place to combat Legendary fish"""
    while True:
        print('would you like to [fish] or [leave]')
        action = input('choose an action: ')
        # Checks to see if user typed in fish
        if action == 'fish':
            # Same code as hooligan_lake()
            n = randint(1, 1000)
            if n < 600:
                player.fight(KillerWhale(), 400)
            elif n < 850:
                player.fight(Kraken(), 600)
            elif n < 1001:
                player.fight(Megalodon(), 1000)
        # Checks to see if user typed in leave
        elif action == 'leave':
            # Exits the area and goes back to map
            break
        # Checks to see if user typed q to quit aswell
        elif action == 'q':
            # Exits the area aswell incase users were used to typing q
            break


def ethereal():
    """Place to combat the game ending final boss fish"""
    while True:
        print('would you like to [fish] or [leave]')
        action = input('choose an action: ')
        # Checks to see if user typed in fish
        if action == 'fish':
            # Runs final boss command and special print text
            print('you come face to face with the Ethereal Ultimatum!')
            player.finalboss()
        # Checks to see if user typed in leave
        elif action == 'leave':
            # Exits the area and goes back to map
            break
        # Checks to see if user typed q to quit aswell
        elif action == 'q':
            # Exits the area aswell incase users were used to typing q
            break
