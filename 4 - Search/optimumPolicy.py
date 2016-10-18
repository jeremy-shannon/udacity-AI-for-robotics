# ----------
# User Instructions:
# 
# Write a function optimum_policy that returns
# a grid which shows the optimum policy for robot
# motion. This means there should be an optimum
# direction associated with each navigable cell from
# which the goal can be reached.
# 
# Unnavigable cells as well as cells from which 
# the goal cannot be reached should have a string 
# containing a single space (' '), as shown in the 
# previous video. The goal cell should have '*'.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def optimum_policy(grid,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    change = True

    while change:
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if goal[0] == x and goal[1] == y:
                    if value[x][y] > 0:
                        value[x][y] = 0

                        change = True

                elif grid[x][y] == 0:
                    for a in range(len(delta)):
                        x2 = x + delta[a][0]
                        y2 = y + delta[a][1]

                        if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                            v2 = value[x2][y2] + cost

                            if v2 < value[x][y]:
                                change = True
                                value[x][y] = v2
    
    policy = [[' ' for x in range(len(grid[0]))] for y in range(len(grid))]
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if value[y][x] == 99:
                continue
            if value[y][x] == 0:
                policy[y][x] = '*'
                continue
            surroundingCells = [99,99,99,99]
            for i in range(len(delta)):
                x2 = x + delta[i][1]
                y2 = y + delta[i][0]
                if x2 >= 0 and x2 < len(grid[0]) and y2 >= 0 and y2 < len(grid):
                    surroundingCells[i] = value[y2][x2]
            minVal = min(surroundingCells)
            for j in range(len(surroundingCells)):
                if surroundingCells[j] == minVal and minVal != 99:
                    policy[y][x] = delta_name[j]

    return policy

for line in optimum_policy(grid, goal, cost):
    print line