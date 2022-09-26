def countpath(row, col):
    if row == 1 or col == 1:
        return 1
    
    left = countpath(row - 1, col)
    right = countpath(row, col - 1)
    return left + right

count = countpath(3,3)
print(count)
