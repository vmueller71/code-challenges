"""
You are being attacked by an army of robots!
Luckily they are rather stupid and approach in one row.

Every robot has an armor value of larger than 0.
To defend yourself you have a single shot front loader rifle that will reduce
a robots armor value by 1.
If a robots armor value goes below 1, it will explode and inflict a damage of 2
(reducing armor by 2) to the robots standing next to it.

So, given a list of robot armor values, your function robotAttack must return 
the minimum number of bullets you have to use to destroy all the robots

Attention: A value 0 in the list of robots means, that this space is not taken by a robot.

Sample:
Input: robots = [1, 2, 1, 2, 1, 1]
Output: 1

Input: robots = [3, 3, 3]
Output: 5

Input: robots = [3, 0, 3, 0, 3]
Output: 9

But we also want to know if we are able to survive the attack!!

So we need an additional function will_we_survive(robots, distance) that accepts a list of robots,
and how many meters away they are.

Now, knowing that reloading a front loader takes exactly 10 seconds, and that
the approaching row of robots jumps 10 meters forward every 5 seconds, your function
must return a boolean value if we can kill all robots in time.

Remember that your gun is empty at the beginning of the attack!

"""

def robot_attack(robots):
    # Your code goes here
    shots_fired = 0
    while any_robots_alive(robots):
        robot_to_kill = find_weakest_robot(robots)
        shots_fired += robots[robot_to_kill]
        robots = kill_robot(robots, robot_to_kill)

    return shots_fired

def find_weakest_robot(robots):
    idx = 0
    min_armor = 10000
    for i in range(0, len(robots)):
        if robots[i] < min_armor and robots[i] > 0:
            min_armor = robots[i]
            idx = i
    return idx

def kill_robot(robots, idx):
    robots[idx] = 0
    if idx:
        if robots[idx - 1] > 2:
            robots[idx - 1] -= 2
        elif robots[idx - 1] in [1, 2]:
            robots = kill_robot(robots, idx-1)
    if idx < len(robots) - 1:
        if robots[idx + 1] > 2:
            robots[idx + 1] -= 2
        elif robots[idx + 1] in [1, 2]:
            robots = kill_robot(robots, idx+1)

    return robots

def any_robots_alive(robots):
    for robot in robots:
        if robot:
            return True

def will_we_survive(robots, distance):
    seconds_needed_to_kill_em_all = float(robot_attack(robots) * 10)
    seconds_before_they_get_me = float(distance) / 10 * 5

    return seconds_needed_to_kill_em_all < seconds_before_they_get_me
