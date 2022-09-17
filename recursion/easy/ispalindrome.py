import math


def reverse(n):
    digits = int(math.log10(n)) + 1
    return rev(n, digits)

def rev(n, digits):
    if n%10 == n:
        return n
    rem = n % 10
    return  (rem * math.trunc(math.pow(10, digits - 1)) + rev(math.floor(n/10), digits - 1))

def isPalin(n):
    return n == reverse(n)

print(isPalin(123212))
