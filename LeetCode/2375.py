#!/usr/bin/env python3

def fn(s: str, res: str, curr: int, visited: dict):
    flag = s[curr]
    if flag == 'I':
        newNode = int(res[-1])+1
    else:
        newNode = int(res[-1])-1
    if visited[newNode] == 0:
        res += str(newNode)
        visited[newNode] = 1
        call = fn(s, res, curr+1, visited)
        if call == -1:
            last = res[-1]
            res = res[:-1]
            if flag == 'I':
                newNode = int(last) + 1
            else:
                newNode = int(last) - 1
            visited[int(last)] = 0
            if visited[newNode] == 0:
                res += str(newNode)
                visited[newNode] = 1
                call = fn(s, res, curr+1, visited)
                return call
            else:
                return -1
        else:
            return res
    else:
        return -1

if __name__ == "__main__":
    s = "IIIDIDDD"
    res = '1'
    curr = 0
    visited = {i+1: 0 for i in range(9)}
    visited[1] = 1
    fn(s, res, curr, visited)