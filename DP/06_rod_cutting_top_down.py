#!/usr/bin/env python3
from typing import List

def cuts(arr: List[int], n: int):
    t = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n+1):
        t[i][0] = 0
        t[0][i] = 0
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i <= j:
                take_it = arr[i-1] + t[i-1][j-i]
                not_take_it = t[i-1][j]
                t[i][j] = max(take_it, not_take_it)
            else:
                t[i][j] = t[i-1][j]
    
    return t[n][n]

arr = [3,5,8,9,10,17,17,20]
print(cuts(arr, len(arr)))