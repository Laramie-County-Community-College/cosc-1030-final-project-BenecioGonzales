# Imports random number generator
import random


# Important variables for basics of code
time_left = 30
thr_pt = .3
two_pt = .5
frthr  = .7
off_rebound = .2
ovr_vict = .5
team_pts = 0
enemy_pts = 3



# Three point calculator
if time_left > 0:
    if random.random() < thr_pt:
            team_pts + 3
            time_left - 10
    else:
            team_pts + 3
            time_left - 10
else:
    if team_pts < enemy_pts:
        loss
    elif team_pts == enemy_pts:
        if random.random() > ovr_vict:
            