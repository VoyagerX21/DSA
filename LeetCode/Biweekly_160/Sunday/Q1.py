from typing import List
import re

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        def validate_code(code: str):
            return re.search(r"^[a-zA-Z0-9_]+$", code)

        total_array = [[code[i], businessLine[i], isActive[i]] for i in range(len(code))]

        ptr = 0
        while ptr < len(total_array):
            i, j, k = total_array[ptr]
            if not (validate_code(i) and k):
                total_array.pop(ptr)
            else:
                ptr += 1

        d = ["electronics", "grocery", "pharmacy", "restaurant"]
        ds = {i: [] for i in d}
        for i in total_array:
            try:
                ds[i[1]].append(i[0])
            except:
                pass

        for i in d:
            ds[i].sort()

        print(ds)

obj = Solution()
obj.validateCoupons(["GROCERY15","ELECTRONICS_50","DISCOUNT10"], ["grocery","electronics","invalid"], [False,True,True])