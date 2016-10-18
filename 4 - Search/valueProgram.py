# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    value = [[99 for x in range(len(grid[0]))] for y in range(len(grid))]
    # make sure your function returns a grid of values as 
    # demonstrated in the previous video.
    value[goal[0]][goal[1]] = 0
    openList = []
    openList.append([0, goal[0],goal[1]])
    while len(openList) != 0:
        openList.sort()
        currentCell = openList.pop(0)
        for i in range(len(delta)):
            targetX = currentCell[2] - delta[i][1]
            targetY = currentCell[1] - delta[i][0]
            if inGrid(grid, targetX, targetY):
                if grid[targetY][targetX] == 0 and value[targetY][targetX] == 99:
                    openList.append([currentCell[0]+cost, targetY, targetX])
                    value[targetY][targetX] = currentCell[0] + cost
    return value
    
    
def inGrid(grid, x, y):
    if x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid):
        return True
    else:
        return False

for line in compute_value(grid, goal, cost):
    print line