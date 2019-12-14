# CS 30
# Period 4
# Date : 12/9/2019
# Krutik Rana
# Program description : The Player and extra info about characters
import weapons as wp
from random import randint
from enemy import *


class Player:
    """
    Player class which contains player logic and is what the user controls.
    Holds healing capability and best weapon
    """
    def __init__(self, x, y):
        # Player inventory
        self.inventory = [wp.Stick(), wp.Bread(), wp.Maggot()]
        self.playername = "X"  # Player name
        self.hp = 100  # Player health
        self.gold = 0  # Player gold
        # Shop Inventory
        self.shop = [
                     wp.Bat(), wp.SpikedBat(), wp.Shovel(), wp.Halberd(),
                     wp.Sword(), wp.Cutlass(), wp.Zweihander(), wp.Kopesh(),
                     wp.Shotel(), wp.Sandwich(), wp.Bread(), wp.Soup(),
                     wp.BurgerKingCombo(), wp.Medkit(),  wp.IceCream(),
                     wp.GranolaBar()
                     ]

    def print_inventory(self):
        """Prints the players inventory"""
        print("Backpack:")
        # Loop for each item in the players inventory
        for item in self.inventory:
            print('* ' + str(item))
        # Assigns the best weapon
        best_weapon = self.most_powerful_weapon()
        # print statement telling the best weapon in inventory
        print("Your best weapon is your {}".format(best_weapon))

    def most_powerful_weapon(self):
        """Determines the most damaging weapon in Players inventory"""
        # sets inital damge to 0
        max_damage = 0
        # sets the best weapon to nothing
        best_weapon = None
        # Loop for each item in inventory
        for item in self.inventory:
            # Code adapted from Make Your own Python Text Based Adventure
            # tries to see if the item damage is greator than the current max
            # damage and then replaces the best weapon in inventory
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass
        # sends the best weapon to function
        return best_weapon

    def __str__(self):
        """Gets the name of the player and makes it a string"""
        return self.playername

    def heal(self):
        """
        Heals the player making the players HP go up, Code adapted from Make
        Your own Python Text Based Adventure
        """
        # Creates a list of consumables from the players inventory
        consumables = [item for item in self.inventory
                       if isinstance(item, wp.Consumable)]
        # If there are no consumables then tells player he has not healing item
        if not consumables:
            print("You don't have any items to heal you!")
            return
        elif self.hp == 100:
            print('Your Full HP!')
            return
        # Shows an item that can heal you
        for i, item in enumerate(consumables, 1):
            print("Choose an item to use to heal: ")
            print("{}. {}".format(i, item))

            valid = False
            while not valid:
                print("type the number associated with the item to use otherw\
ise type q to not use")
                # Gets user input of what item they want to use to heal
                choice = input("")
                # Checks to see if user typed in q
                if choice == 'q':
                    # Deny the heal of that particular item/cancel the heal
                    break
                # Any other option
                else:
                    # Uses the item and heals the player and then removes the
                    # item from the players inventory
                    try:
                        to_eat = consumables[int(choice) - 1]
                        self.hp = min(100, self.hp + to_eat.healing_value)
                        self.inventory.remove(to_eat)
                        print("Current HP: {}".format(self.hp))
                        valid = True
                    except (ValueError, IndexError):
                        print("Invalid choice, try again.")

    def buyshop(self):
        # For loop for each item in shop
        for item in self.shop:
            print(f'you can buy a {item} for {item.value} gold')
        print('typed anything else to leave shop menu')
        # Takes user input of what user wants to buy
        userinp = input('What would you like to buy?: ')
        # lowers user input to match if/elif statements
        userinp = userinp.lower()
        # Checks if user typed in specific item
        if userinp == 'bat':
            # Checks if user has amount of gold to see if user can buy it
            if self.gold >= 50:
                # sets the item from the list into a single value
                item = self.shop.pop(0)
                # adds item to user inventory
                self.inventory.append(item)
                # readds item back to shop list in the exact same spot
                self.shop.insert(0, item)
                # removes gold from player inventory
                self.gold += -50
                # tells user how much gold they have left
                print(f'you have {self.gold} gold left')
            # if they dont have enough gold
            else:
                # tells user they dont have enough gold
                print('insufficient gold')
        # ALL CODE IS SAME
        elif userinp == 'spiked bat':
            if self.gold >= 150:
                item = self.shop.pop(1)
                self.inventory.append(item)
                self.shop.insert(1, item)
                self.gold += -150
                print(f'you have {self.gold} gold left')
            else:
                print('insufficient gold')
        elif userinp == 'shovel':
            if self.gold >= 500:
                item = self.shop.pop(2)
                self.inventory.append(item)
                self.shop.insert(2, item)
                self.gold += -500
                print(f'you have {self.gold} gold left')
            else:
                print('insufficient gold')
        elif userinp == 'halberd':
            if self.gold >= 700:
                item = self.shop.pop(3)
                self.inventory.append(item)
                self.shop.insert(3, item)
                self.gold += -700
                print(f'you have {self.gold} gold left')
            else:
                print('insufficient gold')
        elif userinp == 'sword':
            if self.gold >= 850:
                item = self.shop.pop(4)
                self.inventory.append(item)
                self.shop.insert(4, item)
                self.gold += -850
                print(f'you have {self.gold} gold left')
            else:
                print('insufficient gold')
        elif userinp == 'cutlass':
            if self.gold >= 1200:
                item = self.shop.pop(5)
                self.inventory.append(item)
                self.shop.insert(5, item)
                self.gold += -1200
                print(f'you have {self.gold} gold left')
            else:
                print('insufficient gold')
        elif userinp == 'zweihander':
            if self.gold >= 2500:
                item = self.shop.pop(6)
                self.inventory.append(item)
                self.shop.insert(6, item)
                self.gold += -2500
                print(f'you have {self.gold} gold left')
            else:
                print('insufficient gold')
        elif userinp == 'kopesh':
            if self.gold >= 5000:
                item = self.shop.pop(7)
                self.inventory.append(item)
                self.shop.insert(7, item)
                self.gold += -5000
                print(f'you have {self.gold} gold left')
            else:
                print('insufficient gold')
        elif userinp == 'shotel':
            if self.gold >= 10000:
                item = self.shop.pop(8)
                self.inventory.append(item)
                self.shop.insert(8, item)
                self.gold += -10000
                print(f'you have {self.gold} gold left')
            else:
                print('insufficient gold')
        elif userinp == 'sandwich':
            if self.gold >= 100:
                item = self.shop.pop(9)
                self.inventory.append(item)
                self.shop.insert(9, item)
                self.gold += -100
                print(f'you have {self.gold} gold left')
            else:
                print('insufficient gold')
        elif userinp == 'bread':
            if self.gold >= 60:
                item = self.shop.pop(10)
                self.inventory.append(item)
                self.shop.insert(10, item)
                self.gold += -60
                print(f'you have {self.gold} gold left')
            else:
                print('insufficient gold')
        elif userinp == 'soup':
            if self.gold >= 400:
                item = self.shop.pop(11)
                self.inventory.append(item)
                self.shop.insert(11, item)
                self.gold += -400
                print(f'you have {self.gold} gold left')
            else:
                print('insufficient gold')
        elif userinp == 'burger king combo':
            if self.gold >= 600:
                item = self.shop.pop(12)
                self.inventory.append(item)
                self.shop.insert(12, item)
                self.gold += -600
                print(f'you have {self.gold} gold left')
            else:
                print('insufficient gold')
        elif userinp == 'medkit':
            if self.gold >= 1000:
                item = self.shop.pop(13)
                self.inventory.append(item)
                self.shop.insert(13, item)
                self.gold += -1000
                print(f'you have {self.gold} gold left')
            else:
                print('insufficient gold')
        elif userinp == 'ice cream':
            if self.gold >= 150:
                item = self.shop.pop(14)
                self.inventory.append(item)
                self.shop.insert(14, item)
                self.gold += -150
                print(f'you have {self.gold} gold left')
            else:
                print('insufficient gold')
        elif userinp == 'granola bar':
            if self.gold >= 300:
                item = self.shop.pop(15)
                self.inventory.append(item)
                self.shop.insert(15, item)
                self.gold += -300
                print(f'you have {self.gold} gold left')
            else:
                print('You have nowhere near enough gold!')
        # if user typed anything else
        else:
            print('Comeback when you want something to buy')

    def fight(self, g, k):
        bestweapon = self.most_powerful_weapon()
        current_enemy = g
        # while the player hp and enemy hp is above zero keep fighting
        while self.hp > 0 and current_enemy.hp > 0:
            # give the enemy an action
            enemy_action = randint(1, 2)
            # takes user input to attack
            userinp = input("type a to attack!: ")
            # checks if user typed in a to attack
            if userinp == 'a':
                # attacks the enemy and removes its health from weapon damage
                current_enemy.hp -= bestweapon.damage
                # informs user of what happened
                print(f'>> The {current_enemy} has {current_enemy.hp} HP left')
                # checks if user typed in anything else
            elif userinp == 'heal':
                self.heal()
            else:
                # Tells user they missed
                print('You missed!')
            # if the enemy action is 1 and health is above zero then run this
            if enemy_action == 1 and current_enemy.hp > 0:
                # Damage the player
                self.hp -= current_enemy.damage
                # tell the user of what happened
                print(f'The {current_enemy.name} attacks and deals\
 {current_enemy.damage} Damage!')
                # tell the user how much health they have left
                if self.hp > 0:
                    print(f'you have {self.hp} Hp left')
            # if the enemy action is 2 and health is above zero then run this
            elif enemy_action == 2 and current_enemy.hp > 0:
                # tell user what happened
                print(f'the {current_enemy.name} missed!')
        # if player hp is 0 then stop the game
        if self.hp <= 0:
            # tell user they are dead
            print('DEAD')
            # exit the game
            exit()
        # if user isnt dead
        else:
            print(f'you have defeated a {current_enemy}')
            self.gold += k
            print(f'you obtained {k} gold')
            print(f'you now have {self.gold} gold')

    def finalboss(self):
        bestweapon = self.most_powerful_weapon()
        current_enemy = Ethereal()
        # while the player hp and enemy hp is above zero keep fighting
        while self.hp > 0 and current_enemy.hp > 0:
            # give the enemy an action
            enemy_action = randint(1, 2)
            # takes user input to attack
            userinp = input("type a to attack!: ")
            # checks if user typed in a to attack
            if userinp == 'a':
                # attacks the enemy and removes its health from weapon damage
                current_enemy.hp -= bestweapon.damage
                # informs user of what happened
                print(f'>> The {current_enemy} has {current_enemy.hp} HP left')
                # checks if user typed in anything else
            else:
                # Tells user they missed
                print('You missed!')
            # if the enemy action is 1 and health is above zero then run this
            if enemy_action == 1 and current_enemy.hp > 0:
                # Damage the player
                self.hp -= current_enemy.damage
                # tell the user of what happened
                print(f'The {current_enemy.name} attacks and deals\
 {current_enemy.damage} Damage!')
                # tell the user how much health they have left
                if self.hp > 0:
                    print(f'you have {self.hp} Hp left')
            # if the enemy action is 2 and health is above zero then run this
            elif enemy_action == 2 and current_enemy.hp > 0:
                # tell user what happened
                print(f'the {current_enemy.name} missed!')
        # if player hp is 0 then stop the game
        if self.hp <= 0:
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
            exit()


