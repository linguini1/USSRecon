# Important functions for USSRecon_o

# Imports
import importlib
import time
from os import system, name
import resources.common.classes as cls

# Weapons list
weapons = {"Colt 1911": cls.Colt(),
           "AK47": cls.AK47(),
           "Fedorov Avtomat": cls.Fedorov(),
           "Nagant M1895": cls.Nagant(),
           "Knife": cls.Knife()}

# Items
items = {"Caviar": cls.Caviar(),
         "Vodka": cls.Vodka(),
         "Semechki": cls.Semechki(),
         "Rifle Ammo": cls.RifleAmmo(),
         "Pistol Ammo": cls.PistolAmmo()}


# Function to read non-character dialogue
def read_dialogue(line):
    for character in line[4:]:  # Remove signifier dialogue tag
        print(character, end="", flush=True)  # Print characters individually
        time.sleep(0.0003)  # Give pause before next character
    time.sleep(0.0001)  # One second processing time


# Save progress
def save(protagonist, level):
    with open("resources/common/saveFile.txt", "w") as file:

        file.write(level.split("/")[-1] + "\n")  # Level last saved

        file.write(protagonist.name + "\n")  # user name
        file.write(protagonist.weapon.name + "\n")  # Weapon type
        file.write(str(protagonist.weapon.ammo) + "\n")  # How much ammo is left

        # Writing documents
        for doc in protagonist.documents:
            file.write(doc.title + " | " + doc.path + "\n")

        file.write("ITEMS\n")  # Items header

        # Writing inventory
        for item in protagonist.inventory:
            file.write(item.name + "\n")


# Read save file
def read_save(restart=False):

    protagonist = cls.Protagonist("placeholder")  # Creating empty protag with name placeholder

    with open("resources/common/saveFile.txt", "r") as file:

        data = file.readlines()
        data = [info.replace("\n", "") for info in data]

        level = data[0].split("\\")[-1]  # Which level you're on

        protagonist.name = data[1]  # Setting name
        protagonist.weapon = weapons[data[2]]  # Setting weapon
        protagonist.weapon.ammo = int(data[3])  # Setting weapon ammo

        itemsFound = False  # Not yet found ITEMS header

        # Writing inventory
        for line in data[4:]:

            if "ITEMS" in line:  # Search for items header
                itemsFound = True

            if not itemsFound:  # Not yet found ITEMS header
                title, path = line.split(" | ")
                protagonist.documents.append(cls.Document(title, path))  # Writing doc title and path

            elif itemsFound and "ITEMS" not in line:  # Found ITEMS header
                protagonist.inventory.append(items[line])

        # Resetting move description in case weapon was switched
        if issubclass(protagonist.weapon.__class__, cls.Gun):  # If gun
            protagonist.moves["Attack"] = f"{protagonist.weapon} does {protagonist.weapon.damage}dmg " \
                                          f"x {protagonist.weapon.rateOfFire} shots."

        else:  # If not gun
            protagonist.moves["Attack"] = f"{protagonist.weapon} does {protagonist.weapon.damage}dmg"

    if restart:  # The user is starting from a previously achieved level
        # Opening level (and ignoring ugly error message when level terminates)
        try:
            importlib.import_module(level)
        except ModuleNotFoundError:
            pass

    else:  # The program is recreating the protagonist before the level commences
        return protagonist


# Clear screen
def clear_screen():

    # Windows
    if name == "nt":
        _ = system("cls")

    # Linux & Mac
    else:
        _ = system("clear")


# Display health
def health_display(player, opponent):

    # Health bar
    for _ in range(100):
        print(" ", end="")
    print("-------Health-------", end="")
    for _ in range(100):
        print(" ", end="")

    print()  # New line
    gapLength = round((220 - len(opponent.display_health() + player.display_health())) / 2)  # Dynamic gap length

    # Health of both characters
    for _ in range(gapLength):
        print(" ", end="")
    print(f"{opponent.display_health()} | {player.display_health()}", end="")
    for _ in range(gapLength):
        print(" ", end="")

    print("\n\n")  # New lines


