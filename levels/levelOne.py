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
enter_cont()  # Clear story

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
enter_cont()  # Clearing story

# Battle against first guard
start_battle(player, guardOne)
play_music(file="resources/common/soundFiles/silence.wav")  # Play empty sound for stairwell
weapon_switch(player, guardOne)  # Weapon switch

# Battle against second guard
read_dialogue("NA: The first guard is on the ground, dead. The other guard, stunned and intoxicated takes a "
              "swing at you.")
print("\n")
start_battle(player, guardTwo)
play_music(file="resources/common/soundFiles/silence.wav")  # Play empty sound for stairwell
weapon_switch(player, guardTwo)  # Weapon switch

# Victory
player.inventory.append(Vodka())  # Vodka
player.inventory.append(Vodka())  # Vodka x2
player.inventory.append(RifleAmmo())  # Rifle ammunition
# Script
text_reader("resources/levelOne/guardVictory.txt", narrator=True)
enter_cont()  # Clearing story
regen_break(player)  # Offer player opportunity to use an item before final battle

# Infiltrating document room
docGuard = Guard()  # Document room guard
commander = Commander()  # Commander
boss = NKVD()  # NKVD leader
boss.inventory.append(Caviar())  # NKVD leader gets caviar
plans = Document("Stolpce Plans", "resources/documents/stolpce.txt")

# Dialogue
text_reader("resources/levelOne/docRoom.txt", tags={"NK:": boss,
                                                    "GA:": docGuard,
                                                    "CO:": commander,
                                                    "PR:": player})
enter_cont()  # Clearing story

# Battle with guard
start_battle(player, docGuard)
play_music(file="resources/common/soundFiles/silence.wav")  # Play empty sound for stairwell
weapon_switch(player, docGuard)  # Weapons switch

# Battle with commander
read_dialogue("NA: The commander has escaped their chair and runs at you, gun pointed at your chest.")
print("\n")
start_battle(player, commander, first=True)
play_music(file="resources/common/soundFiles/silence.wav")  # Play empty sound for stairwell
weapon_switch(player, commander)  # Weapon switch

# Battle with NKVD leader
read_dialogue("NA: The NKVD leader looks stunned, yells something unintelligible and points their gun at your head.")
print("\n")
start_battle(player, boss)
play_music(file="resources/common/soundFiles/silence.wav")  # Play empty sound for stairwell
weapon_switch(player, boss)  # Weapon switch

# Victory
player.inventory.append(RifleAmmo())  # Get rifle ammo from guard
player.inventory.append(PistolAmmo())  # Get pistol ammo from NKVD officer
player.inventory.append(Caviar())  # Get caviar from NKVD officer
player.documents.append(plans)

text_reader("resources/levelOne/docVictory.txt", narrator=True)  # Storyline
play_music(file="resources/common/soundFiles/street.wav")  # Play street sound for exiting building
enter_cont()  # Clearing story

# Read documents before continuing
read_document(player)
play_music()  # Ending sound before next level

# Save
save(player, __file__)

# Trigger level 2
importlib.import_module("bonusTrain.py")