def all_characters():
    """
    Commands to list out characters and enemies of the game, and provide
    information about them
    """
    while True:
        # Creates a new line
        print('\n')
        # Tells user how to go back to prevous menu
        print('Type q to go back to the previous menu')
        # Asks for the user input to continue
        user = input('Type [friendly characters] or [enemies] to list characters:\
 ')
        # Lowers all user inputs to satisfy if/elif/else statements
        user = user.lower()
        # Checks to see if user typed in friendly characters
        if user == 'friendly characters':
            # Special loop that loops through all friendly characters
            for k, v in characters.items():
                # If name is Xunerophore then special print statement
                if k == "Xunerophore":
                    print(f"The main character is {k} with {v} Starting HP")
                # If name is Shopkeeper then special print statement
                elif k == "Shopkeeper":
                    print(f"The {k} is {v}")
        # Checks to see if user typed in enemies
        elif user == 'enemies':
            # Special loop that lists the enemies in the game
            for k, v in enemies.items():
                print(f"{k} is an enemy with {v['HP']}HP and {v['Attack']} Attack\
 Damage")
        # Checks to see if user typed in q
        elif user == 'q':
            # quits this part of the menu
            break
        # If user typed in anything else
        else:
            # Tells user the input is invalid
            print('invalid input')


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
