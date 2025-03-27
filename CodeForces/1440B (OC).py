t = int(input())

while t:
    n, k = map(int, input().split())
    ln = list(map(int, input().split()))
    if k == 1:
        print(ln[((n*k)//2)-1])
    elif n == 2:
        print(sum([ln[i] for i in range(n*k) if i % 2 == 0]))
    else:
        c = 0
        start = n*k
        res = 0
        n -= 1
        while c < k:
            start -= n
            res += ln[start]
            c += 1
        print(res)
    t -= 1