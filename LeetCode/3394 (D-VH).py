# QUES
# You are given an integer n representing the dimensions of an n x n grid, with the origin at the bottom-left corner of the grid. You are also given a 2D array of coordinates rectangles, where rectangles[i] is in the form [startx, starty, endx, endy], representing a rectangle on the grid. Each rectangle is defined as follows:
# (startx, starty): The bottom-left corner of the rectangle.
# (endx, endy): The top-right corner of the rectangle.
# Note that the rectangles do not overlap. Your task is to determine if it is possible to make either two horizontal or two vertical cuts on the grid such that:
# Each of the three resulting sections formed by the cuts contains at least one rectangle.
# Every rectangle belongs to exactly one section.
# Return true if such cuts can be made; otherwise, return false.

# Example
#  n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]
# Output: true

# CODE
from typing import List
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x_cords = []
        y_cords = []
        for each in rectangles:
            i, j, k, l = each
            x_cords.append([i, 1])
            x_cords.append([k, 0])
            y_cords.append([j, 1])
            y_cords.append([l, 0])
        
        x_cords.sort()
        y_cords.sort()

        overlap = 0
        lines = 0
        for i in x_cords:
            if i[1] == 0:
                overlap += 1
            else:
                overlap -= 1
            if overlap == 0:
                lines += 1

        if lines >= 3:
            return True
        
        overlap = 0
        lines = 0
        for i in y_cords:
            if i[1] == 0:
                overlap += 1
            else:
                overlap -= 1
            if overlap == 0:
                lines += 1
        
        if lines >= 3:
            return True
        
        return False

obj = Solution()
obj.checkValidCuts(4, [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]])