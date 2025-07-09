#!/usr/bin/env python3
from typing import List

def measure(arr: List[int]):
    s = sorted(set(arr))
    mapp = dict()
    counter = dict()
    for idx, val in enumerate(arr):
        try:
            mapp[val] += idx
            counter[val] += 1
        except:
            mapp[val] = idx
            counter[val] = 1
    
    res = 0
    last = 0
    for i in s:
        const = last + counter[i] - 1
        res += const * counter[i]
        res += mapp[i]
        last = const + 1

    return res

print(measure([1,1,1,1]))