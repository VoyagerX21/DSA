#!/usr/bin/env python3
from typing import List

def number_of_subsetSum(arr: List[int], target: int, n: int, t: List[List[bool]]):
    if n == 0:
        if target == 0:
            return 1
        return 0

    if t[n][target] != -1:
        return t[n][target]

    if arr[n-1] <= target:
        take_it = number_of_subsetSum(arr, target-arr[n-1], n-1, t)
        not_take_it = number_of_subsetSum(arr, target, n-1, t)
        t[n][target] = take_it + not_take_it
    else:
        t[n][target] = number_of_subsetSum(arr, target, n-1, t)
    
    return t[n][target]

arr = [2, 3, 5, 6, 8, 10]
target = 10
t = [[-1 for _ in range(target + 1)] for _ in range(len(arr)+1)]
print(number_of_subsetSum(arr, target, len(arr), t))