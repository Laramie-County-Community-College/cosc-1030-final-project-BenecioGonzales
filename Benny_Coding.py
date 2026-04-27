# Imports random number generator
import random

# Important variables for basics of code
time_left = 30
thr_pt = .3
two_pt = .5
frthr  = .7
off_rebound = .2
ovr_vict = .5
possesion = True


# Three point calculator
while possesion:
    if time_left > 0:
        if random.random() < thr_pt:
            + 3
            time_left - 2
        else:
            + 0
            time_left - 2
    else:
        break