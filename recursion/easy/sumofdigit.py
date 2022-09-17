import math


def sumofdigit(n):
    if n == 0:
        return 0
    return (n%10) + sumofdigit(math.floor(n/10))

print(sumofdigit(124))
