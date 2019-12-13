# CS 30
# Period 4
# Date : 12/9/2019
# Krutik Rana
# Program description : Enemies of the game and their attributes
from Characters import Player
from random import randint

player = Player(None, None)
### Make Combat part of player class ###
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


def enemyencounterethereal():
    """ Enemy encounter for Ethereal Ultimatum"""
    # Tells user what enemy
    print('you come face to face with the Ethereal Ultimatum!')
    # Sets the enemy
    current_enemy = Ethereal()
    # while the player hp and enemy hp is above zero keep fighting
    while player.hp > 0 and current_enemy.hp > 0:
        # give the enemy an action
        enemy_action = randint(1, 2)
        # takes user input to attack
        userinp = input("type a to attack!: ")
        # checks if user typed in a to attack
        if userinp == 'a':
            # attacks the enemy and removes its health from weapon damage
            player.attack()
            # informs user of what happened
            print(f'>> The {current_enemy} has {current_enemy.hp} HP left')
        # checks if user typed in anything else
        else:
            # Tells user they missed
            print('You missed!')
        # if the enemy action is 1 and health is above zero then run this
        if enemy_action == 1 and current_enemy.hp > 0:
            # Damage the player
            player.hp -= current_enemy.damage
            # tell the user of what happened
            print(f'The {current_enemy.name} attacks and deals\
 {current_enemy.damage} Damage!')
            # tell the user how much health they have left
            if player.hp > 0:
                print(f'you have {player.hp} Hp left')
        # if the enemy action is 2 and health is above zero then run this
        elif enemy_action == 2 and current_enemy.hp > 0:
            # tell user what happened
            print(f'the {current_enemy.name} missed!')
    # if player hp is 0 then stop the game
    if player.hp <= 0:
        # tell user they are dead
        print('DEAD')
        # exit the game
        exit()
    # if user isnt dead
    else:
        # game winning text
        print(
              """>> You go to your fathers collection and add the Ethereal
Ultimatum. It got placed in the only slot that was missing a fish. You then
turn around to see your father out of the hospital with tears in his eyes.
THE END
              """)
        # end the game
        exit()


def enemyencountersalmon():
    """Enemy encounter for salmon"""
    # Same Code as Ethereal just with salmon and does not end game
    print('you encountered a Salmon!')
    current_enemy = Salmon()
    while player.hp > 0 and current_enemy.hp > 0:
        enemy_action = randint(1, 2)
        userinp = input("type a to attack!: ")
        if userinp == 'a':
            current_enemy.hp -= enemy_damage
            print(f'>> The {current_enemy} has {current_enemy.hp} HP left')
        else:
            print('You missed!')
        if enemy_action == 1 and current_enemy.hp > 0:
            player.hp -= current_enemy.damage
            print(f'The {current_enemy.name} attacks and deals\
 {current_enemy.damage} Damage!')
            if player.hp > 0:
                print(f'you have {player.hp} Hp left')
        elif enemy_action == 2 and current_enemy.hp > 0:
            print(f'the {current_enemy.name} missed!')
        else:
            print('invalid input')
    if player.hp <= 0:
        print('DEAD')
        exit()
    else:
        # tells user what enemy was killed and how much gold was earned
        print(f'You killed the {current_enemy.name} and obtained 5 gold')
        # Gives user the gold
        player.gold += 5
        # tells user how much gold they have in their inventory
        print(f'you have {str(player.gold)} gold in total')


def enemyencountergoldfish():
    """ Enemy encounter for gold fish"""
    # Same code as Salmon except enemy is now gold fish
    print('you encountered a Gold fish!')
    current_enemy = GoldFish()
    while player.hp > 0 and current_enemy.hp > 0:
        enemy_action = randint(1, 2)
        userinp = input("type a to attack!: ")
        if userinp == 'a':
            current_enemy.hp -= enemy_damage
            print(f'>> The {current_enemy} has {current_enemy.hp} HP left')
        else:
            print('You missed!')
        if enemy_action == 1 and current_enemy.hp > 0:
            player.hp -= current_enemy.damage
            print(f'The {current_enemy.name} attacks and deals\
 {current_enemy.damage} Damage!')
            if player.hp > 0:
                print(f'you have {player.hp} Hp left')
        elif enemy_action == 2 and current_enemy.hp > 0:
            print(f'the {current_enemy.name} missed!')
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
    """Enemy encounter for guppy"""
    # Same code as salmon except enemy is now guppy
    print('you encountered a Guppy!')
    current_enemy = Guppy()
    while player.hp > 0 and current_enemy.hp > 0:
        enemy_action = randint(1, 2)
        userinp = input("type a to attack!: ")
        if userinp == 'a':
            current_enemy.hp -= enemy_damage
            print(f'>> The {current_enemy} has {current_enemy.hp} HP left')
        else:
            print('You missed!')
        if enemy_action == 1:
            player.hp -= current_enemy.damage
            print(f'The {current_enemy.name} attacks and deals\
 {current_enemy.damage} Damage!')
            if player.hp > 0:
                print(f'you have {player.hp} Hp left')
        elif enemy_action == 2:
            print(f'the {current_enemy.name} missed!')
        else:
            print('invalid input')
    if player.hp <= 0:
        print('DEAD')
        exit()
    else:
        print(f'You killed the {current_enemy.name} and obtained 10 gold')
        player.gold += 10
        print(f'you have {str(player.gold)} gold in total')
