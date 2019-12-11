# CS 30
# Period 4
# Date : 12/9/2019
# Krutik Rana
# Program description : Enemies of the game and their attributes
from characters import Player
from random import randint
from weapons import *
import weapons

player = Player(None, None)
best_weapons = player.most_powerful_weapon()
enemy_damage = best_weapons.damage


class Enemy():
    """Parent class of Enemies determining name and health"""
    def __init__(self):
        # Creates a warning to not create raw enemies
        raise NotImplementedError("Do not create raw Enemy objects")

    def __str__(self):
        """Gets the name of the child class and makes it a string"""
        return self.name

    def is_alive(self):
        """Gets the amount of health the enemy has to see if it still lives"""
        return self.hp > 0


class Salmon(Enemy):
    """An enemy the player might face"""
    def __init__(self):
        # Name of the enemy
        self.name = "Salmon"
        # Amount of health the enemy has
        self.hp = 10
        # Damage the enemy does to player
        self.damage = 2


class GoldFish(Enemy):
    """An enemy the player might face"""
    def __init__(self):
        # Name of the enemy
        self.name = 'Goldfish'
        # Amount of health the enemy has
        self.hp = 5
        # Damage the enemy does to player
        self.damage = 1


class Guppy(Enemy):
    """An enemy the player might face"""
    def __init__(self):
        # Name of the enemy
        self.name = 'Guppy'
        # Amount of health the enemy has
        self.hp = 3
        # Damage the enemy does to player
        self.damage = 2


class Hammerhead(Enemy):
    """An enemy the player might face"""
    def __init__(self):
        # Name of the enemy
        self.name = 'Hammerhead Shark'
        # Amount of health the enemy has
        self.hp = 15
        # Damage the enemy does to player
        self.damage = 4


class GreatWhite(Enemy):
    """An enemy the player might face"""
    def __init__(self):
        # Name of the enemy
        self.name = 'Great White Shark'
        # Amount of health the enemy has
        self.hp = 20
        # Damage the enemy does to player
        self.damage = 8


class SawShark(Enemy):
    """An enemy the player might face"""
    def __init__(self):
        # Name of the enemy
        self.name = 'Saw Shark'
        # Amount of health the enemy has
        self.hp = 25
        # Damage the enemy does to player
        self.damage = 6


class Ethereal(Enemy):
    """An enemy the player will have to face to win"""
    def __init__(self):
        # Name of the enemy
        self.name = 'Ethereal Ultimatum'
        # Amount of health the enemy has
        self.hp = 1000
        # Damage the enemy does to player
        self.damage = 20


def enemyencountersalmon():
    print('you encountered a Salmon!')
    current_enemy = Salmon()
    while player.hp > 0 and current_enemy.hp > 0:
        enemy_action = randint(1, 2)
        userinp = input("type a to attack, type r to run: ")
        if userinp == 'a':
            current_enemy.hp -= enemy_damage
            print(current_enemy.hp)
        if enemy_action == 1:
            player.hp -= current_enemy.damage
            print(f'The {current_enemy.name} attack and dealt\
 {current_enemy.damage} Damage!')
            print(f'you have {player.hp} Hp left')
        elif enemy_action == 2:
            print(f'the {current_enemy.name} missed!')
        elif userinp == 'r':
            break
        else:
            print('invalid input')
    if player.hp <= 0:
        print('DEAD')
        exit()
    else:
        print(f'You killed the {current_enemy.name} and obtained 5 gold')
        player.gold += 5
        print(f'you have {str(player.gold)} gold in total')


def enemyencountergoldfish():
    print('you encountered a Gold fish!')
    current_enemy = GoldFish()
    while player.hp > 0 and current_enemy.hp > 0:
        enemy_action = randint(1, 2)
        userinp = input("type a to attack, type r to run: ")
        if userinp == 'a':
            current_enemy.hp -= enemy_damage
            print(current_enemy.hp)
        if enemy_action == 1:
            player.hp -= current_enemy.damage
            print(f'The {current_enemy.name} attack and dealt\
 {current_enemy.damage} Damage!')
            print(f'you have {player.hp} Hp left')
        elif enemy_action == 2:
            print(f'the {current_enemy.name} missed!')
        elif userinp == 'r':
            break
        else:
            print('invalid input')
    if player.hp <= 0:
        print('DEAD')
        exit()
    else:
        print(f'You killed the {current_enemy.name} and obtained 2 gold')
        player.gold += 2
        print(f'you have {str(player.gold)} gold in total')


def enemyencounterguppy():
    print('you encountered a Guppy!')
    current_enemy = Guppy()
    while player.hp > 0 and current_enemy.hp > 0:
        enemy_action = randint(1, 2)
        userinp = input("type a to attack, type r to run: ")
        if userinp == 'a':
            current_enemy.hp -= enemy_damage
            print(current_enemy.hp)
        if enemy_action == 1:
            player.hp -= current_enemy.damage
            print(f'The {current_enemy.name} attack and dealt\
 {current_enemy.damage} Damage!')
            print(f'you have {player.hp} Hp left')
        elif enemy_action == 2:
            print(f'the {current_enemy.name} missed!')
        elif userinp == 'r':
            break
        else:
            print('invalid input')
    if player.hp <= 0:
        print('DEAD')
        exit()
    else:
        print(f'You killed the {current_enemy.name} and obtained 10 gold')
        player.gold += 10
        print(f'you have {str(player.gold)} gold in total')
