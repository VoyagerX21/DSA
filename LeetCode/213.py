from typing import List

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
        
        seen = [-1 for _ in range(len(nums)-1)]
        solve(nums[:-1], 0)
        t1 = seen[0]
        seen = [-1 for _ in range(len(nums)-1)]
        solve(nums[1:], 0)
        t2 = seen[0]
        return max(t1, t2)

obj = Solution()
print(obj.rob([1,2,3]))