# def sumofn(n):
#     if n == 1:
#         return n
#     return n + sumofn(n - 1)

# print(sumofn(5))


def s(n, sum):
    if n == 0:
        print(sum)
        return
    s(n-1, sum+n)

s(3, 0)
