#!/usr/bin/env python3
from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        g = {i: [] for i in range(len(graph))}
        for i in range(len(graph)):
            for j in graph[i]:
                g[j].append(i)
        
        def helper(end, g):
            if end == 0:
                return [[0]]
        
            res = []
            for i in g[end]:
                r = helper(i, g)
                for each in r:
                    res.append([end]+each)
            
            return res
        
        res = helper(len(graph)-1, g)
        for i in range(len(res)):
            res[i] = res[i][::-1]
        
        return res

obj = Solution()
print(obj.allPathsSourceTarget([[1,2],[3],[3],[]]))