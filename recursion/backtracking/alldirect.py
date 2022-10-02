def printpath(p, maze, row, col):
    if row == len(maze) - 1 and col == len(maze) - 1:
        print(p)
        return


    if maze[row][col] == False:
        return

    maze[row][col] = False
    
    if row < len(maze) - 1:
        printpath(p+"D", maze, row+1, col)

    if col < len(maze) - 1:
        printpath(p+"R", maze, row, col+1)

    if row > 0:
        printpath(p+"U", maze, row-1, col)

    if col > 0:
        printpath(p+"L", maze, row, col-1)    
    
    maze[row][col] == True
        
ar = [
    [True, True, True],
    [True, True, True],
    [True, True, True]
]

printpath("", ar, 0, 0)
