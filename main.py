# CS 30
# Period 4
# Date : 09/27/2019
# Krutik Rana
# Program description : Creating Numerical Lists

# Creates a list of Bait
Bait = ["Earthworm", "Crickets", "Grasshoppers"]
# Creates a list of Weapons
Weapon = ["Dagger", "Sword", "Great_Sword", "Diamond_Sword", "Spear", "Stick"]

# Prints out a title for numerical list of Bait
print("\nAvailable Bait:")
# Creates a loop that prints out each Bait in numerical fashion
for Number in range(len(Bait)):
    print(str(Number + 1) + ". " + Bait[Number])

# Prints out a title for numerical list of Weapons
print("\nAvailable Weapons:")
# Creates a loop that prints out each Weapon in numerical fashion
for Number in range(len(Weapon)):
    print(str(Number + 1) + ". " + Weapon[Number])
