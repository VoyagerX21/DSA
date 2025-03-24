#CODE
t = int(input())
while t:
    n = int(input())
    ln = list(map(int, input().split()))
    res = 0
    i = 0
    while i < n:
        if ln[i] != 0:
            while i < n:
                if ln[i] == 0:
                    break
                i += 1
            res += 1
        else:
            i += 1
            
    print(res) 
    t -= 1