# Classes for USSRecon_o

# Imports
import random
import time
import resources.common.functions as fxn


# Document class
class Document:

    # Initialize
    def __init__(self, title, path):
        self.title = title
        self.path = path

    # Read document
    def read(self):

        with open(self.path, "r", encoding="utf-8") as doc:  # Open document
            for line in doc:  # Each line
                for char in line:  # Each character
                    print(char, end="", flush=True)  # Character by character typewriter style
                    time.sleep(0.001)  # Pause between characters
            print()  # New line

    def __str__(self):
        return self.title


# Weapon class
class Weapon:

    # Initialize
    def __init__(self, name, damage):
        self.name = name  # Name of weapon
        self.damage = damage  # Damage amount

    # Print as string
    def __str__(self):
        return self.name


# Gun class
class Gun(Weapon):

    # Initialize
    def __init__(self, name, damage, rateOfFire, magazineSize):
        super().__init__(name, damage)
        self.ammo = magazineSize  # Remaining ammo (starts with full magazine)
        self.rateOfFire = rateOfFire  # Bullets fired per trigger press
        self.magazineSize = magazineSize  # How much the magazine can hold

    # Fire
    def attack(self, opponent):

        if self.ammo > 0:  # Ammo left in magazine

            if not opponent.dodge:  # Opponent isn't dodging
                opponent.health -= self.rateOfFire * self.damage  # Damage per bullet applied to opponent

            else:
                opponent.health -= (self.rateOfFire - 1) * self.damage  # Opponent dodges one bullet
                opponent.dodge = False  # Resetting dodge
                fxn.read_dialogue(f"SE: {opponent.name} dodged one bullet!")
                print()

            # Negative health not allowed
            if opponent.health < 0:
                opponent.health = 0

        else:
            pass

        self.ammo -= self.rateOfFire  # Subtract bullets used from ammo

    # Reload
    def reload(self):
        self.ammo = self.magazineSize


# Nagant class
class Nagant(Gun):

    # Initialize
    def __init__(self):
        super().__init__(name="Nagant M1895", damage=40, rateOfFire=1, magazineSize=7)


# AK47 class
class AK47(Gun):

    # Initialize
    def __init__(self):
        super().__init__(name="AK47", damage=6, rateOfFire=5, magazineSize=40)


# Fedorov class
class Fedorov(Gun):

    # Initialize
    def __init__(self):
        super().__init__(name="Fedorov Avtomat", damage=7, rateOfFire=5, magazineSize=40)


# Colt class
class Colt(Gun):

    # Initialize
    def __init__(self):
        super().__init__(name="Colt 1911", damage=50, rateOfFire=1, magazineSize=8)


# Knife class
class Knife(Weapon):

    # Initialize
    def __init__(self):
        super().__init__(name="Knife", damage=25)

    # Slash
    def attack(self, opponent):
        if opponent.dodge:  # Attack dodged
            opponent.dodge = False  # Resetting dodge
            fxn.read_dialogue(f"SE: {opponent.name} dodged the attack!\n")
            print()
        else:
            opponent.health -= self.damage

            # Negative health not allowed
            if opponent.health < 0:
                opponent.health = 0


# Fists class
class Fists(Weapon):

    # Initialize
    def __init__(self):
        super().__init__(name="Fists", damage=20)

    # Punch
    def attack(self, opponent):
        if opponent.dodge:  # Attack dodged
            opponent.dodge = False  # Reset dodge
            fxn.read_dialogue(f"SE: {opponent.name} dodged the attack!")
            print()
        else:
            opponent.health -= self.damage

            # Negative health not allowed
            if opponent.health < 0:
                opponent.health = 0


# Ammo class
class Ammo:

    # Initialize
    def __init__(self, name, guns, gunType):
        self.guns = guns
        self.name = name
        self.gunType = gunType

    # Print
    def __str__(self):
        return f"{self.name} - reloads {self.gunType} to full"

    # Reload gun
    def use(self, user, choice):

        # Correct ammo selected
        if user.weapon.__class__ in self.guns:
            user.weapon.ammo = user.weapon.magazineSize  # Reloading
            user.inventory.remove(user.inventory[choice - 1])  # Remove item
            fxn.read_dialogue(f"SE: Reloaded {user.weapon} to {user.weapon.ammo}/{user.weapon.magazineSize} rounds.")
            print()

        # Wrong ammo for this weapon
        else:
            fxn.read_dialogue(f"NA: This ammo only works on {self.gunType}!")
            print()


