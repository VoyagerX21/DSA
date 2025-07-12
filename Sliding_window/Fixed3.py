# Problem statement : Given a word pat and a text txt. Return the count of the occurrences of anagrams of the word in the text.
# Example :
# Input txt = "forxxorfxdofr", pat = "for"
# Output 3
# Explanation: for, orf and ofr appears in the txt, hence answer is 3.

# from typing import List
from collections import Counter

# @notworking
# def countAnangrams(pat: str, word: str):
#     mapp = dict()
#     original = dict()
#     for i in pat:
#         try:
#             original[i] += 1
#         except:
#             original[i] = 1
#         mapp[i] = 0

#     i, j, count, res = 0, 0, 0, 0
#     while j < len(word):
#         try:
#             if original[word[j]]:
#                 if mapp[word[j]] < original[word[j]]:
#                     mapp[word[j]] += 1
#                     count += 1
#             if j -i + 1 < len(pat):
#                 j += 1
#             elif j - i + 1 == len(pat):
#                 if count == len(pat):
#                     # compare both maps and increase res
#                     flag = True
#                     for k in pat:
#                         if original[k] != mapp[k]:
#                             flag = False
#                             break
#                     if flag:
#                         res += 1
                    
#                 # slide the window
#                 # bdhane se pehle condition check krlena
#                 try:
#                     if mapp[word[i]]:
#                         mapp[word[i]] -= 1
#                         count -= 1
#                 except:
#                     pass
#                 i += 1
#                 j += 1

#         except:
#             count = 0
#             for p in mapp:
#                 mapp[p] = 0
#             if j - i + 1 < len(pat):
#                 j += 1
#             elif j - i + 1 == len(pat):
#                 i += 1
#                 j += 1
    
#     return res

def countAnagrams(pat: str, word: str):
    original = Counter(pat)
    mapp = Counter()
    i, j, res = 0, 0, []
    while j < len(word):
        if word[j] not in original:
                mapp = Counter()
                j += 1
                i = j
                continue
        else:
            mapp[word[j]] += 1
        
        if j-i+1 < len(pat):
            j += 1
        
        elif j-i+1 == len(pat):
            if mapp == original:
                res.append(i)
            # mapp[word[i]] = max(mapp[word[i]]-1, 0)
            mapp[word[i]] -= 1
            if mapp[word[i]] == 0: # because counter stores key even if the value is zero so we need to delete it
                del mapp[word[i]]
            i += 1
            j += 1
    
    return res

res = countAnagrams("abc", "cbaebabacd")
print(res)