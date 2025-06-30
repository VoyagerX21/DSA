#!/usr/bin/env python3
from typing import List

def knapsack(wt:List[int], val: List[int], n: int, W: int):
    t = [[-1 for _ in range(W+1)] for _ in range(n+1)] # initialization of the dp

    # Base condition fulfilled of recursion
    for i in range(n+1):
        t[i][0] = 0
    for i in range(W+1):
        t[0][i] = 0

    for i in range(1, n+1):
        for j in range(1, W+1):
            if wt[i-1] <= j: # just replace the actual n-1 and W with i and j and boom
                take_it = val[i-1] + t[i-1][j-wt[i-1]]
                not_take_it = t[i-1][j]
                t[i][j] = max(take_it, not_take_it)
            else:
                t[i][j] = t[i-1][j] # same as not take it
    
    return t[n][W] # answer will be in the last cell

val = [1,3,4,5]
wt = [1,4,3,7]
n = len(wt)
W = 7
print(knapsack(wt, val, n, W))