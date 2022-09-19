import math


def mergesortInPlace(arr, s , e):
    if e - s == 1:
        return arr
    mid = math.floor(len(arr) / 2)

    mergesortInPlace(arr, s, mid)
    mergesortInPlace(arr, mid+1, e)

    mergeInPlace(arr, s, mid, e)

def mergeInPlace(arr, start, mid, end):
    mix = [0 for i in range(len(arr))]
    i = start
    j = mid+1
    k = 0

    while i < mid and j < end:

        if arr[i] < arr[j]:
            mix[k] = arr[i]
            i += 1
        else:
            mix[k] = arr[j]
            j += 1
        k += 1
    
    while i < mid:
        mix[k] = arr[i]
        k += 1
        i += 1

    while j < end:
        mix[k] = arr[j]
        k += 1
        j += 1       
    
    return mix



def mergesort(arr):

    if len(arr) == 1:
        return arr
    mid = math.floor(len(arr) / 2)

    left = mergesort(arr[0:mid])
    right = mergesort(arr[mid:len(arr)])

    return merge(left, right)

def merge(lh, rh):
    mix = [0 for i in range(len(lh)+len(rh))]
    i = 0
    j = 0
    k = 0

    while i < len(lh) and j < len(rh):

        if lh[i] < rh[j]:
            mix[k] = lh[i]
            i += 1
        else:
            mix[k] = rh[j]
            j += 1
        k += 1
    
    while i < len(lh):
        mix[k] = lh[i]
        k += 1
        i += 1

    while j < len(rh):
        mix[k] = rh[j]
        k += 1
        j += 1       
    
    return mix



arr = [5, 4, 3, 2, 1]

arr1 = mergesortInPlace(arr, 0, len(arr))

print(arr1)
print(arr)
