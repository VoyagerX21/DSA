from typing import List

class Solution:
    def distance(self, graph: dict, start: int, online: dict, depth: int, visited: dict) -> int:
        # explore neighbours
        visited[start] = 1
        for i in graph[start]:
            if online[i] == 1 and visited[i] == 0:
                return i
        
        # explore neighborur's neighbour
        for i in graph[start]:
            if visited[i] == 0:
                res = self.distance(graph, i, online, depth+1, visited)
                if res != -1:
                    return res
        
        return -1
         
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        online = {i+1: 1 for i in range(c)}
        graph = {i+1: [] for i in range(c)}
        for i, j in connections:
            graph[i].append(j)
            graph[j].append(i)
        
        for i in graph:
            graph[i].sort()
        
        res = []
        for i, j in queries:
            if i == 2:
                online[j] = 0
            else:
                # main logic goes here
                if online[j] == 1:
                    res.append(j)
                    online[j]
                else:
                    visited = {i+1: 0 for i in range(c)}
                    res.append(self.distance(graph, j, online, 1, visited))
                    # online[j] = 1
        
        return res

obj = Solution()
# print(obj.distance({1: [2], 2: [1, 3], 3: [2, 4], 4: [3, 5], 5: [4]}, 2, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, 1, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}))
# obj.processQueries(5, [[1,2],[2,3],[3,4],[4,5]], [[1,3],[2,1],[1,1],[2,2],[1,2]])
# obj.processQueries(3, [], [[1,1],[2,1],[1,1]])

obj.processQueries(3, [[3,2],[1,3],[2,1]], [[2,2],[1,2],[1,2],[1,3],[1,1],[1,3],[1,1],[1,1],[2,1],[1,1],[2,3],[2,3],[2,3],[2,1],[2,1],[2,1],[1,1],[1,1],[1,2],[1,2],[2,1],[2,1],[2,2],[1,2],[1,1]])