# Pistol ammo class
class PistolAmmo(Ammo):

    # Initialize
    def __init__(self):
        super().__init__(guns=[Colt, Nagant],
                         name="Pistol Ammo",
                         gunType="pistols")


# Rifle ammo class
class RifleAmmo(Ammo):

    # Initialize
    def __init__(self):
        super().__init__(gunType="rifles",
                         name="Rifle Ammo",
                         guns=[AK47, Fedorov])


# PowerUp class
class PowerUp:

    # Initialize
    def __init__(self, name, regen):
        self.name = name
        self.regen = regen

    # Display as string
    def __str__(self):
        return f"{self.name} - restores {self.regen}hp"

    # Use itself
    def use(self, user, choice):
        user.health += self.regen

        # Don't exceed max health
        if user.health > user.maxHealth:
            user.health = user.maxHealth

        user.inventory.remove(user.inventory[choice - 1])  # Remove item

        # Confirmation of heal
        fxn.read_dialogue(f"SE: {user.name} healed to {user.health}/{user.maxHealth} using {self.name}!")
        print()


# Caviar class
class Caviar(PowerUp):

    # Initialize
    def __init__(self):
        super().__init__(name="Caviar", regen=100)


# Vodka class
class Vodka(PowerUp):

    # Initialize
    def __init__(self):
        super().__init__(name="Vodka", regen=50)


# Semechki class
class Semechki(PowerUp):

    # Initialize
    def __init__(self):
        super().__init__(name="Semechki", regen=25)


# Base Character class
class Character:

    # Initialize
    def __init__(self, name, weapon, maxHealth, taunts):
        self.name = name
        self.weapon = weapon
        self.health = maxHealth
        self.maxHealth = maxHealth
        self.inventory = []
        self.dodge = False
        self.taunts = taunts
        self.moves = {}

    def __str__(self):
        return f"Name: {self.name}\nHealth: {self.health}/{self.maxHealth}\nWeapon: {str(self.weapon)}"

    # Pick up item
    def pick_up_item(self, item):
        self.inventory.append(item)

    # Assign random name
    def pick_name(self):
        with open("resources/common/data/names.txt", "r") as names:
            lines = names.read().splitlines()
            self.name += f" ({random.choice(lines)})"

    # Reading dialogue
    def read_dialogue(self, line):
        print(f"{self.name}: ", end="")  # Dialogue tag
        for character in line[4:]:  # Removes signifier dialogue tag
            print(character, end="", flush=True)  # Prints individual character
            time.sleep(0.03)  # Small delay for type writer style
        time.sleep(0.5)  # Processing time

    # Display moves
    def display_moves(self):
        print(f"----------{self.name}'s Moves-----------")
        for index, key in enumerate(self.moves):
            print(f"{index + 1}) {key} - {self.moves[key]}")
        print("\n\n\n")

    # Display health
    def display_health(self):
        return f"{self.name.upper()}: {self.health}/{self.maxHealth}"

    # Taunt
    def taunt(self):
        self.read_dialogue("SE: " + random.choice(self.taunts))  # Picks a random taunt
        print()


