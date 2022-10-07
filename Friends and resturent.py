for _ in range(int(input())):
    n = int(input())
    x = list(map(int,input().split()))
    y = list(map(int,input().split()))
    t = []
    for i in range(n):
        t.append(y[i]-x[i])
    t.sort()
    groups = 0
    l = 0
    r = n-1
    while l<r:
        if t[r] + t[l] >=0:
            groups += 1
            r -= 1
        l += 1
    print(groups)
    