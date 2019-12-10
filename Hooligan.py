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
            if n < 11:
                print('you encountered a Salmon!')
                current_enemy = Salmon()
                while player.hp > 0 or enemy.hp > 0:
                    userinp = input("type a to attack, type r to run")
                    if userinp == 'a':
                        current_enemy.hp -= enemy_damage
                        print(current_enemy.hp)
                    if userinp == 'r':
                        break
        # Checks to see if user typed in leave
        elif action == 'leave':
            # Exits the area and goes back to map
            break
        # Checks to see if user typed q to quit aswell
        elif action == 'q':
            # Exits the area aswell incase users were used to typing q
            break


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
