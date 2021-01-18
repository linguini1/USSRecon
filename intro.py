# Introduction scene

# Imports
from resources.common.functions import *
from resources.common.classes import *

# Introduction
play_music(file="resources/common/soundFiles/moscowNights.wav")  # Play intro music
text_reader("resources/intro/setting.txt", narrator=True)

# Mission Brief
text_reader("resources/intro/missionBrief.txt", narrator=True)
print()

# Getting name
playerName = input("What's your name, soldier? Enter: ")

# Setting up player
player = Protagonist(playerName)
player.inventory.append(Caviar())

# Mission acceptance
while True:
    accepted = input("Do you accept this mission? Enter (y/n): ")

    if accepted.lower() == "y" or accepted.lower() == "yes":  # Responded yes
        text_reader("resources/intro/missionAccepted.txt", narrator=True)
        accepted = True
        break

    elif accepted.lower() == "n" or accepted.lower() == "no":  # Responded no
        text_reader("resources/intro/missionDeclined.txt", narrator=True)
        accepted = False
        break

    else:  # Invalid response
        read_dialogue("NA: It's a yes or no question, soldier.\n")

# Starting next level
if accepted:

    input("Press enter to continue.")

    # Save information
    save(player, __file__)

    # Trigger level one
    clear_screen()  # Clear screen
    importlib.import_module("levelOne.py")  # Open first level
