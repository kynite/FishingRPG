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
        # Value of the weapon
        self.value = 50


class SpikedBat(WeaponName):
    """A weapon that the player can use"""
    def __init__(self):
        # Name of the weapon
        self.name = 'Spiked Bat'
        # Damage of the weapon
        self.damage = 5
        # Value of the weapon
        self.value = 150


class Shovel(WeaponName):
    """A weapon that the player can use"""
    def __init__(self):
        # Name of the weapon
        self.name = 'Shovel'
        # Damage of the weapon
        self.damage = 10
        # Value of the weapon
        self.value = 500


class Halberd(WeaponName):
    """A weapon that the player can use"""
    def __init__(self):
        # Name of the weapon
        self.name = 'Halberd'
        # Damage of the weapon
        self.damage = 20
        # Value of the weapon
        self.value = 700


class Sword(WeaponName):
    """A weapon that the player can use"""
    def __init__(self):
        # Name of the weapon
        self.name = 'Sword'
        # Damage of the weapon
        self.damage = 30
        # Value of the weapon
        self.value = 850


class Cutlass(WeaponName):
    """A weapon that the player can use"""
    def __init__(self):
        # Name of the weapon
        self.name = 'Halberd'
        # Damage of the weapon
        self.damage = 50
        # Value of the weapon
        self.value = 1200


class Zweihander(WeaponName):
    """A weapon that the player can use"""
    def __init__(self):
        # Name of the weapon
        self.name = 'Zweihänder'
        # Damage of the weapon
        self.damage = 120
        # Value of the weapon
        self.value = 2500


class Kopesh(WeaponName):
    """A weapon that the player can use"""
    def __init__(self):
        # Name of the weapon
        self.name = 'Kopesh'
        # Damage of the weapon
        self.damage = 300
        # Value of the weapon
        self.value = 5000


class Shotel(WeaponName):
    """A weapon that the player can use"""
    def __init__(self):
        # Name of the weapon
        self.name = 'Shotel'
        # Damage of the weapon
        self.damage = 500
        # Value of the weapon
        self.value = 10000


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
        # Value of food
        self.value = 100


class Bread(Consumable):
    """A consumable the player can use to heal"""
    def __init__(self):
        # Name of the consumable
        self.name = 'Bread'
        # Healing value of the consumable
        self.healing_value = 5
        # Value of food
        self.value = 60


class Maggot(Consumable):
    """A consumable the player can use to heal"""
    def __init__(self):
        # Name of the consumable
        self.name = 'Maggot'
        # Healing value of the consumable
        self.healing_value = 1


class Soup(Consumable):
    """A consumable the player can use to heal"""
    def __init__(self):
        # Name of the consumable
        self.name = 'Soup'
        # Healing value of the consumable
        self.healing_value = 30
        # Value of food
        self.value = 400


class BurgerKingCombo(Consumable):
    """A consumable the player can use to heal"""
    def __init__(self):
        # Name of the consumable
        self.name = 'Burger King Combo'
        # Healing value of the consumable
        self.healing_value = 80
        # Value of food
        self.value = 600


class Medkit(Consumable):
    """A consumable the player can use to heal"""
    def __init__(self):
        # Name of the consumable
        self.name = 'Medkit'
        # Healing value of the consumable
        self.healing_value = 100
        # Value of food
        self.value = 1000


class IceCream(Consumable):
    """A consumable the player can use to heal"""
    def __init__(self):
        # Name of the consumable
        self.name = 'Ice Cream'
        # Healing value of the consumable
        self.healing_value = 18
        # value of food
        self.value = 150


class GranolaBar(Consumable):
    """A consumable the player can use to heal"""
    def __init__(self):
        # Name of the consumable
        self.name = 'Granola Bar'
        # Healing value of the consumable
        self.healing_value = 20
        self.value = 300
