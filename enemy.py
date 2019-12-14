# CS 30
# Period 4
# Date : 12/9/2019
# Krutik Rana
# Program description : Enemies of the game and their attributes


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
        self.damage = 1


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
        self.hp = 30
        # Damage the enemy does to player
        self.damage = 2


class GreatWhite(Enemy):
    """An enemy the player might face"""
    def __init__(self):
        # Name of the enemy
        self.name = 'Great White Shark'
        # Amount of health the enemy has
        self.hp = 45
        # Damage the enemy does to player
        self.damage = 4


class SawShark(Enemy):
    """An enemy the player might face"""
    def __init__(self):
        # Name of the enemy
        self.name = 'Saw Shark'
        # Amount of health the enemy has
        self.hp = 60
        # Damage the enemy does to player
        self.damage = 3


class CatFish(Enemy):
    """An enemy the player might face"""
    def __init__(self):
        # name of the enemy
        self.name = 'Cat Fish'
        # Amount of health the enemy has
        self.hp = 100
        # Damage the enemy does to player
        self.damage = 6


class PufferFish(Enemy):
    """An enemy the player might face"""
    def __init__(self):
        # name of the enemy
        self.name = 'Puffer Fish'
        # Amount of health the enemy has
        self.hp = 150
        # Damage the enemy does to player
        self.damage = 10


class AnglerFish(Enemy):
    """An enemy the player might face"""
    def __init__(self):
        # name of the enemy
        self.name = 'Angler Fish'
        # Amount of health the enemy has
        self.hp = 70
        # Damage the enemy does to player
        self.damage = 15


class KillerWhale(Enemy):
    """An enemy the player might face"""
    def __init__(self):
        # name of the enemy
        self.name = 'Killer Whale'
        # Amount of health the enemy has
        self.hp = 800
        # Damage the enemy does to player
        self.damage = 5


class Kraken(Enemy):
    """An enemy the player might face"""
    def __init__(self):
        # name of the enemy
        self.name = 'Kraken'
        # Amount of health the enemy has
        self.hp = 1200
        # Damage the enemy does to player
        self.damage = 8


class Megalodon(Enemy):
    """An enemy the player might face"""
    def __init__(self):
        # name of the enemy
        self.name = 'Megalodon'
        # Amount of health the enemy has
        self.hp = 1800
        # Damage the enemy does to player
        self.damage = 15


class Ethereal(Enemy):
    """An enemy the player will have to face to win"""
    def __init__(self):
        # Name of the enemy
        self.name = 'Ethereal Ultimatum'
        # Amount of health the enemy has
        self.hp = 2500
        # Damage the enemy does to player
        self.damage = 20
