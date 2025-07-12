# Problem statement: You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
from typing import List

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         def solve(arr: List[int], n: int, res: int) -> int:
#             if n >= len(arr):
#                 return res
#             take = solve(arr, n+2, res+arr[n])
#             not_take = solve(arr, n+1, res)
#             return max(take, not_take)
        
#         result = solve(nums, 0, 0)
#         return result

class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(arr: List[int], i: int):
            if i >= len(arr):
                return 0
            if seen[i] != -1:
                return seen[i]
            take = arr[i] + solve(arr, i+2)
            not_take = solve(arr, i+1)
            seen[i] = max(take, not_take)
            return seen[i]
            
        seen = [-1 for _ in range(len(nums))]
        solve(nums, 0)

obj = Solution()
print(obj.rob([2,7,9,3,1]))