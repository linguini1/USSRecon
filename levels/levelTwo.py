# Level Two - Smolensk Base

# Imports
from resources.common.functions import *
from resources.common.classes import *

# Read in previous protagonist data
player = read_save()

# Save that player has reached the train ride level
save(player, __file__)

# Setting
play_music(file="resources/common/soundFiles/car.wav")  # Driving noises
text_reader("resources/levelTwo/setting.txt", narrator=True)  # Storyline

play_music(file="resources/common/soundFiles/plain.wav")  # Outside noises
text_reader("resources/levelTwo/altercation.txt", narrator=True)  # Continue story line

# Clear setting
enter_cont()

# Battle against guard
guard = Guard()  # Initialize guard
start_battle(player, guard)  # Fight
play_music(file="resources/common/soundFiles/plain.wav")  # Starting outside noises
weapon_switch(player, guard)  # Switch weapons

# Victory
for item in [RifleAmmo(), Caviar(), Vodka(), Vodka(), Semechki(), Semechki()]:
    player.inventory.append(item)  # Collecting loot

text_reader("resources/levelTwo/gate.txt", narrator=True)  # Victory and moving to the base's entrance
play_music(file="resources/common/soundFiles/silence.wav")  # Starting noises for inside the base

# Inside the base
soldierOne = Soldier()  # Initialize first soldier
soldierTwo = Soldier()  # Initialize second soldier
text_reader("resources/levelTwo/base.txt", tags={"S1:": soldierOne,
                                                 "S2:": soldierTwo})
# Clear story
enter_cont()

# Battle against first soldier
start_battle(player, soldierOne, first=True)  # Soldier moves first
play_music(file="resources/common/soundFiles/silence.wav")  # Resume background noise
weapon_switch(player, soldierOne)  # Weapon switch

# Battle against second soldier
start_battle(player, soldierTwo, first=True)  # Soldier moves first
play_music(file="resources/common/soundFiles/silence.wav")  # Resume background noise
weapon_switch(player, soldierTwo)  # Weapon switch

# Victory
text_reader("resources/levelTwo/bridge.txt", narrator=True)  # Narration
player.inventory.append(Semechki())  # Semechki
player.inventory.append(Semechki())  # Semechki x2

# Clear story
enter_cont()

# Regen break
regen_break(player)

# Assassinate a commander
if issubclass(player.weapon.__class__, Gun):  # Player weapon is a gun

    if player.weapon.ammo > 1:  # Player's gun has ammo
        text_reader("resources/levelTwo/gun.txt", narrator=True)  # Read gun altercation
        player.weapon.ammo -= player.weapon.rateOfFire  # Unloads one set of bullets

    else:  # Player's gun has no ammo, use fists
        text_reader("resources/levelTwo/fists.txt", narrator=True)

    # Clear story
    enter_cont()

else:  # Player weapon is a knife
    text_reader("resources/levelTwo/knife.txt", narrator=True)

    # Clear story
    enter_cont()

# Fight with second commander
commander = Commander()  # Initialize commander
plans = Document("Stolpce Training Protocols", "resources/documents/stolpceProtocols.txt")  # Document - plans
start_battle(player, commander, first=True)  # Battle
play_music(file="resources/common/soundFiles/silence.wav")  # Start background noise
weapon_switch(player, commander)  # Switch weapons with dead commander

# Victory
text_reader("resources/levelTwo/bridgeVic.txt", narrator=True)  # Read story
player.documents.append(plans)  # Acquire document
play_music(file="resources/common/soundFiles/plain.wav")  # Play outside noises

text_reader("resources/levelTwo/escape.txt", narrator=True)  # Continue story
play_music(file="resources/common/soundFiles/car.wav")  # Play car noises

text_reader("resources/levelTwo/driveHome.txt", narrator=True)  # Continue story
enter_cont()  # Clear story and continue

# Read documents before next level
read_document(player)

# Show end screen
importlib.import_module("endScreen.py")
