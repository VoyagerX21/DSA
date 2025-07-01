#!/usr/bin/env python3
from typing import List

def subsetSum(arr: List[int], s: int, n: int):
    t = [[-1 for _ in range(s+1)] for _ in range(n+1)]
    # initialization sochna pdta h as you know
    # array mein elements zero hue (n=0) and sum non-zero mannge toh (s != 0), obviously False
    for i in range(1, s+1):
        t[0][i] = False
    # array mein elements kitne bhi ho but sum humesha zero maange toh, obviously always true (empty set ka sum = 0)
    for i in range(n+1):
        t[i][0] = True
    # hogya initialization but bss condition likhon or chlte bano
    for i in range(1, n+1):
        for j in range(1, s+1):
            # first condition
            if arr[i-1] <= j:
                take = t[i-1][j-arr[i-1]]
                not_take = t[i-1][j]
                t[i][j] = take or not_take
            # second case
            else:
                t[i][j] = t[i-1][j]
    
    return t[n][s]

arr = [2, 5, 7, 8, 10]
s = 32
print(subsetSum(arr, s, len(arr)))