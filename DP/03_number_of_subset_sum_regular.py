#!/usr/bin/env python3
from typing import List

def number_of_subsetSum(arr: List[int], target: int, n: int):
    global c
    if n == 0:
        if target == 0:
            c += 1
        return
    
    if arr[n-1] <= target:
        number_of_subsetSum(arr, target-arr[n-1], n-1)
        number_of_subsetSum(arr, target, n-1)
    else:
        number_of_subsetSum(arr, target, n-1)

arr = [2, 3, 5, 6, 7, 10]
target = 11
global c
c = 0
number_of_subsetSum(arr, target, len(arr))
print(c)