# Protagonist class
class Protagonist(Character):

    # Initialize
    def __init__(self, name):
        super().__init__(name,
                         weapon=Colt(),
                         maxHealth=250, taunts=["Take that commie!",
                                                "Where's Marx to save you now?",
                                                "For Uncle Sam!",
                                                "You Russian swine!",
                                                "Don't worry, I'll shoot you all with the same number of bullets; just "
                                                "like a socialist would want!"])
        self.moves = {"Punch": f"{Fists().damage}dmg",
                      "Dodge": "Dodges one bullet or melee attack this turn.",
                      "Use Item": "Choose an item from your inventory to use.",
                      "Attack": f"{self.weapon} does {self.weapon.damage}dmg x {self.weapon.rateOfFire} shots.",
                      "Taunt": "Taunt your opponent."}
        self.name = name
        self.documents = []  # Added inventory for documents

    # Use item
    def use_item(self):

        # Displaying items
        print("Items: ")
        for index, item in enumerate(self.inventory):
            print(f"{index + 1}) {item}")
        print()

        # Making choice
        while True:
            choice = input("Item to use (or type 'skip'): ")

            if choice != "skip":  # Didn't skip choosing an item

                try:
                    choice = int(choice)

                    if 1 <= choice <= len(self.inventory):  # An item was selected
                        self.inventory[choice - 1].use(self, choice)  # Use item
                        break

                    else:
                        fxn.read_dialogue("SE: You didn't pick a valid option, man!")  # Out of range
                        print()

                except ValueError:
                    fxn.read_dialogue(f"SE: You didn't pick a valid option, man!")  # Not integer
                    print()

            else:  # Skipped
                break

    # Switch weapons
    def switch_weapon(self, opponent):

        fxn.read_dialogue(f"NA: Switched {self.weapon} with {opponent.weapon}")
        print()

        self.weapon = opponent.weapon  # Actual switch

        # Resetting move description
        if issubclass(self.weapon.__class__, Gun):  # If gun
            self.moves["Attack"] = f"{self.weapon} does {self.weapon.damage}dmg x {self.weapon.rateOfFire} shots."

        else:  # If not gun
            self.moves["Attack"] = f"{self.weapon} does {self.weapon.damage}dmg"

    # Attack
    def attack(self, opponent):

        while True:

            choice = input("Your move: ")

            try:
                choice = int(choice)

                if 0 < choice <= len(self.moves):

                    if choice == 1:  # Punch
                        Fists().attack(opponent)
                        print()
                        break
                    elif choice == 2:  # Dodge
                        self.dodge = True
                        print()
                        break
                    elif choice == 3:  # Use item

                        if len(self.inventory) > 0:  # Items available
                            self.use_item()
                            print()

                        else:  # Empty inventory
                            fxn.read_dialogue("NA: You don't have any items left!")
                            print()

                    elif choice == 4:  # Use weapon

                        if issubclass(self.weapon.__class__, Gun):
                            if self.weapon.ammo > 0:
                                self.weapon.attack(opponent)
                                fxn.read_dialogue(f"NA: {self.weapon.ammo}/{self.weapon.magazineSize} rounds left.")
                                print()
                                break

                            else:
                                fxn.read_dialogue("NA: Out of ammo! Pick another move!")
                                print()

                        else:
                            self.weapon.attack(opponent)
                            print()
                            break

                    else:  # Taunt
                        self.taunt()
                        print()

                else:
                    fxn.read_dialogue("NA: You weren't hired for your sense of humour; pick an option!")
                    print()

            except ValueError:
                fxn.read_dialogue("NA: Type the number associated with the move you want to use, soldier!")
                print()

    # Read documents
    def read_documents(self):

        # Making choice
        while True:

            # Display documents
            for index, doc in enumerate(self.documents):
                print(f"{index + 1}) {doc.title}")

            # Make choice
            choice = input("Document to read (or type 'skip'): ")

            if choice == 'skip':  # Skip
                fxn.clear_screen()
                break

            else:  # Player chose document
                try:
                    choice = int(choice)

                    if 1 <= choice <= len(self.documents):  # An item was selected
                        print()
                        self.documents[choice - 1].read()
                        input("Press enter to continue.")
                        fxn.clear_screen()

                    else:
                        fxn.read_dialogue("NA: You didn't pick a valid option, man!")  # Out of range
                        print()

                except ValueError:
                    fxn.read_dialogue(f"NA: You didn't pick a valid option, man!")  # Not integer or skip input
                    print()


# NKVD Kingpin class
class NKVD(Character):

    # Initialize
    def __init__(self):
        super().__init__(name="NKVD Kingpin",
                         weapon=Nagant(),
                         maxHealth=130,
                         taunts=["You can't destroy the communist empire!",
                                 "Американская собака!",
                                 "The wave of communism is unstoppable.",
                                 "Where's your precious individuality now?",
                                 "Capitalist scum!"])
        self.moves = {"Punch": f"{Fists().damage}dmg",
                      f"Shoot": f"{self.weapon.name} does {self.weapon.damage}dmg x {self.weapon.rateOfFire} shot",
                      "Dodge": "Dodges one bullet or melee attack this turn."}
        self.pick_name()

    # Attack
    def attack(self, opponent):

        attack = random.choice([True, False, True])  # Pick between dodging and attacking

        if attack:  # Use a weapon to attack

            if self.weapon.ammo > 0:  # Shoot gun
                fxn.read_dialogue(f"SE: {self.name} used {self.weapon}!")
                print()
                self.weapon.attack(opponent)

            else:  # If there's no ammo, use fists
                fxn.read_dialogue(f"SE: {self.name} used their fists!")
                print()
                Fists().attack(opponent)

        else:  # Dodge
            self.dodge = True
            fxn.read_dialogue(f"SE: {self.name} used dodge!")
            print()


