#!/usr/bin/env python

# Problem statement: You need to find the minimum cost to reach the last element of a given vector of positive integers of size N. The cost of moving from one element to another is the absolute difference between the elements. You can only take a jump of max size equal to 3, i.e, if you are at index i, you can go to i+1, i+2 or i+3
# Note: the cost of reaching the first element is 0
# Input: N = 5, arr[] = [30, 10, 60, 10, 60]
# Output: 30

from typing import List
import sys
sys.setrecursionlimit(10**6)

def calculate(pre: List[int], curr: int, arr: List[int]):
    if pre[curr] != -1:
        return pre[curr]

    maxi = 3
    i = curr-1
    d = float('inf')
    while maxi > 0:
        if i >= 0:
            r = calculate(pre, i, arr)
            d = min(d, r+abs(arr[curr]-arr[i]))
            i -= 1
            maxi -= 1
        else:
            break
    
    pre[curr] = d
    return pre[curr] 

def solve(arr: List[int], n: int):
    pre = [-1 for _ in range(n)]
    pre[0] = 0
    calculate(pre, n-1, arr)
    return pre[n-1]

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(arr, n))