#!/usr/bin/env python3
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while left <= right and top <= bottom:
            # Traverse from left to right
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1

            # Traverse downwards
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1

            # Make sure we are now on a different row
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1

            # Make sure we are now in a different column
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1

        return res

obj = Solution()
res = obj.spiralOrder([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
print(res)