# Level One - NKVD Hideout

# Imports
from resources.common.functions import *
from resources.common.classes import *

# Read in previous protagonist data
player = read_save()

# Save that player has reached level 1
save(player, __file__)

# Setting
play_music(file="resources/common/soundFiles/street.wav")  # Street ambiance plays
text_reader("resources/levelOne/setting.txt")

# Altercation
gopnik = Gopnik()  # Initializing gopnik character
gopnik.inventory.append(Semechki())  # Giving gopnik Semechki

# Dialogue
text_reader("resources/levelOne/gopnik.txt", tags={"PR:": player, "GP:": gopnik})

# Give user time to read story
input("Press enter to continue.")
clear_screen()
# Battle
start_battle(player, gopnik)

# Victory + entering hideout
play_music(file="resources/common/soundFiles/street.wav")  # Street ambiance returns
text_reader("resources/levelOne/gopnikVictory.txt", narrator=True)

player.inventory.append(Semechki())  # Player gets semechki

# Guard conversation
guardOne = Guard()  # First guard
guardTwo = Guard()  # Second guard
guardTwo.inventory.append(Vodka())  # Giving second guard his vodka

# Dialogue
play_music(file="resources/common/soundFiles/silence.wav")  # Play empty sound for stairwell
text_reader("resources/levelOne/guards.txt", tags={"G1:": guardOne,
                                                   "G2:": guardTwo,
                                                   "PR:": player})
input("Press enter to continue.")  # Giving user time to read dialogue
clear_screen()

# Battle against first guard
start_battle(player, guardOne)
weapon_switch(player, guardOne)

play_music(file="resources/common/soundFiles/silence.wav")  # Play empty sound for stairwell
# Battle against second guard
read_dialogue("NA: The first guard is on the ground, dead. The other guard, stunned and intoxicated takes a "
              "swing at you.")
print("\n")
start_battle(player, guardTwo)
weapon_switch(player, guardTwo)

# Victory
play_music(file="resources/common/soundFiles/silence.wav")  # Play empty sound for stairwell
player.inventory.append(Vodka())  # Vodka
player.inventory.append(Vodka())  # Vodka x2
player.inventory.append(RifleAmmo())  # Rifle ammunition
# Script
text_reader("resources/levelOne/guardVictory.txt", narrator=True)
input("Press enter to continue.")  # Clear narration
clear_screen()
regen_break(player)  # Offer player opportunity to use an item before final battle

# Infiltrating document room
docGuard = Guard()  # Document room guard
commander = Commander()  # Commander
boss = NKVD()  # NKVD leader
boss.inventory.append(Caviar())  # NKVD leader gets caviar
plans = Document("Stolpce Plans", "resources/common/documents/stolpce.txt")

# Dialogue
text_reader("resources/levelOne/docRoom.txt", tags={"NK:": boss,
                                                    "GA:": docGuard,
                                                    "CO:": commander,
                                                    "PR:": player})
input("Press enter to continue.")
clear_screen()

# Battle with guard
start_battle(player, docGuard)
weapon_switch(player, docGuard)
play_music(file="resources/common/soundFiles/silence.wav")  # Play empty sound for stairwell

# Battle with commander
read_dialogue("NA: The commander has escaped their chair and runs out you, gun pointed at your chest.")
print("\n")
start_battle(player, commander, first=True)
weapon_switch(player, commander)
play_music(file="resources/common/soundFiles/silence.wav")  # Play empty sound for stairwell

# Battle with NKVD leader
read_dialogue("NA: The NKVD leader looks stunned, yells something unintelligible and points their gun at your head.")
print("\n")
start_battle(player, boss)
weapon_switch(player, boss)
play_music(file="resources/common/soundFiles/silence.wav")  # Play empty sound for stairwell

# Victory
player.inventory.append(RifleAmmo())  # Get rifle ammo from guard
player.inventory.append(PistolAmmo())  # Get pistol ammo from NKVD officer
player.inventory.append(Caviar())  # Get caviar from NKVD officer
player.documents.append(plans)
text_reader("resources/levelOne/docVictory.txt", narrator=True)
play_music(file="resources/common/soundFiles/street.wav")  # Play street sound for exiting building
input("Press enter to continue.")
clear_screen()

# Read documents before continuing
read_document(player)
play_music()  # Ending sound before next level

# Save
save(player, __file__)

# Trigger level 2
importlib.import_module("bonusTrain.py")