# Battle
def start_battle(player, opponent, first=False):

    # Opponent starts first
    if first:
        P1 = opponent
        P2 = player

    # Player starts first
    else:
        P1 = player
        P2 = opponent

    while P1.health > 0:

        # Move display
        if not first:

            # Display second player moves
            opponent.display_moves()

            # Display first player choices
            player.display_moves()

        if first:

            # Display second player moves
            opponent.display_moves()

            # Display first player choices
            player.display_moves()

        # Player one turn
        P1.attack(P2)  # Attack

        # Continue
        input("Press enter to continue.")
        clear_screen()

        # Health
        health_display(player, opponent)

        if not P2.health > 0:
            break

        # Move display
        if not first:
            # Display second player moves
            opponent.display_moves()

            # Display first player choices
            player.display_moves()

        if first:
            # Display second player moves
            opponent.display_moves()

            # Display first player choices
            player.display_moves()

        # Player two turn turn
        P2.attack(P1)  # Attack

        # Continue
        input("Press enter to continue.")
        clear_screen()

        # Health
        health_display(player, opponent)

    if opponent.health == 0:
        print(""" 
                  ::: === :::====  :::  ===      :::  ===  === :::====  :::= === ===
                  ::: === :::  === :::  ===      :::  ===  === :::  === :::===== ===
                   =====  ===  === ===  ===      ===  ===  === ===  === ======== ===
                    ===   ===  === ===  ===       ===========  ===  === === ====    
                    ===    ======   ======         ==== ====    ======  ===  === ===
                    
                    
              """)
        input("Press enter to continue.")  # Continue
        clear_screen()

    elif player.health == 0:
        print("""                                                  
              ####  ###  #   #     #####  ###   #### #####  #  
             #   # #   #  # #       #  # #   # #     #      #  
              #### #   #   #        #  # #   # #     ####   #  
              #  # #   #  #         #  # #   # #     #         
             #   #  ###  #         #   #  ###   #### #####  #  
             
             
             """)
        print("(You Lose!)")
        quit()


# Weapon switch
def weapon_switch(P1, P2):

    for character in [P1, P2]:

        if issubclass(character.weapon.__class__, cls.Gun):
            print(f"----------{character.name}'s weapon stats----------\n"
                  f"Weapon: {character.weapon}\n"
                  f"Ammo: {character.weapon.ammo}/{character.weapon.magazineSize}\n"
                  f"Shots per turn: {character.weapon.rateOfFire}\n"
                  f"Damage: {character.weapon.damage}\n")

        else:
            print(f"----------{character.name}'s weapon stats----------\n"
                  f"Weapon: {character.weapon}\n"
                  f"Damage: {character.weapon.damage}\n")

    switch = input("Do you want to switch weapons with your victim? Enter (y/n): ")

    if switch.lower() == "yes" or switch.lower() == "y":
        P1.switch_weapon(P2)
        input("Press enter to continue.")
        clear_screen()

    elif switch.lower() == "no" or switch.lower() == "n":
        print(f"Held on to {P1.weapon}.")
        input("Press enter to continue.")
        clear_screen()

    else:
        print("Yes or no, soldier?")


# Read text
def text_reader(fileLocation, tags=None, narrator=False):

    with open(fileLocation, "r", encoding="utf-8") as script:

        for line in script:  # Iterating each line

            if narrator or "NA:" in line:  # Only the narrator reads this file
                read_dialogue(line)

            else:
                for charTag in tags:  # Checking for which character reads the line

                    if charTag in line:  # Make the associated character read the line
                        tags[charTag].read_dialogue(line)

        print()  # Final line break


# Regen break
def regen_break(player):

    read_dialogue(f"NA: Your current health is {player.health}/{player.maxHealth}.")  # Display health
    print()  # New line

    if issubclass(player.weapon.__class__, cls.Gun):  # If weapon is gun, display its ammo
        read_dialogue(f"NA: Your {player.weapon} has {player.weapon.ammo}/{player.weapon.magazineSize} rounds left.")
        print()  # New line

    while True:

        choice = input("Would you like to use an item before you continue? Enter(y/n): ")  # Use item?

        if choice.lower() == "yes" or choice.lower() == "y":  # Use an item
            player.use_item()

        elif choice.lower() == "no" or choice.lower() == "n":  # Skip this regen break
            read_dialogue("NA: Whatever you say soldier.")
            print()
            input("Press enter to continue.")
            clear_screen()
            break

        else:  # Invalid input
            read_dialogue("NA: Yes or no, soldier.")

        input("Press enter to continue.")  # Clear this screen
        clear_screen()


# Read documents
def read_document(player):

    while True:
        choice = input("Would you like to read your documents before the next level? Enter (y/n): ")

        if choice.lower() == "yes" or choice.lower() == "y":  # Yes
            player.read_documents()
            break

        elif choice.lower() == "no" or choice.lower() == "n":  # No
            read_dialogue("NA: Suit yourself, soldier.")
            break

        else:  # Invalid input
            read_dialogue("NA: Yes or no, soldier.")
