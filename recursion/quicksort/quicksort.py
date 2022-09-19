import os

os.system("cls")

import math


def quicksort(arr):
    if len(arr) < 2:
        return arr
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            #swap
            temp = arr[0]
            arr[0] = arr[1]
            arr[1] = temp

            return arr
    else:
        mid = math.floor(len(arr)/2)
        pivot = arr[0]

        left = [i for i in arr[1:] if i <= pivot]
        right = [i for i in arr[1:] if i > pivot]

        return quicksort(left) + [pivot] + quicksort(right)

arr1 = [5, 6, 9, 3, 7, 2, 1]
print(quicksort(arr1))

