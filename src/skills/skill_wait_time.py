import random
import sys
import time

##### Skill Wait Time #####

# Skill Wait time function 
# Determines how long skill actions take based on skill level and rng
def skill_wait_time(number):
    if number == 0:     # Low level/long skill time
        rng = random.randrange(4)
        if rng == 0:
            periods = (".........\n")
        elif rng == 1:
            periods = (".......\n")
        elif rng == 2:
            periods = (".....\n")
        else:
            periods = ("...\n")
    elif number == 1:
        rng = random.randrange(3)
        if rng == 0:
            periods = (".......\n")
        elif rng == 1:
            periods = (".....\n")
        else:
            periods = ("...\n")
    elif number == 2:
        rng = random.randrange(2)
        if rng == 0:
            periods = (".....\n")
        else:
            periods = ("...\n")
    elif number == 3:   # High level/short skill time
        periods = ("...\n")    
    for character in periods:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.6)