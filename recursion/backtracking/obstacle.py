def printpath(p, maze, row, col):
    if row == 2 and col == 2:
        print(p)
        return

    if maze[row][col] == False:
        return

    if row < 2:
        printpath(p+"D", maze, row+1, col)
    
    if col < 2:
        printpath(p+"R", maze, row, col+1)
        
ar = [
    [True, True, True],
    [True, False, True],
    [True, True, True]
]
printpath("", ar, 0, 0)
