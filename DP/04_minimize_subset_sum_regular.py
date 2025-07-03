#!/usr/bin/env python3

def subsetSum(arr, target, n):
    if n == 0:
        if target == 0:
            return True
        return False

    if arr[n-1] <= target:
        return subsetSum(arr, target-arr[n-1], n-1) or subsetSum(arr, target, n-1)
    else:
        return subsetSum(arr, target, n-1)

arr = [1, 6, 11, 5]
range_sum = sum(arr)//2

while range_sum:
    if subsetSum(arr, range_sum, len(arr)):
        print(sum(arr)-2*range_sum)
        break
    range_sum -= 1