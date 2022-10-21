# Jackson Blackman
# 2022-10-20
# A text based game

# Imports
from time import sleep
import os
import sys
import random

# Functions
## Slowprint function simulates typing
def slowprint(str):
  for char in str:
    sys.stdout.write(char)
    sys.stdout.flush()
    typing_speed = random.uniform(.001,.15)
    sleep(typing_speed)

# Intro
slowprint('The year is 2054 and the true first man-operated mission to mars is taking place. \n')
skip = str(input('\n PRESS ENTER TO CONTINUE \n'))
os.system('cls')

## Name collection
slowprint('Only some of the most fit personnel were chosen in order to ensure survival. Your name is: \n')
first_name = str(input('First name: '))
last_name = str(input('Last name: '))
skip = str(input('\n PRESS ENTER TO CONTINUE \n'))
os.system('cls')

slowprint('You were chosen for your clean record and excilent military service \n')
skip = str(input('\n PRESS ENTER TO CONTINUE \n'))
os.system('cls')

slowprint('Although this mission was well engineered you could have not expect everything')
print()
skip = str(input('\n PRESS ENTER TO CONTINUE \n'))
os.system('cls')

# Spaceship animation
print(r'''
 /\/\/\                            /  \
| \  / |                         /      \
|  \/  |                       /          \
|  /\  |----------------------|     /\     |
| /  \ |                      |    /  \    |
|/    \|                      |   /    \   |
|\    /|                      |  | (  ) |  |
| \  / |                      |  | (  ) |  |
|  \/  |                 /\   |  |      |  |   /\
|  /\  |                /  \  |  |      |  |  /  \
| /  \ |               |----| |  |      |  | |----|
|/    \|---------------|    | | /|   .  |\ | |    |
|\    /|               |    | /  |   .  |  \ |    |
| \  / |               |    /    |   .  |    \    |
|  \/  |               |  /      |   .  |      \  |
|  /\  |---------------|/        |   .  |        \|
| /  \ |              /   NASA   |   .  |  NASA    \
|/    \|              (          |      |           )
|/\/\/\|               |    | |--|      |--| |    |
------------------------/  \-----/  \/  \-----/  \--------
                        \\//     \\//\\//     \\//
                         \/       \/  \/       \/
                         ''')
sleep(.5)
print(r'''                        \\//     \\//\\//     \\//
                         \/       \/  \/       \/''')
print()
sleep(.5)
print(r'''                        \\//     \\//\\//     \\//
                         \/       \/  \/       \/''')
print()
sleep(.5)
print(r'''                        \\//     \\//\\//     \\//
                         \/       \/  \/       \/''')
print()
sleep(.5)
print(r'''                        \\//     \\//\\//     \\//
                         \/       \/  \/       \/''')
print()
sleep(.5)
print(r'''                        \\//     \\//\\//     \\//
                         \/       \/  \/       \/''')
skip = str(input('\n PRESS ENTER TO CONTINUE \n'))
os.system('cls')

# Outer space animation
print(r'''
                   .'.
                   |o|
                  .'o'.
                  |.-.|
                  '   '
                   ( )
                    )
                   ( )

               ____
          .-'""p 8o""`-.
       .-'8888P'Y.`Y[ ' `-.
     ,']88888b.J8oo_      '`.
   ,' ,88888888888["        Y`.
  /   8888888888P            Y8\
 /    Y8888888P'             ]88\
:     `Y88'   P              `888:
:       Y8.oP '- >            Y88:
|          `Yb  __             `'|
:            `'d8888bo.          :
:             d88888888ooo.      ;
 \            Y88888888888P     /
  \            `Y88888888P     /
   `.            d88888P'    ,'
     `.          888PP'    ,'
       `-.      d8P'    ,-'   
          `-.,,_'__,,.-'
          ''')
