#!/usr/bin/env python3
from typing import List

def subsetSum(arr: List[int], s: int, n: int):
    global t

arr = [2, 3, 7, 8, 10]
s = 11
n = len(arr)
global t
t = [[-1 for _ in range(s+1)] for _ in range(n+1)]