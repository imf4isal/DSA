def printpath(p, row, col):
    if row == 1 and col == 1:
        l = []
        l.append(p)
        return l
    
    list = []
    if row > 1:
        list.extend(printpath(p+"D", row-1, col))
    
    if col > 1:
        list.extend(printpath(p+"R", row, col-1))
    return list

print(printpath("",3,3))
