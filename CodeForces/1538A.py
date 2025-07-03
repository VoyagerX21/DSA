t = int(input())

while t:
    n = int(input())
    arr = list(map(int, input().split()))
    mini = min(arr)
    smallest = min(arr.index(mini), n-arr.index(mini))
    maxi = max(arr)
    largest = min(arr.index(maxi), n-arr.index(maxi))
    print(smallest + largest)
    t -= 1