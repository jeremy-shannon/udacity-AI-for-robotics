# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's 
# optimal path to the position specified in goal; 
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a 
# right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [2, 0] # given in the form [row,col]

cost = [2, 1, 20] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid,init,goal,cost):
    value = [[[999 for facing in range(len(forward))]\
        for col in range(len(grid[0]))]\
        for row in range(len(grid))]
    policy = [[[' ' for facing in range(len(forward))]\
        for col in range(len(grid[0]))]\
        for row in range(len(grid))]
    change = True
    
    while change:
        change = False
        
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                for f in range(len(forward)):
                    if x == goal[1] and y == goal[0]:
                        if value[y][x][f] > 0:
                            value[y][x][f] = 0
                            policy[y][x][f] = '*'
                            change = True
                    elif grid[y][x] == 0:
                        for f2 in range(len(forward)):
                            x2 = x + forward[f2][1]
                            y2 = y + forward[f2][0]
                            if x2 >= 0 and x2 < len(grid[0]) and y2 >= 0 and y2 < len(grid) and grid[y2][x2] == 0:
                                targetVal = value[y2][x2][f2]
                                for a in range(len(action)):
                                    if (f + action[a]) % len(forward) == f2:
                                        v2 = targetVal + cost[a]
                                        if v2 < value[y][x][f]:
                                            value[y][x][f] = v2
                                            policy[y][x][f] = action_name[a]
                                            change = True
                                    
    policy2D = [[' ' for x in range(len(grid[0]))] for y in range(len(grid))]
    x = init[1]
    y = init[0]
    f = init[2]
    policy2D[y][x] = policy[y][x][f]

    while policy[y][x][f] != '*':
        if policy[y][x][f] == 'R':
            f = (f - 1) % 4
        elif policy[y][x][f] == 'L':
            f = (f + 1) % 4
        x += forward[f][1]
        y += forward[f][0]
        policy2D[y][x] = policy[y][x][f]
    return policy2D

for line in optimum_policy2D(grid,init,goal,cost):
    print line