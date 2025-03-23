# QUESTION

# You are given a circular array nums and an array queries.
# For each query i, you have to find the following:
# The minimum distance between the element at index queries[i] and any other index j in the circular array, where nums[j] == nums[queries[i]]. If no such index exists, the answer for that query should be -1.
# Return an array answer of the same size as queries, where answer[i] represents the result for query i.

# EXAMPLE 
# Input: nums = [1,3,1,4,1,3,2], queries = [0,3,5]
# Output: [2,-1,3]
# Explanation:
# Query 0: The element at queries[0] = 0 is nums[0] = 1. The nearest index with the same value is 2, and the distance between them is 2.
# Query 1: The element at queries[1] = 3 is nums[3] = 4. No other index contains 4, so the result is -1.
# Query 2: The element at queries[2] = 5 is nums[5] = 3. The nearest index with the same value is 1, and the distance between them is 3 (following the circular path: 5 -> 6 -> 0 -> 1).

# CODE
from typing import List

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        dic = dict()
        for i in range(len(nums)):
            try:
                dic[nums[i]].append(i)
            except:
                dic[nums[i]] = [i]
        
        idx = {i: nums[i] for i in range(len(nums))}
        
        res = [-1 for i in range(len(queries))]
        for i in range(len(queries)):
            m = idx[queries[i]]
            if len(dic[m]) == 1:
                continue
            for j in dic[m]:
                if j != queries[i]:
                    res[i] = j
                    break
        
        return res

obj = Solution()
print(obj.solveQueries([1,3,1,4,1,3,2], [0,3,5]))
