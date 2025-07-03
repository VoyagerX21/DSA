#!/usr/bin/env python3
from typing import List

def nextLargerElement(arr: List[int]):
    res = [-1 for _ in range(len(arr))]
    st = [arr[-1]]
    i = len(arr) - 2
    while i >= 0:
        while st:
            if st[0] <= arr[i]:
                st.pop(0)
            else:
                break
        if st:
            res[i] = st[0]
        
        st.insert(0, arr[i])
        i -= 1
    
    return res

arr =[41, 88, 58, 69, 93, 42, 44, 25, 12, 47, 41, 88, 58, 69, 93, 42, 44, 25, 12, 47]
print(nextLargerElement(arr))