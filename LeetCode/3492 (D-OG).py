# QUESTION

# You are given a positive integer n representing an n x n cargo deck on a ship. Each cell on the deck can hold one container with a weight of exactly w. However, the total weight of all containers, if loaded onto the deck, must not exceed the ship's maximum weight capacity, maxWeight.
# Return the maximum number of containers that can be loaded onto the ship.

# EXAMPLE 
# Input: n = 2, w = 3, maxWeight = 15
# Output: 4
# Explanation:
# The deck has 4 cells, and each container weighs 3. The total weight of loading all containers is 12, which does not exceed maxWeight.

# CODE
class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        return min(maxWeight//w, n*n)

obj = Solution()
obj.maxContainers(2, 3, 15)