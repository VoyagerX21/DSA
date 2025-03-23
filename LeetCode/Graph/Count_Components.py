#!/usr/bin/env python3

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