#!/usr/bin/env python3
from typing import List

def knapsack(wt: List[int], val: List[int], n: int, W: int):
    if n == 0 or W == 0:
        return 0
    if wt[n-1] <= W:
        return max(val[n-1]+knapsack(wt, val, n-1, W-wt[n-1]), knapsack(wt, val, n-1, W))
    elif wt[n-1] > W:
        return knapsack(wt, val, n-1, W)

val = [1,3,4,5]
wt = [1,4,5,7]
n = len(wt)
W = 7
print(knapsack(wt, val, n, W))