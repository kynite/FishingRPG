# CS 30
# Period 4
# Date : 12/9/2019
# Krutik Rana
# Program description : Arriving at a lake interactions
from characters import Player
from enemy import *
import enemy
from random import randint
from weapons import *
import weapons

player = Player(None, None)
best_weapons = player.most_powerful_weapon()
enemy_damage = best_weapons.damage


def residential():
    """Place where you will be able to buy items"""
    while True:
        # Welcomes user and asks if they will purchase or leave
        print('Welcome, would you like to purchase? or leave')
        action = input('choose an action: ')
        # Checks to see if user typed in purchase
        if action == 'purchase':
            print("doesn't work")
            pass
        # Checks to see if user typed in leave
        elif action == 'leave':
            # Exits the area and goes back to map
            break
        # Checks to see if user typed q to quit aswell
        elif action == 'q':
            # Exits the area aswell incase users were used to typing q
            break


def hooligan_lake():
    """Place to Combat easy fish"""
    while True:
        print('would you like to fish or leave')
        action = input('choose an action: ')
        # Checks to see if user typed in fish
        if action == 'fish':
            n = randint(1, 10)
            if n < 5:
                enemyencountersalmon()
            elif n < 8:
                enemyencountergoldfish()
            elif n < 11:
                enemyencounterguppy()
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
        print('would you like to fish or leave')
        action = input('choose an action: ')
        # Checks to see if user typed in fish
        if action == 'fish':
            print("doesn't work")
            pass
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
        print('would you like to fish or leave')
        action = input('choose an action: ')
        # Checks to see if user typed in fish
        if action == 'fish':
            print("doesn't work")
            pass
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
        print('would you like to fish or leave')
        action = input('choose an action: ')
        # Checks to see if user typed in fish
        if action == 'fish':
            print("doesn't work")
            pass
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
        print('would you like to fish or leave')
        action = input('choose an action: ')
        # Checks to see if user typed in fish
        if action == 'fish':
            enemyencounterethereal()
        # Checks to see if user typed in leave
        elif action == 'leave':
            # Exits the area and goes back to map
            break
        # Checks to see if user typed q to quit aswell
        elif action == 'q':
            # Exits the area aswell incase users were used to typing q
            break
