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
thr_pt_vict = 0
two_pt_vict = 0


# Three point calculator
for times in range(10000):
    time_left = 30
    team_pts = 0
    enemy_pts = 3
    while time_left > 0:
        if random.random() < thr_pt:
            team_pts += 3
            time_left -= 10
        else:
            time_left -= 10

    # Score calculator
    if team_pts > enemy_pts:
        thr_pt_vict += 1
    elif team_pts == enemy_pts:
        if random.random() < ovr_vict:
            thr_pt_vict += 1
        else:
            thr_pt_vict += 0
    else:
        thr_pt_vict += 0

print(f"The percentage chance of winning only going for threes is {thr_pt_vict/10000 * 100:.0f}%