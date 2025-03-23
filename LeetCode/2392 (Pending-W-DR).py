from typing import List

class Solution:
    def hasCycle(self, graph) -> bool:
        def dfs(node, visited, recStack):
            visited.add(node)
            recStack.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    if dfs(neighbor, visited, recStack):
                        return True
                elif neighbor in recStack:
                    return True
            recStack.remove(node)
            return False

        visited = set()
        recStack = set()
        for node in graph:
            if node not in visited:
                if dfs(node, visited, recStack):
                    return True

        return False

    def dfs(self, graph, count, start) -> None:
        for i in graph[start]:
            count[i] += 1
            self.dfs(graph, count, i)

    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row = {_+1: 0 for _ in range(k)}
        col = {_+1: 0 for _ in range(k)}
        row_graph = {_+1: set() for _ in range(k)}
        col_graph = {_+1: set() for _ in range(k)}
        for s, e in rowConditions:
            row_graph[s].add(e)

        for s, e in colConditions:
            col_graph[s].add(e)

        if self.hasCycle(row_graph):
            return []

        if self.hasCycle(col_graph):
            return []

        for i in range(k):
            self.dfs(row_graph, row, i+1)

        for i in range(k):
            self.dfs(col_graph, col, i+1)

        res = [[0]*k for _ in range(k)]
        for i in range(1, k+1):
            if res[row[i]][col[i]] != 0:
                for j in range(k):
                    if res[j][col[i]] != 0:
                        res[j][col[i]] = i
                        break
            else:
                res[row[i]][col[i]] = i

        return res


obj = Solution()
obj.buildMatrix(8, [[1, 2], [7, 3], [4, 3], [5, 8], [7, 8], [8, 2], [5, 8], [3, 2], [1, 3], [7, 6], [4, 3], [7, 4], [4, 8], [7, 3], [7, 5]], [[5, 7], [2, 7], [4, 3], [6, 7], [4, 3], [2, 3], [6, 2]])