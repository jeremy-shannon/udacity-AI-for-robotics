# -----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
# 
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left, 
# up, and down motions. Note that the 'v' should be 
# lowercase. '*' should mark the goal cell.
#
# You may assume that all test cases for this function
# will have a path from init to goal.
# ----------

grid = [[0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1
expand = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

class Node:
    def __init__(self, x, y):
        self.children = [None,None,None,None]
        self.parent = None
        self.y = y
        self.x = x
    def findByCoords(self,x,y):
        if self.x == x and self.y == y:
            return self
        else:
            for child in self.children:
                if child != None:
                    if child.findByCoords(x,y) != None:
                        return child.findByCoords(x,y)

        
def search(grid,init,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1

    x = init[0]
    y = init[1]
    g = 0
    
    startNode = Node(x,y)
    currentNode = startNode

    open = [[g, x, y]]

    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand

    while not found and not resign:
        if len(open) == 0:
            resign = True
            return 'fail'
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]
            currentNode = startNode.findByCoords(x,y)
            
            if x == goal[0] and y == goal[1]:
                found = True
                expand[x][y] = '*'
                while True:
                    parentNode = currentNode.parent
                    for i in range(len(parentNode.children)):
                        if parentNode.children[i] == currentNode:
                            expand[parentNode.x][parentNode.y] = delta_name[i]
                    if parentNode == startNode:
                        break
                    currentNode = parentNode
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            currentNode.children[i] = Node(x2,y2)
                            childNode = currentNode.children[i]
                            childNode.parent = currentNode
                            closed[x2][y2] = 1

    return expand # make sure you return the shortest path
output = search(grid, init, goal, cost)
for i in output:
    print i