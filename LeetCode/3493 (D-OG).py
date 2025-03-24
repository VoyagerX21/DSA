# QUESTION

# You are given a 2D integer array properties having dimensions n x m and an integer k.
# Define a function intersect(a, b) that returns the number of distinct integers common to both arrays a and b.
# Construct an undirected graph where each index i corresponds to properties[i]. There is an edge between node i and node j if and only if intersect(properties[i], properties[j]) >= k, where i and j are in the range [0, n - 1] and i != j.
# Return the number of connected components in the resulting graph.

# EXAMPLE 
# Input: properties = [[1,2],[1,1],[3,4],[4,5],[5,6],[7,7]], k = 1
# Output: 3
# Explanation:
# The graph formed has 3 connected components:

# CODE
from typing import List

def dfs(graph: dict, visited: dict, start: int) -> None:
    visited[start] = 1
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, visited, i)

def count_components(graph: dict) -> int:
    res = 0
    s = [_ for _ in range(len(graph))]
    while s:
        visited = {_: 0 for _ in range(len(graph))}
        dfs(graph, visited, s[0])
        for _ in visited:
            if visited[_] == 1:
                s.remove(_)
        res += 1
    
    return res

class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        pro = list(map(set, properties))
        graph = {_: [] for _ in range(len(pro))}

        for i in range(len(pro)):
            for j in range(len(pro)):
                if i != j:
                    if len(pro[i].intersection(pro[j])) >= k:
                        graph[i].append(j)
        
        return count_components(graph)

obj = Solution()
print(obj.numberOfComponents([[1,1],[1,1]], 2))