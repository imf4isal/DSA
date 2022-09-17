import math


def count(n):
    return helper(n, 0)

def helper(n, c):
    if n == 0:
        return c
    rem = n % 10
    if rem == 0:
        return helper(math.floor(n/10), c+1)

    return helper(math.floor(n/10), c)


print(count(29104))
