# Problem statement : Given an array of integers arr[] of size N and a number K. Return the maximum sum of a subarray of size k
# Example :
# Input N = 4, K = 2, arr[] = [100, 200, 300, 400]
# Output 700
from typing import List

# def maxOfWindow(arr: List[int], n: int, k: int):
#     res = -1
#     if n < k:
#         return -1
#     if n == k:
#         return sum(arr)
#     initial = sum(arr[:k])
#     res = max(res, initial)
#     i = k
#     while i < n:
#         initial -= arr[i-k]
#         initial += arr[i]
#         res = max(res, initial)
#         i += 1

#     return res

def maxOfWindow(arr: List[int], n: int, k: int) -> int:
    res = -1
    i = 0
    j = 0
    summ = 0
    while j < n:
        # do calculation
        summ += arr[j]

        if (j-i+1) < k: # window size not yet hit
            j += 1
            # add any other thing according to the problem
        
        elif (j-i+1) == k: # window size hit
            # 1) answer from calculation
            res = max(res, summ)
            # 2) slide the window
            summ -= arr[i]
            i += 1
            j += 1

    return res 

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    res = maxOfWindow(arr, n, k)
    print(res)