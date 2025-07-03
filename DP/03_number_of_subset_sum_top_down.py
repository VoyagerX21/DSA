#!/usr/bin/env python3
from typing import List

def number_of_subsetSum(arr: List[int], target: int, n: int):
    t = [[0 for _ in range(target+1)] for _ in range(n+1)]
    for i in range(n+1):
        t[i][0] = 1
    for i in range(1, target+1):
        t[0][i] = 0
    
    for i in range(1, n+1):
        for j in range(1, target + 1):
            if arr[i-1] <= j:
                take_it = t[i-1][j-arr[i-1]]
                not_take_it = t[i-1][j]
                t[i][j] = take_it + not_take_it
            else:
                t[i][j] = t[i-1][j]
    
    print(t[n][target])
   

arr = [1, 2, 3, 3]
target = 6
number_of_subsetSum(arr, target, len(arr))