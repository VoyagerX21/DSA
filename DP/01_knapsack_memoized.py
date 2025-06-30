#!/usr/bin/env python3
from typing import List

def knapsack(wt: List[int], val: List[int], n: int, W: int):
    if n == 0 or W == 0:
        return 0
    # Hum ek function call me t[n][W] calculate krne ki koshish kr rhe h
    # firstly check hi kr lete h t[n][W] already toh nhi h
    if t[n][W] != -1:
        return t[n][W]
    # nhi h toh calculate krna pdega jiske lie 2 conditions h, first wt[n-1]<w and second is wt[n-1]>w
    if wt[n-1] <= W: # first condition
        take_it = val[n-1] + knapsack(wt, val, n-1, W-wt[n-1]) # jb woh t[n-1][W-wt[n-1]] k lie jaega toh first line mein hi return aa jaega if present hua toh
        not_take_it = knapsack(wt, val, n-1, W) # jb woh t[n-1][W] k lie jaega toh first line mein hi return aa jaega if present hua toh that's why first check is important
        t[n][W] = max(take_it, not_take_it)
    else: # second condition
        t[n][W] = knapsack(wt, val, n-1, W)
    
    return t[n][W] # abb calculate hogya toh return hi krdo

val = [1,3,4,5]
wt = [1,4,3,7]
n = len(wt)
W = 7
t = [[-1 for _ in range(W+1)] for _ in range(n+1)]
print(knapsack(wt, val, n, W))