# USSRecon
RPG game based on being an American spy in the Soviet Union of 1924. Some events are based on historical facts. You must
infiltrate soviet military and secret police units in order to provide information to the Homeland Intelligence Agency
and stop the spread of communism across Eastern Europe and the rest of the world.

# How to play
Read through the following documentation to gain a better understanding of the game mechanics. When you're ready to
play, run the **loadingScreen.py** file from the console window.


<h2>Levels</h2>
At the end of each level you'll be given the option to read your documents. Your inventory content will progress into 
the next level with you, as well as your weapon and its remaining ammo. You will be restored to full health before each 
level.

Your progress is also saved at the beginning of each new level. If you quit the game in the middle of a level, you will
restart at the beginning of the same level the next time you play.

The game contains bonus levels that will allow you to discover hidden secrets and collect useful items. You can choose
whether you want to complete these levels, as they are optional.


<h2>Battles</h2>
Battles take place between two characters max.

<h3>Order</h3>
The character who is most quick-witted will attack first. This largely depends on the situation, but some characters
are typically more speedy than others. See _**Characters**_ for a comprehensive list of attributes.

<h3>Format</h3>
Moves are displayed before each turn. When the character makes a move, the new health stats are displayed. The screen is
cleared after each move, with the health bars displayed at the top of the screen. The player is required to press enter
to continue after each move to confirm that they've read and understand the move that was played.

<h2>Moves</h2>

<h3>Punch</h3>
Punching has unlimited use. It can be dodged, and all characters possess this move. Characters who use a firearm will
default to this attack when they run out of ammunition.

<h3>Dodge</h3>
This move sets up a character to dodge the next attack. With melee attacks, this completely avoids any damage. With
firearm attacks, this move can only dodge one bullet. This makes it ineffective against guns that have a rate of fire
higher than one shot per turn.

<h3>Use Item</h3>
This move is unique to the player. It allows you to choose an item to use during battle. Power-ups can be used to heal
in the middle of a fight, and ammunition can refill your gun. A player may use as many items as they like during one
turn. This move is incredibly useful and should be taken advantage of.

<h3>Attack</h3>
This move defaults to using the weapon a character has equipped. It will fire a gun, slash with a knife, or punch. For
NPCs, this move will default to punch if their primary weapon runs out of ammo. The player has a separate punch move
(in case they carry a melee weapon), so this move will just display **"out of ammo"** and prompt a new move choice
should they run out of ammo.

<h2>Weapons</h2>
There are three types of weapons: pistols, rifles and melee weapons. Pistols and rifles have their own unique ammo. 
Importantly, although pistols deal more damage per turn, they can be completely dodged because they fire only once per
turn. Rifles deal less damage on average, but are guaranteed to hit the opponent because they fire multiple times.
Melee weapons are usually weaker than guns, but they have unlimited use.

<h3>Fists</h3>
Fists do 20 damage, and they are the default weapon that all characters possess (besides those with knives).

<h3>Knife</h3>
The knife deals 25 damage, which is only slightly better than fists. NPCs with knives will never punch.

<h3>Colt 1911</h3>
This pistol deals the most damage per turn of any weapon (50). The player starts with this weapon. It holds 8 rounds and
has a firing rate of one shot per turn, making it useless against dodge. This weapon cannot be found on an NPC.

<h3>Nagant M1895</h3>
This pistol deals 40 damage per turn. It holds 7 rounds and has a firing rate of one shot per turn, making it useless
against dodge.

<h3>AK47</h3>
This rifle deals 30 damage per turn, with 6 damage per shot and 5 shots per turn. It holds 40 rounds.

<h3>Federov Avtomat</h3>
This rifle deals 35 damage per turn, with 7 damage per shot and 5 shots per turn. It holds 40 rounds.

<h2>Characters</h2>

<h3>NKVD Kingpin</h3>
The NKVD Kingpin has 130hp. Because they're bureaucratic and don't often see the field of battle, they usually attack
second. They have three moves: punch, shoot and dodge. The Kingpin uses a Nagant M1895 as their primary weapon, and
will only use their fists when they run out of ammo. They have a 66% chance of attacking with their primary weapon, and
a 33% chance of dodging.

<h3>Guard</h3>
The Guard has 120hp. They aren't well-trained, and are lazier than other characters. As a result, they usually attack
second. They have two moves: punch and shoot. The Guard uses an AK47 and will only punch if they run out of ammo.

<h3>Soldier</h3>
The Soldier has 150hp. They are a highly trained version of the Guard, which means that they typically attack first. The
Soldier uses an AK47 and has two moves: shoot and punch. They will also only use punch if they deplete their ammo.

<h3>Commander</h3>
The Commander has 110hp. Because they hold a high military position, they usually attack first. They use a Fedorov
Avtomat because it has slightly better stats than the AK47 of lower position characters. The Commander has two moves:
shoot and punch. They will only use punch once they have run out of ammo for their primary weapon.

<h3>Spy</h3>
The Spy has 80hp. Because they are stealthy, and by necessity, quick, they typically attack first. They use a knife. The
Spy has two moves: slash and dodge. They have a 75% chance of slashing, and a 25% chance of dodging.

<h3>Gopnik</h3>
The Gopnik has 50hp. They are slow and intoxicated, and therefore usually attack second. They have only one move: punch.

<h2>Items</h2>

<h3>Ammo</h3>
All ammo completely refills the magazine of the gun it is used on.

**Pistol Ammo:** can only reload pistols

**Rifle Ammo:** can only reload rifles.

<h3>Power-ups</h3>
**Caviar:** Restores 100hp to the user when used.

**Vodka:** Restores 50hp to the user when used.

**Semechki:** Restores 25hp to the user when used.

<h3>Documents</h3>
Documents contain important information for the Intelligence Agency. You may read your documents at the end of each
level. These are used to advance the plot.