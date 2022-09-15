def sumofn(n):
    if n == 1:
        return n
    return n + sumofn(n - 1)

print(sumofn(5))
