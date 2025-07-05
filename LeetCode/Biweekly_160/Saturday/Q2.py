#!/usr/bin/env python3
from typing import List

class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        cost = 1
        i = 0
        j = 0
        while i < m and j < n:
            # entry cost
            first = (i+2)*(j+1) if i+1 != m else -1 #downward
            second = (i+1)*(j+2) if j+1 != n else -1 #rightward

            #both choices are available
            if first != -1 and second != -1:
                first += waitCost[i+1][j]
                second += waitCost[i][j+1]
                if first < second:
                    cost += first
                    i += 1
                elif first > second:
                    cost += second
                    j += 1
                else:
                    if first-waitCost[i+1][j] > second-waitCost[i][j+1]:
                        cost += second
                        j += 1
                    else:
                        cost += first
                        i += 1
            
            # downward choice is only available
            elif first != -1 and second == -1:
                first += waitCost[i+1][j]
                cost += first
                i += 1
            
            # rightward choice is only available
            elif first == -1 and second != -1:
                second += waitCost[i][j+1]
                cost += second
                j += 1
            
            # none choices are available (return kro then)
            else:
                return cost - waitCost[m-1][n-1]

# class Solution:
#     def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
#         # Memoization cache to store min cost to reach (i,j)
#         dp = {}
        
#         def solve(i: int, j: int) -> int:
#             # Base case: reached destination
#             if i == m - 1 and j == n - 1:
#                 return 1  # Initial cost, excluding waitCost[m-1][n-1]
            
#             # Check if result is cached
#             if (i, j) in dp:
#                 return dp[(i, j)]
            
#             min_cost = float('inf')
            
#             # Try moving downward if within bounds
#             if i + 1 < m:
#                 entry_cost = (i + 2) * (j + 1)  # Cost to move to (i+1,j)
#                 total_cost = entry_cost + waitCost[i + 1][j] + solve(i + 1, j)
#                 min_cost = min(min_cost, total_cost)
            
#             # Try moving rightward if within bounds
#             if j + 1 < n:
#                 entry_cost = (i + 1) * (j + 2)  # Cost to move to (i,j+1)
#                 total_cost = entry_cost + waitCost[i][j + 1] + solve(i, j + 1)
#                 min_cost = min(min_cost, total_cost)
            
#             # Cache the result
#             dp[(i, j)] = min_cost
#             return min_cost
        
#         # Start from (0,0)
#         return solve(0, 0) - waitCost[m-1][n-1]


obj = Solution()
print(obj.minCost(2, 3, [[3,3,2],[3,887,2]]))

# Edge case
# m = 2
# n = 3
# waitCost = [[3,3,2],[3,887,2]]

# This test case fails because you preferred downward over rightward by default, which is wrong, we need to backtrack this problem or use recursion so that all possible paths can be traversed.

# In the second approach of the problem as you can see it uses DP, I was using Greedy approach which will not always be optimal path as it misses the crucial future step