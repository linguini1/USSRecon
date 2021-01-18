# Level One - NKVD Hideout

# Imports
from resources.common.functions import *
from resources.common.classes import *

# Read in previous protagonist data
player = read_save()

# Save that player has reached level 1
save(player, __file__)

# Setting
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
text_reader("resources/levelOne/gopnikVictory.txt", narrator=True)

player.inventory.append(Semechki())  # Player gets semechki

# Guard conversation
guardOne = Guard()  # First guard
guardTwo = Guard()  # Second guard
guardTwo.inventory.append(Vodka())  # Giving second guard his vodka

# Dialogue
text_reader("resources/levelOne/guards.txt", tags={"G1:": guardOne,
                                                   "G2:": guardTwo,
                                                   "PR:": player})
input("Press enter to continue.")  # Giving user time to read dialogue
clear_screen()

# Battle against first guard
start_battle(player, guardOne)
weapon_switch(player, guardOne)

# Battle against second guard
read_dialogue("NA: The first guard is on the ground, unconscious. The other guard, stunned and intoxicated takes a "
              "swing at you.")
print("\n")
start_battle(player, guardTwo)
weapon_switch(player, guardTwo)

# Victory
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

# Battle with commander
read_dialogue("NA: The commander has escaped their chair and runs out you, gun pointed at your chest.")
print("\n")
start_battle(player, commander, first=True)
weapon_switch(player, commander)

# Battle with NKVD leader
read_dialogue("NA: The NKVD leader looks stunned, yells something unintelligible and points their gun at your head.")
print("\n")
start_battle(player, boss)
weapon_switch(player, boss)

# Victory
player.inventory.append(RifleAmmo())  # Get rifle ammo from guard
player.inventory.append(PistolAmmo())  # Get pistol ammo from NKVD officer
player.inventory.append(Caviar())  # Get caviar from NKVD officer
player.documents.append(plans)
text_reader("resources/levelOne/docVictory.txt", narrator=True)
input("Press enter to continue.")
clear_screen()

# Read documents before continuing
read_document(player)

# Save
save(player, __file__)

# Trigger level 2
importlib.import_module("bonusTrain.py")
