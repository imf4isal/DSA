
def permutation(p, up):
    if len(up) == 0:
        print(p)
        return
    
    char = up[0]

    for i in range(len(p)+1):
        first = p[0:i]
        last = p[i:len(p)]
        permutation(first+char+last,up[1:])
        
permutation("","abc")

def permutationlist(p, up):
    if len(up) == 0:
        lst = []
        lst.append(p)
        return lst
    char = up[0]
    arr = []

    for i in range(len(p)+1):
        first = p[0:i]
        last = p[i:len(p)]
        ans = permutationlist(first+char+last,up[1:])
        arr.extend(ans)
    return arr
        
anss = permutationlist("","abc")
print(anss)


def permutationcount(p, up):
    if len(up) == 0:
        
        return 1
    
    char = up[0]
    count = 0
    for i in range(len(p)+1):
        first = p[0:i]
        last = p[i:len(p)]
        count = count+permutationcount(first+char+last,up[1:])
    return count 
count = permutationcount("","abc")
print(count)
