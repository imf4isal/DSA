import math


def productofdigit(n):
    if n % 10 == n:
        return n
    return (n%10) * productofdigit(math.floor(n/10))

print(productofdigit(224))
