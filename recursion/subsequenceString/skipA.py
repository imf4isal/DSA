

def skip(p, up):
    if len(up) == 0:
        print(p)
        return

    char = up[0]

    if char == "a":
        skip(p, up[1:])
    else:
        skip(p+char, up[1:])

skip("","bacaccd")


def skip2(up):
    if len(up) == 0:
        return ""

    char = up[0]

    if char == "a":
        return skip2(up[1:])
    else:
        return char + skip2(up[1:])

print(skip2("bcaccad"))

def skipapple(up):
    if len(up) == 0:
        return ""


    if up.startswith("apple"):
        return skipapple(up[5:])
    else:
        return up[0] + skipapple(up[1:])

print(skipapple("bcappled"))
