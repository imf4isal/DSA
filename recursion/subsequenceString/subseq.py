
import os

os.system("cls")


def subseq(p, up, arr):
    if len(up) == 0:
        arr.append(p)
        return
    
    char = up[0]
    subseq(p + char, up[1:], arr)
    subseq(p, up[1:], arr)

arr = []
subseq("", "abc", arr)
print(arr)


def subseqret(p, up):
    if len(up) == 0:
        arr = []
        arr.append(p)
        return arr
    
    char = up[0]
    fh = subseqret(p + char, up[1:])
    sh = subseqret(p, up[1:])
    return fh+sh


print(subseqret("", "abc"))


