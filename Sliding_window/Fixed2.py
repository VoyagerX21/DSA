# Problem statement : Given an array and a positive integer k, find the first negative integer for each window (contiguous subarray) of size k
# Example :
# Input N = 5, K = 2, arr[] = [-8, 2, 3, -6, 10]
# Output [-8, 0, -6, -6]
from typing import List

# def find(arr: List[int], start: int, end: int) -> int:
#     for i in range(start, end+1):
#         if arr[i] < 0:
#             return i
    
#     return -1

# def firstNegInWindow(arr: List[int], n: int, k: int) -> List[int]:
#     if n < k:
#         return [-1]
    
#     if n == k:
#         u = find(arr, 0, len(arr)-1)
#         if u == -1:
#             return [0]
#         return [arr[u]]

#     so_far = find(arr, 0, k-1)
#     res = [arr[so_far] if so_far != -1 else 0]
#     i = 1
#     while i <= n-k:
#         start = i
#         end = i+k-1
#         if so_far != -1:
#             if start <= so_far <= end:
#                 res.append(arr[so_far])
#             else:
#                 so_far = find(arr, start, end)
#                 if so_far == -1:
#                     res.append(0)
#                 else:
#                     res.append(arr[so_far])
#         else:
#             so_far = find(arr, start, end)
#             if so_far == -1:
#                 res.append(0)
#             else:
#                 res.append(arr[so_far])
#         i += 1
    
#     return res

def firstNegInWindow(arr: List[int], n: int, k: int) -> List[int]:
    res, i, j, d= [], 0, 0, [] # initialization basic
    while j < n:
        # Calculation part
        if arr[j] < 0:
            d.append(arr[j])

        # first condition of not hitting
        if j-i+1 < k:
            j+=1

        # second condition for hitting
        elif j-i+1 == k:
            # checking if d is empty or not
            if d:
                res.append(d[0])
                # slide krne se pehle check kro ki htane wala element kahi top pe toh nhi hai, agar h toh usse bhi hta do
                if d[0] == arr[i]:
                    d.pop(0)
            else:
                # d hi empty hai toh 0 daal do
                res.append(0)
            # mandatory increment
            i += 1
            j += 1

    return res

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    res = firstNegInWindow(arr, n, k)
    print(res)