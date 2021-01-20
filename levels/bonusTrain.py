# Bonus Level - Train Ride

# Imports
from resources.common.functions import *
from resources.common.classes import *

# Read in previous protagonist data
player = read_save()

# Save that player has reached the train ride level
save(player, __file__)

# Setting
play_music(file="resources/common/soundFiles/train.wav")  # Starting train sounds
text_reader("resources/bonusTrain/setting.txt", narrator=True)

# Complete bonus level or ignore it
while True:

    choice = input("Do you want to complete this bonus level? Enter (y/n): ")

    if choice.lower() == "yes" or choice.lower() == "y":
        clear_screen()
        break

    elif choice.lower() == "no" or choice.lower() == "n":
        read_dialogue("NA: Suit yourself soldier. I hope you can live with this on your conscience.")
        print()

        # Continue to level 2
        enter_cont()

        # Importing next level and ignoring error message
        try:
            importlib.import_module("levelTwo.py")
        except ModuleNotFoundError:
            pass

    else:
        read_dialogue("NA: Yes or no, soldier.")
        print()

# Confrontation
spy = Spy()  # Spy character
spy.inventory.append(Caviar())  # Carries caviar
spy.inventory.append(PistolAmmo())  # Pistol ammo
spy.inventory.append(PistolAmmo())  # Pistol ammo x2

# Dialogue
text_reader("resources/bonusTrain/lure.txt", tags={"PR:": player,
                                                   "SP:": spy})

# Clear story
enter_cont()

spy.health -= Fists().damage  # Initial punch

# Battle, spy moves first
start_battle(player, spy, first=True)
play_music(file="resources/common/soundFiles/train.wav")  # Starting train sounds after battle again
weapon_switch(player, spy)  # Switch weapons

# Victory
player.inventory.append(Caviar())  # Carries caviar
player.inventory.append(PistolAmmo())  # Pistol ammo
player.inventory.append(PistolAmmo())  # Pistol ammo x2

# Script
text_reader("resources/bonusTrain/victory.txt", narrator=True)
enter_cont()

# Read documents
read_document(player)
play_music()  # Ending train sounds before next level

# Save
save(player, __file__)

# Next level
importlib.import_module("levelTwo.py")
