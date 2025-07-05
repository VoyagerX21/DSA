#!/usr/bin/env python3
from typing import List

def fn(arr: List[int], target: int, n: int, d: int):
    t = [[-1 for _ in range(target + 1)] for _ in range(n+1)]
    for i in range(n+1):
        t[i][0] = 1
    for j in range(1, target + 1):
        t[0][j] = 0
    
    for i in range(1, n+1):
        for j in range(1, target+1):
            if arr[i-1] <= j:
                take = t[i-1][j-arr[i-1]]
                not_take = t[i-1][j]
                t[i][j] = take + not_take
            else:
                t[i][j] = t[i-1][j]
        
    return t[n][target]

arr = [1, 2, 3, 4, 5]
d = 3
if (sum(arr)+d) % 2 != 0:
    print(0)
else:
    print(fn(arr, (sum(arr)+d)//2, len(arr), d))