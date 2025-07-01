#!/usr/bin/env python3
from typing import List

def subsetSum(arr: List[int], s: int, n: int, t: List[List[int]]):
    if n == 0:
        if s == 0:
            return True
        return False

    if t[n][s] != -1:
        return t[n][s]

    if arr[n-1] <= s:
        take_it = subsetSum(arr, s-arr[n-1], n-1, t)
        not_take_it = subsetSum(arr, s, n-1, t)
        t[n][s] = take_it or not_take_it
    else:
        t[n][s] = subsetSum(arr, s, n-1, t)
    
    return t[n][s]

arr = [2, 5, 7, 8, 10]
s = 12
t = [[-1 for _ in range(s+1)] for _ in range(len(arr)+1)]
print(subsetSum(arr, s, len(arr), t))