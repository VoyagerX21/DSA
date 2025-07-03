#!/usr/bin/env python3

def subsetSum(arr, target: int, n: int):
    t = [[-1 for _ in range(target+1)] for _ in range(n+1)]
    for i in range(n+1):
        t[i][0] = True
    for i in range(1, target + 1):
        t[0][i] = False

    for i in range(1, n+1):
        for j in range(target + 1):
            if arr[i-1] <= j:
                take = t[i-1][j-arr[i-1]]
                not_take = t[i-1][j]
                t[i][j] = take or not_take
            else:
                t[i][j] = t[i-1][j]
    
    return t[n][target]

arr = [1, 6, 11 ,5]
range_sum = sum(arr) // 2
while range_sum:
    if subsetSum(arr, range_sum, len(arr)):
        print(sum(arr)-2*range_sum)
        break
    range_sum -= 1