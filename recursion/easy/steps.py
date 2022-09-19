import math


def steps(n):
    return helper(n, 0)

def helper(n, c):
    if n == 0:
        return c
    rem = n % 2
    if rem == 0:
        return helper(math.floor(n/2), c+1)
    else:
        return helper(n-1, c+1)


print(steps(14))
