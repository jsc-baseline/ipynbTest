import random

fmature = 10# age when a fish gives birth
smature = 20# age when a shark gives birth
nrg = 15# original shark energy

def MakeGrid(N): #inputs: N
    grid = []# creates a list for whole sea
    for i in range(N): #iterates N times
        temp = []# creates a list for each row
        for j in range(N): #iterates N times
            temp.append(['E'])# creates each cell with an 'E' for empty
        grid.append(temp)# appends empty row to grid
    return grid# outputs: grid | returns empty N x N grid

def RandomFish(grid, P): #inputs: grid, P
    V = len(grid)# cols of grid
    H = len(grid[0])# rows of grid
    k = 0# number of fish created
    while k < P: #iterates P times
        v = int(random.random() * V)# selects a random value for cols coordinate
        h = int(random.random() * H)# selects a random value for rows coordinate
        if grid[v][h][0] == 'E': #checks coordinate for empty cell
            newfish = ['F', 0, fmature, 0, False]# creates a new fish
            grid[v][h] = newfish# places fish in empty cell
            k += 1# increments fish counter

def RandomShark(grid, P): #inputs: grid, P
    V = len(grid)# cols of grid
    H = len(grid[0])# rows of grid
    k = 0# number of sharks created
    while k < P: #iterates P times
        v = int(random.random() * V)# selects a random value for cols coordinate
        h = int(random.random() * H)# selects a random value for rows coordinate
        if grid[v][h][0] == 'E': #checks coordinate for empty cell
            newshark = ['S', 0, smature, nrg, False]# creates a new shark
            grid[v][h] = newshark# places fish in empty cell
            k += 1# increments fish counter

def Iterate(grid): #inputs: grid
    MoveFish(grid)# moves fish to new cells
    Age(grid)# increments age of fish
    Birth(grid)# creates new fish
    ReduceEnergy(grid)# reduces energy of sharks
    Feed(grid)# feeds fish to sharks
#    Reset(grid)# resets move flag for next iteration

def MoveFish(grid): #inputs: grid
    rows = len(grid)# rows of grid
    cols = len(grid[0])# cols of grid
    for i in range(rows): #iterates through rows
        for j in range(cols): #iterates through cols
            if grid[i][j][0] == 'F' and grid[i][j][4] == False:
                temp = grid[i][j]
                '''four corners: only two cells to move'''
                if i == 0 and j == 0:           # (0, 0)
                    if grid[i][j + 1][0] == 'E':
                        grid[i][j + 1] = temp
                        grid[i][j + 1][4] = True
                        grid[i][j] = ['E']
                    elif grid[i + 1][j][0] == 'E':
                        grid[i + 1][j] = temp
                        grid[i + 1][j][4] = True
                        grid[i][j] = ['E']
                elif i == 0 and j == (len(grid) - 1): # (0, 9)
                    if grid[i][j - 1][0] == 'E':
                        grid[i][j - 1] = temp
                        grid[i][j - 1][4] = True
                        grid[i][j] = ['E']
                    elif grid[i + 1][j][0] == 'E':
                        grid[i + 1][j] = temp
                        grid[i + 1][j][4] = True
                        grid[i][j] = ['E']
                elif i == (len(grid) - 1) and j == 0: # (9, 0)
                    if grid[i - 1][j][0] == 'E':
                        grid[i - 1][j] = temp
                        grid[i - 1][j][4] = True
                        grid[i][j] = ['E']
                    elif grid[i][j + 1][0] == 'E':
                        grid[i][j + 1] = temp
                        grid[i][j + 1][4] = True
                        grid[i][j] = ['E']
                elif i == (len(grid) - 1) and j == (len(grid) - 1): # (9, 9)
                    if grid[i - 1][j][0] == 'E':
                        grid[i - 1][j] = temp
                        grid[i - 1][j][4] = True
                        grid[i][j] = ['E']
                    elif grid[i][j - 1][0] == 'E':
                        grid[i][j - 1] = temp
                        grid[i][j - 1][4] = True
                        grid[i][j] = ['E']
                '''outer lines: only three cells to move '''
                if i == 0 and (j != 0 or j == (len(grid) - 1)): # (0, 1) to (0, 8)
                    if grid[i][j + 1][0] == 'E':
                        grid[i][j + 1] = temp
                        grid[i][j + 1][4] = True
                        grid[i][j] = ['E']
                    elif grid[i][j - 1][0] == 'E':
                        grid[i][j - 1] = temp
                        grid[i][j - 1][4] = True
                        grid[i][j] = ['E']
                    elif grid[i + 1][j][0] == 'E':
                        grid[i + 1][j] = temp
                        grid[i + 1][j][4] = True
                        grid[i][j] = ['E']
                if (i != 0 or i == (len(grid) - 1)) and j == (len(grid) - 1): # (1, 9) to (8, 9)
                    if grid[i][j - 1][0] == 'E':
                        grid[i][j - 1] = temp
                        grid[i][j - 1][4] = True
                        grid[i][j] = ['E']
                    elif grid[i - 1][j][0] == 'E':
                        grid[i - 1][j] = temp
                        grid[i - 1][j][4] = True
                        grid[i][j] = ['E']
                    elif grid[i + 1][j][0] == 'E':
                        grid[i + 1][j] = temp
                        grid[i + 1][j][4] = True
                        grid[i][j] = ['E']


def Age(grid): #inputs: grid
    for i in range(len(grid)): #iterates through rows
        for j in range(len(grid[0])): #iterates through cols
            if grid[i][j][0] != 'E':
                grid[i][j][1] += 1

def Birth(grid): #inputs: grid
    return

def ReduceEnergy(grid): #inputs: grid
    for i in range(len(grid)): #iterates through rows
        for j in range(len(grid[0])): #iterates through cols
            if grid[i][j][0] == 'S':
                grid[i][j][3] -= 1
                if grid[i][j][3] < 1:
                    grid[i][j] = ['E']

def Feed(grid): #inputs: grid
    rows = len(grid)# rows of grid
    cols = len(grid[0])# cols of grid
    for i in range(rows): #iterates through rows
        for j in range(cols): #iterates through cols
            if grid[i][j][0] == 'S':
                grid[i][j][3] += 1

def Reset(grid): #inputs: grid
    for i in range(len(grid)): #iterates through rows
        for j in range(len(grid[0])): #iterates through cols
            if grid[i][j][0] == 'F':
                grid[i][j][4] = False

grid = MakeGrid(10)
RandomFish(grid, 32)
RandomShark(grid, 4)
for i in range(10): #iterates through rows
    print()
    for j in range(10): #iterates through cols
        print('%32s' % grid[i][j], end = '')
Iterate(grid)
print('\n')
for i in range(10): #iterates through rows
    print()
    for j in range(10): #iterates through cols
        print('%32s' % grid[i][j], end = '')
for i in range(10): #iterates through rows
    print()
    for j in range(10): #iterates through cols
        print('(%2d, %2d)' % (i, j), end = '')







