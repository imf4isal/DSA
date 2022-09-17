
import math

# sum = 0

# def reversenumber(n):
#     if n == 0:
#         return
#     global sum
#     sum = (sum * 10) + (n%10)
#     reversenumber(math.floor(n/10))


# reversenumber(243631)
# print(sum)


###alt way

def reverse(n):
    digits = int(math.log10(n)) + 1
    print(digits)
    return rev(n, digits)

def rev(n, digits):
    if n%10 == n:
        return n
    rem = n % 10
    return  (rem * math.trunc(math.pow(10, digits - 1)) + rev(math.floor(n/10), digits - 1))

print(reverse(23443))
