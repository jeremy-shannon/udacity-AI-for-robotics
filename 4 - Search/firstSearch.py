# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    take = [0,init[0],init[1]]
    print "take:", take
    open = []
    path = "fail"
    while True:
        if take[1] == goal[0] and take[2] == goal[1]:
            print "success!"
            path = take
            break
        for dir in delta:
            cell = [take[0]+cost,take[1]+dir[0],take[2]+dir[1]]
            if cell[1] > -1 and cell[1] < len(grid) and cell[2] > -1 and\
            cell[2] < len(grid[0]) and grid[cell[1]][cell[2]] == 0:
                open.append(cell)
        grid[take[1]][take[2]] = 2
        if len(open) == 0:
            break
        open.sort()
        print "open:", open
        take = open[0]
        print "take:", take
        open.pop(0)
    return path

print search(grid,init,goal,cost)