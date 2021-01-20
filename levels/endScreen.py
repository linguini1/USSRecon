# End Screen

# Imports
from resources.common.functions import *  # Allows me to access functions without extra syntax

# Impressive title
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

time.sleep(2.3)  # Pause before "The End"

# Line breaks
print("\n\n")

# The end
print(""" ______   __  __     ______        ______     __   __     _____    
/\__  _\ /\ \_\ \   /\  ___\      /\  ___\   /\ "-.\ \   /\  __-.  
\/_/\ \/ \ \  __ \  \ \  __\      \ \  __\   \ \ \-.  \  \ \ \/\ \ 
   \ \_\  \ \_\ \_\  \ \_____\     \ \_____\  \ \_\\\\"\_\  \ \____- 
    \/_/   \/_/\/_/   \/_____/      \/_____/   \/_/ \/_/   \/____/ """)

time.sleep(5.5)  # Pause before credits

# Line breaks
print("\n")

# Credits
read_dialogue("ES: Developed by Matteo Golin")
print()
read_dialogue("ES: Programmed by Matteo Golin")
print()
read_dialogue("ES: Written by Matteo Golin")
print()
read_dialogue("ES: Music by Red Army Choir, The XS Project, and Vladimir Troshin")
print()

# Line breaks
print("\n")

# Press enter to continue
input("Press enter to close the program.")
clear_screen()
quit()
