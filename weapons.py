# CS 30
# Period 4
# Date : 12/9/2019
# Krutik Rana
# Program description : Weapons and healing items of game


class WeaponName:
    """Parent Class to child classes in terms of naming"""
    def __str__(self):
        """Gets the name of a child class and makes it a string"""
        return self.name


class Stick(WeaponName):
    """A weapon that the player can use"""
    def __init__(self):
        # Name of the weapon
        self.name = 'stick'
        # Damage of the weapon
        self.damage = 1


class Bat(WeaponName):
    """A weapon that the player can use"""
    def __init__(self):
        # Name of the weapon
        self.name = 'Bat'
        # Damage of the weapon
        self.damage = 3
        self.value = 50


class SpikedBat(WeaponName):
    """A weapon that the player can use"""
    def __init__(self):
        # Name of the weapon
        self.name = 'Spiked Bat'
        # Damage of the weapon
        self.damage = 5
        self.value = 150


class Sword(WeaponName):
    """A weapon that the player can use"""
    def __init__(self):
        # Name of the weapon
        self.name = 'Sword'
        # Damage of the weapon
        self.damage = 10
        self.value = 500


class Consumable:
    """Parent class for all consumable items"""
    def __init__(self):
        """Gives a warning when a raw consumable is created"""
        raise NotImplementedError("dont create raw objects")

    def __str__(self):
        """String method describing the consumable"""
        return "{} (+{} HP)".format(self.name, self.healing_value)


class Sandwich(Consumable):
    """A consumable the player can use to heal"""
    def __init__(self):
        # Name of the consumable
        self.name = 'Sandwich'
        # Healing value of the consumable
        self.healing_value = 10
        self.value = 100


class Bread(Consumable):
    def __init__(self):
        # Name of the consumable
        self.name = 'Bread'
        # Healing value of the consumable
        self.healing_value = 5
        self.value = 60


class Maggot(Consumable):
    def __init__(self):
        # Name of the consumable
        self.name = 'Maggot'
        # Healing value of the consumable
        self.healing_value = 1
        self.value = 3
