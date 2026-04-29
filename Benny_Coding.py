# Imports random number generator
import random    

# Important variables for basics of code
thr_pt_per = .32
two_pt_per = .53
fr_thr_per  = .68
off_rebound = .21
ovr_vict = .5

# Defines the function
def simulate(strategy):
    wins = 0
    team_pts_total = 0
    
    for times in range(10000):
        time_left = 30
        team_pts = 0
        enemy_pts = 3
        while time_left > 0:
            
            # Three point strategy
            if strategy == "three":    
                if random.random() < thr_pt_per:
                    team_pts += 3
                    time_left -= random.randint(8, 12)
                else:
                    time_left -= random.randint(8, 12)

            # Two point strategy
            elif strategy == "two":

            # Score calculator
        if team_pts > enemy_pts:
                wins += 1
        elif team_pts == enemy_pts:
                if random.random() < ovr_vict:
                    wins += 1
        team_pts_total += team_pts
    return wins, team_pts_total/10000

# Two point calculator
for times in range(10000):
    time_left = 30
    team_pts = 0
    enemy_pts = 3
    while time_left > 0:
        if time_left > 10:
            if random.random() < two_pt_per:
                team_pts += 2
                time_left -= random.randint(8, 12)
            else:
                time_left -= random.randint(8, 12)

        # Fouling the enemy
        else:
            for times in range(2):
                if random.random() < fr_thr_per:
                    enemy_pts += 1
                else:
                    enemy_pts += 0
            if random.random() < off_rebound:
                if random.random() < two_pt_per:
                    team_pts += 2
                    time_left -= random.randint(8, 12)
                else:
                    time_left -= random.randint(8, 12)
            else:
                time_left -= random.randint(8, 12)
    # Score calculator
    if team_pts > enemy_pts:
        two_pt_vict += 1
    elif team_pts == enemy_pts:
        if random.random() < ovr_vict:
            two_pt_vict += 1
        else:
            two_pt_vict += 0
    team_pts_total_two += team_pts

wins_3pt, thr_avg_pts = simulate("three")
wins_2pt, two_avg_pts = simulate("two")

print(f"The percentage chance of winning only going for threes is {wins_3pt/10000 * 100:.1f}% and the average points scored is {thr_avg_pts:.2f}")
print(f"The percentage chance of winning only going for twos is {wins_2pt/10000 * 100:.1f}% and the average points scored is {two_avg_pts:.2f}")