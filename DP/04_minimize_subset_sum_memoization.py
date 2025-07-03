#!/usr/bin/env python3

def subsetSum(arr, target, n, t):
    if n == 0:
        if target == 0:
            return True
        return False
    
    if t[n][target] != -1:
        return t[n][target]

    if arr[n-1] <= target:
        take_it = subsetSum(arr, target-arr[n-1], n-1, t)
        not_take_it = subsetSum(arr, target, n-1, t)
        t[n][target] = take_it or not_take_it
    else:
        t[n][target] = subsetSum(arr, target, n-1, t)
    
    return t[n][target]

arr = [1, 6, 11 ,5]
range_sum = sum(arr) // 2
while range_sum:
    t = [[-1 for _ in range(range_sum+1)] for _ in range(len(arr)+1)]
    if subsetSum(arr, range_sum, len(arr), t):
        print(sum(arr)-2*range_sum)
        break
    range_sum -= 1