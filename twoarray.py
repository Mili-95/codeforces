t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = map(int, input().split())
    b = map(int, input().split())
    a = sorted(a)
    b = sorted(b, reverse=True)
    for i in range(k):
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]
    print(sum(a))        

