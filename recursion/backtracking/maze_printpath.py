def printpath(p, row, col):
    if row == 1 and col == 1:
        print(p)
        return
    
    if row > 1:
        printpath(p+"D", row-1, col)
    
    if col > 1:
        printpath(p+"R", row, col-1)
        

printpath("",3,3)
