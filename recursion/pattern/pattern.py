import os

os.system('cls')


#pattern 1: 
# * * * *
# * * *
# * *
# *

def pattern1(r, c):
    if r == 0:
        return

    if c < r:
        print("*", end="")
        pattern1(r, c+1)
    else:
        print()
        pattern1(r-1, 0)

pattern1(4, 0)

def pattern2(r, c):
    if r == 0:
        return

    if c < r:
        pattern2(r, c+1)
        print("*", end="")
    else:
        pattern2(r-1, 0)
        print()

pattern2(4, 0)


def bubble(arr, r, c):
    if r == 0:
        return

    if c < r:
        if arr[c] > arr[c+1]:
            #swap
            temp = arr[c]
            arr[c] = arr[c+1]
            arr[c+1] = temp
        
        bubble(arr, r, c+1)  
    else:
        bubble(arr, r-1, 0)

ar = [4, 3, 2, 1]
bubble(ar, len(ar) - 1, 0)
print()
print()
print(ar)

def selection(arr, r, c, max):
    if r == 0:
        return

    if c < r:
        if arr[c+1] > arr[max]:
            selection(arr, r, c+1, c+1)
        else:
            selection(arr, r, c+1, max)
    else:
        temp = arr[max]
        arr[max] = arr[len(arr)-1]
        arr[len(arr)-1] = temp
        selection(arr, r-1, 0, 0)



ar1 = [4, 3, 2, 1]
selection(ar1, len(ar1) - 1, 0, 0)
print()
print()
print(ar1)
