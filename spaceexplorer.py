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

# intro
slowprint('The year is 2054 and the true first man-operated mission to mars is taking place. \n')
skip = str(input('\n PRESS ENTER TO CONTINUE \n'))
os.system('cls')

slowprint('Only some of the most fit personal were chosen in order to ensure survival. Your name is: \n')
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
