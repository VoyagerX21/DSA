from typing import List
from collections import Counter

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        while nums:
            t = []
            j = set(nums)
            for i in j:
                t.append(i)
                nums.remove(i)
            res.append(t)
        
        return res

obj = Solution()
print(obj.findMatrix([4,5,3,3,3]))