# Soldier class
class Soldier(Character):

    # Initialize
    def __init__(self):
        super().__init__(name="Soldier",
                         weapon=AK47(),
                         maxHealth=150,
                         taunts=["Arngh!", "For the Motherland!", "Attackkkkkk!",
                                 "We will defeat you!", "Aghhhhhhhh!"])
        self.moves = {"Punch": f"{Fists().damage}dmg",
                      f"Shoot": f"{self.weapon.name} does {self.weapon.damage}dmg x {self.weapon.rateOfFire} shots"}
        self.pick_name()


# Commander class
class Commander(Character):

    # Initialize
    def __init__(self):
        super().__init__(name="Commander",
                         weapon=Fedorov(),
                         maxHealth=110,
                         taunts=["Arngh!", "For the Motherland!", "I don't need backup!", "Say your last words!"])
        self.moves = {"Punch": f"{Fists().damage}dmg",
                      f"Shoot": f"{self.weapon.name} does {self.weapon.damage}dmg x {self.weapon.rateOfFire} shots"}
        self.pick_name()

    # Attack
    def attack(self, opponent):

        if self.weapon.ammo > 0:  # Shoot gun
            fxn.read_dialogue(f"SE: {self.name} used {self.weapon}!\n")
            self.weapon.attack(opponent)

        else:  # If there's no ammo, use fists
            fxn.read_dialogue(f"SE: {self.name} used their fists!\n")
            Fists().attack(opponent)


# Guard class
class Guard(Character):

    # Initialize
    def __init__(self):
        super().__init__(name="Guard",
                         weapon=AK47(),
                         maxHealth=120,
                         taunts=["Умирай собака!", "Сука настоящая!", "American долбаеб!", "Черт!", "Сука бляттттттт!"])
        self.moves = {"Punch": f"{Fists().damage}dmg",
                      f"Shoot": f"{self.weapon.name} does {self.weapon.damage}dmg x {self.weapon.rateOfFire} shots"}
        self.pick_name()

    # Attack
    def attack(self, opponent):

        if self.weapon.ammo > 0:  # Shoot gun
            fxn.read_dialogue(f"SE: {self.name} used {self.weapon}!\n")
            self.weapon.attack(opponent)

        else:  # If there's no ammo, use fists
            fxn.read_dialogue(f"SE: {self.name} used their fists!\n")
            Fists().attack(opponent)


# Spy class
class Spy(Character):

    # Initialize
    def __init__(self):
        super().__init__(name="Spy",
                         weapon=Knife(),
                         maxHealth=80,
                         taunts=["No one can hear you scream...", "Want to feel my blade, житель запада?",
                                 "Take that, капиталист!", "You and I can relate; we're both шпионы."])
        self.moves = {"Slash": f"{Knife().damage}dmg",
                      "Dodge": "Dodges one bullet or melee attack this turn."}
        self.pick_name()

    # Attack

    def attack(self, opponent):

        attack = random.choice([True, False, True, True])  # Pick between dodging and attacking

        if attack:  # Use a weapon to attack
            fxn.read_dialogue(f"SE: {self.name} used slash!")
            print()
            self.weapon.attack(opponent)

        else:  # Dodge
            self.dodge = True
            fxn.read_dialogue(f"SE: {self.name} used dodge!")
            print()


# Gopnik class
class Gopnik(Character):

    # Initialize
    def __init__(self):
        super().__init__(name="Gopnik",
                         weapon=Fists(),
                         maxHealth=50,
                         taunts=["For ze glorious Modderland!", "Хехе, иди на хуй, американец...",
                                 "Пиздец!", "I don't like vesterners...", "Got any semechki?"])
        self.moves = {"Punch": f"{Fists().damage}dmg"}
        self.pick_name()

    # Attack
    def attack(self, opponent):
        fxn.read_dialogue(f"SE: {self.name} used {self.weapon}!\n")
        self.weapon.attack(opponent)
