# Menu

# Imports
from resources.common.functions import *  # Allows me to access functions without extra syntax
import resources.common.functions as fxn  # Allows me to change the reading speed variable for the WHOLE game

# Impressive title screen
clear_screen()  # Clearing screen

# Title music
play_music(file="resources/common/soundFiles/march.wav")
time.sleep(1.4)

print("""UUUUUUUU     UUUUUUUU   SSSSSSSSSSSSSSS    SSSSSSSSSSSSSSS RRRRRRRRRRRRRRRRR                                                                              
U::::::U     U::::::U SS:::::::::::::::S SS:::::::::::::::SR::::::::::::::::R                                                                             
U::::::U     U::::::US:::::SSSSSS::::::SS:::::SSSSSS::::::SR::::::RRRRRR:::::R                                                                            
UU:::::U     U:::::UUS:::::S     SSSSSSSS:::::S     SSSSSSSRR:::::R     R:::::R                                                                           
 U:::::U     U:::::U S:::::S            S:::::S              R::::R     R:::::R    eeeeeeeeeeee        cccccccccccccccc   ooooooooooo   nnnn  nnnnnnnn    
 U:::::D     D:::::U S:::::S            S:::::S              R::::R     R:::::R  ee::::::::::::ee    cc:::::::::::::::c oo:::::::::::oo n:::nn::::::::nn  
 U:::::D     D:::::U  S::::SSSS          S::::SSSS           R::::RRRRRR:::::R  e::::::eeeee:::::ee c:::::::::::::::::co:::::::::::::::on::::::::::::::nn 
 U:::::D     D:::::U   SS::::::SSSSS      SS::::::SSSSS      R:::::::::::::RR  e::::::e     e:::::ec:::::::cccccc:::::co:::::ooooo:::::onn:::::::::::::::n
 U:::::D     D:::::U     SSS::::::::SS      SSS::::::::SS    R::::RRRRRR:::::R e:::::::eeeee::::::ec::::::c     ccccccco::::o     o::::o  n:::::nnnn:::::n
 U:::::D     D:::::U        SSSSSS::::S        SSSSSS::::S   R::::R     R:::::Re:::::::::::::::::e c:::::c             o::::o     o::::o  n::::n    n::::n
 U:::::D     D:::::U             S:::::S            S:::::S  R::::R     R:::::Re::::::eeeeeeeeeee  c:::::c             o::::o     o::::o  n::::n    n::::n
 U::::::U   U::::::U             S:::::S            S:::::S  R::::R     R:::::Re:::::::e           c::::::c     ccccccco::::o     o::::o  n::::n    n::::n
 U:::::::UUU:::::::U SSSSSSS     S:::::SSSSSSSS     S:::::SRR:::::R     R:::::Re::::::::e          c:::::::cccccc:::::co:::::ooooo:::::o  n::::n    n::::n
  UU:::::::::::::UU  S::::::SSSSSS:::::SS::::::SSSSSS:::::SR::::::R     R:::::R e::::::::eeeeeeee   c:::::::::::::::::co:::::::::::::::o  n::::n    n::::n
    UU:::::::::UU    S:::::::::::::::SS S:::::::::::::::SS R::::::R     R:::::R  ee:::::::::::::e    cc:::::::::::::::c oo:::::::::::oo   n::::n    n::::n
      UUUUUUUUU       SSSSSSSSSSSSSSS    SSSSSSSSSSSSSSS   RRRRRRRR     RRRRRRR    eeeeeeeeeeeeee      cccccccccccccccc   ooooooooooo     nnnnnn    nnnnnn""")

time.sleep(2.3)  # Pause before author

print("""
 ______        __         __     __   __     ______     __  __     __     __   __     __        ______     ______     __    __     ______    
/\  __ \      /\ \       /\ \   /\ "-.\ \   /\  ___\   /\ \/\ \   /\ \   /\ "-.\ \   /\ \      /\  ___\   /\  __ \   /\ "-./  \   /\  ___\   
\ \  __ \     \ \ \____  \ \ \  \ \ \-.  \  \ \ \__ \  \ \ \_\ \  \ \ \  \ \ \-.  \  \ \ \     \ \ \__ \  \ \  __ \  \ \ \-./\ \  \ \  __\   
 \ \_\ \_\     \ \_____\  \ \_\  \ \_\\\\"\_\  \ \_____\  \ \_____\  \ \_\  \ \_\\\\"\_\  \ \_\     \ \_____\  \ \_\ \_\  \ \_\ \ \_\  \ \_____\ 
  \/_/\/_/      \/_____/   \/_/   \/_/ \/_/   \/_____/   \/_____/   \/_/   \/_/ \/_/   \/_/      \/_____/   \/_/\/_/   \/_/  \/_/   \/_____/
  """)

time.sleep(5.5)  # Pause before loading save

print("\n\n\n\n\n")  # Some line gaps

# Check for save file
while True:
    read_dialogue("TS: Do you have a save file? ")
    saved = input("Enter (y/n): ")

    if saved.lower() == "y" or saved.lower() == "yes":

        play_music()  # End music
        clear_screen()
        read_save(restart=True)  # Pass a protagonist with a placeholder name
        break

    elif saved.lower() == "n" or saved.lower() == "no":

        play_music()  # End music
        clear_screen()
        # Ignore ugly error message
        try:
            importlib.import_module("intro.py")
            break
        except ModuleNotFoundError:
            break

    elif saved.lower() == "debug":  # Secret debugging option to change text speeds

        clear_screen()

        while True:
            char = input("Pause after character: ")
            line = input("Pause after line: ")

            try:
                char = float(char)
                line = float(line)
                fxn.charPause = char
                fxn.linePause = line
                break

            except ValueError:
                read_dialogue("DE: You didn't give a usable value for one of the options.")
                print()

    else:
        read_dialogue("NA: Yes or no, soldier.")
